# MyAastha Seva Bot

## Overview
**MyAastha Seva Bot** is a RAG-based AI chatbot designed to provide automated customer support for Aastha Co-operative Credit Society. The chatbot leverages **LangChain, ChromaDB, and Streamlit** to retrieve and generate accurate responses based on a custom knowledge base, including FAQs and official documentation.

## Features
- **Web Scraping & Data Collection**: Gathers information from `http://myaastha.in/` to build a comprehensive knowledge base.
- **RAG-based Retrieval**: Uses **ChromaDB** to store and retrieve relevant context for customer queries.
- **Generative AI Responses**: Powered by **Groq's LLAMA models** to generate accurate and user-friendly responses.
- **Memory-Enabled Conversations**: Remembers past interactions to provide contextual and coherent responses.
- **Streamlit UI**: User-friendly web interface for customers to interact with the chatbot.
- **80% Query Resolution Target**: Aims to automate customer support efficiently, reducing manual intervention.

## Tech Stack
- **Python**
- **LangChain**
- **ChromaDB** (Vector Database)
- **Streamlit**
- **Groq’s LLAMA models**
- **BeautifulSoup** (for Web Scraping)
- **dotenv** (for environment variables)

## Project Structure
```
MyAastha-Seva-Bot/
│── data/                # Processed knowledge base and vector storage
│── models/              # Fine-tuned models and embeddings
│── scripts/             # Web scraping and data processing scripts
│── app.py               # Streamlit UI for chatbot
│── rag_pipeline.py      # RAG model pipeline with LangChain & ChromaDB
│── requirements.txt     # Dependencies
│── .env                 # API keys and environment variables
│── README.md            # Project Documentation
```

## Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/arghads9177/myaastha-seva-bot.git
cd myaastha-seva-bot
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add the necessary API keys:
```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 5️⃣ Run the Chatbot
```bash
streamlit run app.py
```

## Future Enhancements
- ✅ **Deploy on DigitalOcean or any other cloud platform(AWS, GCP)**
- ✅ **Add More Data Sources for FAQs**
- ✅ **Enhance UI with User Authentication**
- ✅ **Improve Response Accuracy using LoRA Fine-tuning**

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For any queries, reach out to **[Argha Dey Sarkar]** at **email2argha@gmail.com**.

