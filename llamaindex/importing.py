from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.node_parser import SimpleNodeParser
import os
from llama_index import StorageContext, load_index_from_storage
from llama_index import Document
import openai
from llama_index.evaluation import DatasetGenerator
import json
from datetime import datetime
import streamlit as st