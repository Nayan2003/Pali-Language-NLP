import pandas as pd
from collections import Counter
import json
import os

# Make sure output folder exists
os.makedirs('outputs', exist_ok=True)

# Step 1 — Load tokenized data (replace path if needed)
# Example: if your tokenized words are saved as tokenized_samannaphala.json
with open('data/tokenized_samannaphala.json', 'r', encoding='utf-8') as f:
    tokens = json.load(f)

# Step 2 — Count word frequencies
word_counts = Counter(tokens)

# Step 3 — Convert to DataFrame
df = pd.DataFrame(word_counts.items(), columns=['Pali_Word', 'Frequency'])

# Step 4 — Sort by frequency (descending)
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Step 5 — Save the result
df.to_csv('outputs/pali_word_frequency.csv', index=False, encoding='utf-8')
print("✅ Frequency list saved successfully to outputs/pali_word_frequency.csv")

# Display top 10
print(df.head(10))
