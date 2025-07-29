from dotenv import load_dotenv

load_dotenv()

import streamlit as st

import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#models = genai.GenerativeModel('gemini-pro')


# models = genai.list_models()
# for m in models:
#     print(m.name)


def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("models/gemini-2.0-flash")

    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = ["""
You are an expert in converting English questions to SQL queries.
The SQL database is called 'student' and has the following columns:
- name (TEXT)
- class (TEXT)
- section (TEXT)
- marks (INTEGER)

Provide without any explanation or formatting (no backticks, no 'SQL:' prefix).

Example:
Question: How many entries of records are present?
Query: SELECT COUNT(*) FROM student;
Question:tell me all the students studying in datascience class?
Query:select * from student where class="Datascience"

"""]
st.set_page_config(page_title="I can retrive any SQL query")
st.header("Gemini App to retrive SQL Data")

question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")


if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,'student.db')
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
