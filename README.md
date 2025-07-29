 తెలుగు సామెతల ఖజానా (Telugu Proverbs Treasury)

A community-driven Streamlit web application to collect, preserve, and share timeless Telugu proverbs, along with their meanings and contextual usage.

---

##  Features

-  **Submit Proverbs**: Users can contribute their favorite Telugu proverbs with meanings and optional context.
-  **AI-based Categorization**: Automatically classifies each proverb into one of 20 thoughtful categories using a multilingual zero-shot model.
-  **Google Sheets Integration**: All entries are stored in a live Google Sheet, enabling easy access and transparency.
-  **Simple, Clean UI**: Built with Streamlit for an intuitive and culturally respectful experience.

---

##  Live Demo

🔗 [Open the App on Streamlit Cloud](https://telugusamethalu.streamlit.app/)  
🔗 [View Google Sheet of Proverbs](https://docs.google.com/spreadsheets/d/1J3j-IwOJr3iZlB9x_bc-7v3_L8QQE1_cZa45aA6V140/edit?gid=0#gid=0)

---

##  Tech Stack

- **Frontend & Logic**: [Streamlit](https://streamlit.io/)
- **ML Model**: `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` via HuggingFace Transformers
- **Backend**: Google Sheets API (via `gspread` and `oauth2client`)
- **Deployment**: Streamlit Cloud

---

##  AI Classification

The app uses a multilingual zero-shot classification model to predict the category of a proverb from 20 themes:
Family, Friendship, Morality, Hard Work, Knowledge, Devotion, Culture, Literature,
Humility, Patience, Courage, Arrogance, Love, Greed, Wisdom, Responsibility,
Satire, Politics, Wealth, Time


This is powered by HuggingFace’s [`pipeline`](https://huggingface.co/docs/transformers/main_classes/pipelines) abstraction.

---

##  Project Structure

```plaintext
├── app.py                 # Main Streamlit app
├── ai_classifier.py       # AI model and classification logic
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml       # Credentials (never commit this!)
├── .gitignore             # Ignore config & secret files
└── README.md              # Project documentation
