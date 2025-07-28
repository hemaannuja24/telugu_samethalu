from transformers import pipeline

# Load once and reuse
classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

# Define the candidate labels (in English internally)
CATEGORIES = {
    "Family": "కుటుంబం",
    "Friendship": "స్నేహం",
    "Morality": "నీతి",
    "Hard Work": "శ్రమ",
    "Knowledge": "జ్ఞానం",
    "Devotion": "భక్తి",
    "Culture": "సంస్కృతి",
    "Literature": "సాహిత్యం",
    "Humility": "వినయం",
    "Patience": "సహనం",
    "Courage": "ధైర్యం",
    "Arrogance": "అహంకారం",
    "Love": "ప్రేమ",
    "Greed": "దురాశ",
    "Wisdom": "ఆలోచన",
    "Responsibility": "బాధ్యత",
    "Satire": "వ్యంగ్యం",
    "Politics": "రాజకీయం",
    "Wealth": "ధనము",
    "Time": "సమయం"
}

def classify_proverb(text):
    result = classifier(text, list(CATEGORIES.keys()))
    top_label = result["labels"][0]
    return CATEGORIES[top_label]
