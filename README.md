# 🕉️ Pali Language NLP Project

## 📘 Overview
This project aims to process and analyze ancient **Pali language texts** using modern **Natural Language Processing (NLP)** techniques.  
The main goal is to clean, structure, and interpret traditional Pali scriptures and make them computationally readable for research, linguistic analysis, and digital preservation.

---

## 🧠 Objectives
- To create **clean and normalized text corpora** from raw Pali scriptures.  
- To handle **Pali-specific challenges** like:
  - Replacement of symbols (e.g., `pe०`)
  - Multiple textual variants
  - Complex punctuation and markers
- To perform **morphological, syntactic, and semantic analysis** on the processed texts.
- To prepare datasets for further **machine learning and linguistic research**.

---

## ⚙️ Project Structure

| Task No. | Description | Status |
|-----------|-------------|--------|
| 0 | Create ready-to-read text (replace `pe०`, remove variants, handle punctuation) | ✅ Planned |
| 1 | Process **Sāmaññaphala Sutta (सामञ्‍ञफलसुत्तं)** — Tokenization, Cleaning, and Text Structuring | 🚧 In Progress |
| 2 | POS tagging and morphological analysis | ⏳ Pending |
| 3 | Lexical database and translation alignment | ⏳ Pending |
| 4 | Semantic relation mapping and Pali-English glossary generation | ⏳ Pending |

---

## 🧩 Tools & Libraries
- **Python 3.x**
- **NLTK / spaCy (custom models for Pali)**
- **Regular Expressions (Regex)**
- **Pandas / JSON** for database management
- **Jupyter Notebook / VS Code** for analysis

---

## 🗂️ Folder Structure
'''
Pali-Language-NLP/
│
├── data/
│ ├── raw_texts/
│ ├── cleaned_texts/
│ ├── variants_db.json
│
├── scripts/
│ ├── preprocess_pe.py
│ ├── tokenize_pali.py
│
├── outputs/
│ ├── processed_suttas/
│
├── README.md
└── requirements.txt
'''

---

## 🧾 Current Focus
**Task 1:** Working on _Sāmaññaphala Sutta_ text.  
Goals:
1. Load raw text  
2. Normalize and clean special characters  
3. Apply tokenization  
4. Prepare for further morphological analysis

---

## 👥 Team
**Project Lead:** Nayan Khuje  
**Research Focus:** Pali NLP, Linguistic Data Processing, and Semantic Structuring

---

## 📅 Timeline
| Phase | Task | Duration |
|--------|------|-----------|
| Phase 1 | Data Cleaning (Tasks 0–1) | Week 1–2 |
| Phase 2 | Morphological Analysis | Week 3–4 |
| Phase 3 | Lexical Database & Alignment | Week 5–6 |
| Phase 4 | Semantic Mapping | Week 7–8 |

---

## 📜 License
This project is for **academic and research purposes** under open collaboration.


## 🧩 Tools
- **Python 3.x**
- **Regex (re module)**
- **Indic NLP Library** *(for Devanagari processing)*
- **NLTK / spaCy (custom tokenizer)**

---

# 🕉️ Pali Language NLP Project

## 📘 Overview
This project aims to process and analyze ancient **Pali language texts** using modern **Natural Language Processing (NLP)** techniques.  
The main goal is to clean, structure, and interpret traditional Pali scriptures and make them computationally readable for research, linguistic analysis, and digital preservation.

---

## ⚙️ Task 1 — Sāmaññaphala Sutta (सामञ्‍ञफलसुत्तं)

### 📜 Input Sample (Devanagari)
> १५०. एवं मे सुतं – एकं समयं भगवा राजगहे विहरति जीवकस्स कोमारभच्‍चस्स अम्बवने महता भिक्खुसङ्घेन सद्धिं अड्ढतेळसेहि भिक्खुसतेहि।  
> ...  
> १५६. अञ्‍ञतरोपि खो राजामच्‍चो राजानं मागधं अजातसत्तुं वेदेहिपुत्तं एतदवोच – ‘‘अयं, देव, निगण्ठो नाटपुत्तो नाथपुत्तो (सी॰), नातपुत्तो (पी॰) सङ्घी चेव गणी च गणाचरियो च ञातो यसस्सी तित्थकरो साधुसम्मतो बहुजनस्स रत्तञ्‍ञू चिरपब्बजितो अद्धगतो वयोअनुप्पत्तो। तं देवो निगण्ठं नाटपुत्तं पयिरुपासतु। अप्पेव नाम देवस्स निगण्ठं नाटपुत्तं पयिरुपासतो चित्तं पसीदेय्या’’ति। एवं वुत्ते, राजा मागधो अजातसत्तु वेदेहिपुत्तो तुण्ही अहोसि।

---

### 🧾 Goals for Task 1
1. **Text Normalization**
   - Remove variant markers like `(सी॰)`, `(स्या॰)`, `(पी॰)`  
   - Handle inconsistent spellings (e.g., "नातपुत्तो" vs "नाथपुत्तो")  
   - Ensure uniform Unicode normalization (NFC form)
2. **Sentence Segmentation**
   - Split the paragraph into clean, single-sentence units for analysis
3. **Tokenization**
   - Break text into words, preserving Devanagari integrity  
   - Create a token list for further linguistic tagging
4. **Cleaning and Structuring**
   - Remove numbering (like `१५०.`) but store them as metadata  
   - Maintain a clean corpus for morphological analysis
5. **Output**
   - `cleaned_samanaphala.txt` (plain cleaned text)  
   - `tokens_samanaphala.json` (tokenized data)

---

## 🧠 Next Steps
- Implement text normalization using **Python + Regex**
- Build a tokenizer suited for **Pali (Devanagari script)**
- Create structured data outputs for NLP pipeline

---

## 🗂️ Folder Update
'''
Pali-Language-NLP/
│
## 🗂️ Folder Structure

Pali-Language-NLP/
│
├── data/
│   ├── raw_texts/
│   │   └── samanaphala_raw.txt
│   ├── cleaned_texts/
│   │   └── samanaphala_cleaned.txt
│
├── scripts/
│   ├── normalize_text.py
│   ├── tokenize_pali.py
│
├── outputs/
│   ├── samanaphala_tokens.json
│
├── README.md
└── requirements.txt


## 👤 Author
**Nayan Khuje**  
MSc Computer Science | Pali NLP Researcher | AI & Data Science Enthusiast
