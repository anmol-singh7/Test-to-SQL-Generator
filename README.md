# Text-to-SQL-Generator

## Project Overview

This project uses Google's Gemini AI model to generate SQL queries from natural language questions. The application allows users to input questions in plain English, which are then converted into SQL queries that are executed on a SQLite database. The results are then displayed in the Streamlit app.

## Prerequisites
1) **Python** (version 3.9+ recommended)
2) **Google API Key** for Gemini AI (add it in the .env file)

### Setup Instructions
1) **Clone the Repository:**
```bash
git clone https://github.com/anmol-singh7/Text-to-SQL-Generator.git
cd Text-to-SQL-Generator
```
2) **Install Dependencies:** Use requirements.txt to install all necessary packages:

```bash
pip install -r requirements.txt
```

### 3. Environment Variable:
- Create a `.env` file in the root directory.
- Add your Google Gemini API key in `.env`:
```bash
GOOGLE_API_KEY=your_google_api_key
```


### Database Setup:
Run sqlite.py to create the student.db database with some sample student records.

```bash
python sqlite.py
```


### Running the Application
1) Start the Streamlit Application:
```bash
streamlit run sql.py
```
2) Access the Application:
- Once the application starts, a URL will be displayed in the terminal, such as http://localhost:8501.
- Open the URL in a web browser to access the application.

