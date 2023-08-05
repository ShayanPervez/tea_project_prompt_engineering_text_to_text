from langchain import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate
import streamlit as st

questions = [
    "To begin with your name, can you please share in 30 words an ambitious aspiration that you want to work on and why?",
    "Could you please, expand upon your answer for me",
    "What will be the reward or payoff if you are successful in achieving your ambitious aspiration?",
    "On a scale of 1-10, how would you describe your energy levels as you think about your ambitious aspiration e.g. 1 comatose, 10 fired up beyond belief",
    "To enable me to explore your inner voice, can you take a moment to think back to one of your most embarrassing or memorable failures. Do you have one in mind?",
    "Please share a brief summary of that situation with me.",
    "Have you been able to let go emotionally from this failure?(answer in yes or no)",
    "Did you learn from the failure?(answer in yes or no)",
    "Tell me more about the biggest learning for you from this failure?",
    "When your inner voice gets in the way of making progress against your aspirations, what does that conversation sound like?",
    "When you hear your inner voice getting negative, telling you that you are going to fail, are you able to reassure yourself that you will in fact be successful?",
    "Could you please describe the reassurance techniques that you use?"

]

full_template = """
    {introduction}
    Question: {my_question}
    Answer: {my_answer}
"""

introduction_template = """
You are a growth mindset coach giving supportive feedback. Your Job is following:
   1. System will ask it's Question.
   2. User will provide Answer based on Question asked by system.
   3.Based on those Answer you will provides answer to the user provided Answer taking references from the uploaded documents and providing the best inference.
   Note:- While Inferring you should not take any reference or any person's name , expectation is just inference to the questions is needed.
"""

prompt = PromptTemplate(
    input_variables=["introduction", "my_question", "my_answer"],
    template=full_template
)

for i in range(0, len(questions)):
    question_template = questions[i]
    answer_template = st.text_area(question_template)
    out = prompt.format(introduction=introduction_template, my_question=question_template, my_answer=answer_template)
    if st.button(label=f"Submit Question: {i}"):
        st.write(out)

