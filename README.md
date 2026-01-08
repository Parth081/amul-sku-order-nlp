# 🥛 Amul SKU NLP (spaCy)

A **production-ready NLP pipeline** built with **spaCy** to extract structured **Amul product order information** from free-form text and voice-transcribed inputs.

Designed to work reliably on **real-world noisy inputs** such as chat messages, call transcripts, and distributor order notes.

---

## 🚀 Features

- **Product detection**  
  Identifies Amul products like Milk, Butter, etc.

- **Variant inference**  
  Detects variants such as *Taza, Almond, Soy, Raw, Full Cream*

- **Quantity & unit extraction**  
  Handles values like `500 ml`, `1.5 L`, `200 gm`

- **Noise-tolerant preprocessing**  
  Robust to conversational and unstructured text


## 🧪 Example

### Input
book amul taza milk 500 ml



### Output
json
{
  "product": "Amul Taza Milk",
  "variant": "taza",
  "quantity": ["500"],
  "unit": ["ml"]
}

🏗 Architecture Overview
High-Level Flow

flowchart TD
    A[User / Voice Input] --> B[Text Preprocessing]
    B --> C[spaCy NER Model]
    C --> D[Product Detection]
    D --> E[Rule Engine]
    E --> F[Quantity & Unit Extraction]
    F --> G[Variant Inference]
    G --> H[Structured Output]
Design Principles
Machine Learning (spaCy NER)
Used only for product name detection to allow generalization

Rule-based extraction
Used for quantities and units for deterministic accuracy

Keyword-based logic
Used for variant inference to match business rules

📁 Project Structure

amul-sku-nlp/
│
├── src/                # Core NLP logic & training code
├── examples/           # Demo scripts and usage examples
├── model/              # Trained spaCy model (generated, not committed)
├── requirements.txt
└── README.md

⚙️ Setup & Usage

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Train the model

python src/train.py

3️⃣ Run demo

python -m examples.demo

📌 Use Cases
🎙 Voice-based ordering systems

📱 Distributor & retailer mobile apps

🏪 POS / ERP order ingestion

🤖 Chatbots & WhatsApp ordering

📝 Notes
Train once, reuse across multiple applications

Trained model files are intentionally excluded from Git

Easily extensible for:

New products

New variants

Additional units

Other FMCG brands

🚧 Future Enhancements
Multi-brand SKU extraction

Quantity–unit pairing (e.g., 500 ml × 10)

REST API using FastAPI

Multilingual support

Confidence scoring for entities

✅ Tech Stack
Python 3.x

spaCy

Regex & Rule-based NLP

📄 License
This project is intended for internal / educational / POC use.
Add a license file if required.


### ✅ What this README gives you
- Professional GitHub-ready formatting
- Clear architecture diagram (renders natively on GitHub)
- Clean examples
- Enterprise-friendly explanation

If you want next:
- GitHub **badges**
- **FastAPI** deployment README
- **Voice → text → SKU** pipeline diagram
- **Multi-brand extension**

Just say the word 🚀

