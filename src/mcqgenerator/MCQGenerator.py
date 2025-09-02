#MCQGenerator.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_openai import ChatOpenAI  
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Load environment variables
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=key, temperature=0.7)

# ---------------- QUIZ GENERATION PROMPT ----------------
TEMPLATE = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions conform to the text.
Format your response like RESPONSE_JSON below.

### RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

quiz_chain = LLMChain(
    llm=llm,
    prompt=quiz_generation_prompt,
    output_key="quiz",
    verbose=True
)

# ---------------- QUIZ EVALUATION PROMPT ----------------
TEMPLATE2 = """
You are an expert English grammarian and writer. Given a Multiple Choice Quiz for {subject} students, \
evaluate the complexity of the questions and provide analysis in less than 50 words. \
If needed, update questions and tone so they match student ability.

Quiz_MCQ:
{quiz}
"""

quiz_evalution_prompt = PromptTemplate(
    input_variables=["subject", "quiz"],
    template=TEMPLATE2
)

review_chain = LLMChain(
    llm=llm,
    prompt=quiz_evalution_prompt,
    output_key="review",
    verbose=True
)

# FINAL SEQUENTIAL CHAIN 
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True
)


