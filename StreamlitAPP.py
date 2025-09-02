import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain_community.callbacks.manager import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain 
from src.mcqgenerator.logger import logging





with open("Response.json", "r") as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQ Cretor Application with LangChain") 

with st.form("user_inputs"):
    uploaded_file=st.file_uploader("Upload a PDF or text file")

    mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

    subject=st.text_input("Insert Subject",max_chars=20)

    tone=st.text_input("Complexity Level of Questions", max_chars=20, placeholder="simple")

    button=st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cd:
                    response=generate_evaluate_chain.invoke(
                        {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                            }
                    )

                
                quiz = response.get("quiz", None)
                if quiz is not None:
                    table_data = get_table_data(quiz)
                    if table_data is not None:
                        for idx, q in enumerate(table_data, 1):
                            st.markdown(f"**Q{idx}. {q['MCQ']}**")
                            options = q["Choices"].split(" || ")
                            for opt in options:
                                st.write(f"- {opt}")
                            st.markdown(f"**Correct Answer:** {q['Correct']}")  
                            st.write("---")  

                        st.text_area(label="Review", value=response["review"])
                else:
                    st.error("Error in the table data")

            except Exception as e:
                print(f"Total Tokens:{cd.total_tokens}")
                print(f"Prompt_Tokens:{cd.prompt_tokens}")
                print(f"Completion Tokens:{cd.completion_tokens}")
                print(f"Total Cost:{cd.total_cost}")

                if isinstance(response,dict):

                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)

                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)
