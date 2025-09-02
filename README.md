## 📝 MCQ Generator using LangChain & Streamlit

This project is a Multiple Choice Question (MCQ) Generator built with Streamlit, LangChain, and OpenAI.
It allows you to upload text, specify quiz parameters (like subject, tone, and number of questions), and automatically generate MCQs with options and answers.

## 🚀 Features

– 📂 Upload a text file (study material, notes, or articles).
– 🎯 Generate MCQs automatically based on the content.
– ⚡ Customize quiz parameters (number of questions, subject, and tone).
– 📊 View results as a table or in readable Q&A format.
– ✅ Includes AI-generated review/feedback on the quiz.

## 🛠️ Tech Stack

– Python 3.8+
– Streamlit – For interactive UI
– LangChain – Prompt engineering & OpenAI integration
– OpenAI API – For quiz generation
– Pandas – For table data handling

## 📂 Project Structure
```
├── src/
│   ├── mcqgenerator/
│   │   ├── MCQGenerator.py   # Quiz generation logic
│   │   ├── utils.py          # File reading & table conversion helpers
│   │   ├── logger.py         # Logging
│   │   └── __init__.py
├── StreamlitAPP.py            # Main Streamlit app
├── requirements.txt           # Dependencies
├── .env                       # API keys (not pushed to Git)
└── README.md                  # Project documentation
```

## ⚙️ Setup & Installation

1. Clone the repository
```
git clone https://github.com/your-username/mcq-generator.git
cd mcq-generator
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Set up environment variables
Create a .env file in the root folder and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

5. Run the Streamlit app
```
streamlit run StreamlitAPP.py
```
## 📖 Usage

1. Upload a .txt file with study material.
2. Enter the number of questions, subject, and tone (e.g., "formal", "casual").
3. Click Generate.
4. The app will display:
– A table of MCQs with options and correct answers.
– A readable format (Q & Options).
– AI-generated review/feedback about the quiz.

## 🖼️ Example Output

Readable Format
```
Q1: What is the capital of France?  
a) Berlin  
b) Madrid  
c) Paris  
d) Rome  

✅ Correct Answer: c) Paris
```
## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements.

📜 License

This project is licensed under the MIT License.
