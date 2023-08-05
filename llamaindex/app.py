import json
import os

from importing import *

openai.api_key = "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"


def construct_index(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist('storage')
    return index


def logdata(input_text: str, answer: str):
    with open('logs/chatbox.json', 'a') as logfile:
        data = {
            "datetime": datetime.now().strftime(r'%d/%m/%Y %H:%M:%S'),
            "Question": input_text,
            "Answer": answer
        }
        json.dump(data, logfile)
        logfile.write(os.linesep)


def chatbot(input_text):
    if not input_text:
        return ""
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    # log
    logdata(input_text, response.response)

    return response.response


def main():
    input_text = st.text_area("Enter your prompt")
    if st.button(label="Submit"):
        st.write(chatbot(input_text))


if __name__ == "__main__":
    directory_path = 'docs'
    file_name = 'list_of_directory/directory.json'
    new_file_list = os.listdir('docs')

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            old_files_list = json.load(f)
        if old_files_list == new_file_list:
            main()
        else:
            with open(file_name,'r')as file:
                json.dump(new_file_list,file)
            construct_index(directory_path)
            main()

    else:
        with open(file_name, 'w') as file:
            json.dump(new_file_list, file)
