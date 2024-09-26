from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_communtiy.llms import Ollama

import streamlit as st
import os
import dotenv import load_dotenv

load_dotenv()