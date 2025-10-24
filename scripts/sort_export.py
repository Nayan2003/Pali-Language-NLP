# scripts/sort_export.py
import pandas as pd
import os

# Ensure outputs folder exists
os.makedirs('outputs', exist_ok=True)

# Step 1 — Load the frequency data (from Step 3)
df = pd.read_csv('outputs/pali_word_frequency.csv')

# Step 2 — Sort by Frequency (descending)
df = df.sort_values(by='Frequency', ascending=False).reset_index(drop=True)

# Step 3 — Optional: add Romanized column placeholder
# (filled in next step — Romanization)
df['Romanized'] = ''

# Step 4 — Reorder columns for clarity
df = df[['Pali_Word', 'Romanized', 'Frequency']]

# Step 5 — Export clean version
df.to_csv('outputs/pali_word_frequency_sorted.csv', index=False, encoding='utf-8')
print("✅ Sorted frequency file saved to outputs/pali_word_frequency_sorted.csv")

# Display top 10 for quick check
print(df.head(10))
