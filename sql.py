from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

my_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=my_api_key)

## Function to load Google GEmini Model
def get_gemino_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([*prompt, "\n\n", question])
    # Remove any markdown formatting such as ```sql ``` around the SQL command
    cleaned_sql = response.text.replace("```sql", "").replace("```", "").strip()
    return cleaned_sql

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt = [
    """
    You are an expert in converting English questions to SQL code! The SQL database 
    is named STUDENT and has the following columns - NAME, CLASS, and SECTION.
    
    Example 1 - How many records are present?
    The SQL command should be: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class?
    The SQL command should be: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';

    Note: The SQL code should not include any ``` or "sql" formatting. Please output only the SQL query text.
    """
]

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    sql = get_gemino_response(question, prompt)
    st.write(f"Generated SQL Query: {sql}")  # Display the generated query for debugging

    try:
        response = read_sql_query(sql, "student.db")
        st.subheader("The Response is")
        for row in response:
            st.header(row)
    except sqlite3.OperationalError as e:
        st.error(f"An error occurred: {e}")
