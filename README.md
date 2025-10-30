# Text-to-SQL Query Helper Tool

A Streamlit-based web application that converts natural language text into SQL queries using the Groq LLM API.

## Features

- Convert natural language questions into SQL queries
- Support for multiple SQL dialects:
  - Standard SQL
  - MySQL
  - PostgreSQL
  - SQLite
- Interactive web interface built with Streamlit
- Powered by Groq's LLaMA 3.3 70B model

## Prerequisites

- Python 3.x
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mayank1Bhardwaj/NLP-Project.git
cd text-2-sequel
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your natural language question about the database in the text area

4. Select the desired SQL dialect from the dropdown menu

5. Click the "Generate SQL Query" button to get the corresponding SQL query

## Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web application framework
- [Groq](https://groq.com/) - LLM API provider
- [LangChain](https://python.langchain.com/) - LLM framework
- [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
