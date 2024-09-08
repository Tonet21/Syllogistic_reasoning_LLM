import re
from syllo import syllogisms
from collections import defaultdict
import pandas as pd
from syllo import possible_conclusions
from mistral import model_conclusions


import re

conclusions = []
i = 0

# Iterate over the syllogisms and process each conclusion
for prem1, prem2,mood, type_ in syllogisms:

    conclusion = model_conclusions[i]

    # Classify the conclusion based on its starting words
    if re.search("Some", conclusion):
        if re.search(".+not", conclusion):
            conclusion = [mood, possible_conclusions[i][3], "O", type_]
        else:
            conclusion = [mood, possible_conclusions[i][2], "I", type_]
    elif re.search("All", conclusion):
        conclusion = [mood, possible_conclusions[i][0], "A", type_]
    elif re.search("No", conclusion):
        conclusion = [mood, possible_conclusions[i][1], "E", type_]
    else:
        conclusion = [mood, "NVC", "NVC", type_]

    # Append the cleaned-up conclusion to the list
    conclusions.append(conclusion)
    i += 1


for conclusion in conclusions:
        print(conclusion)

conclusion_count = defaultdict(dict)
for syllo_mood, _, conclusion_mood, type_ in conclusions:
  conclusion_count[syllo_mood][conclusion_mood] = conclusion_count[syllo_mood].get(conclusion_mood, 0) + 1


type_count = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
for syllo_mood, _, conclusion_mood, type_ in conclusions:
    type_count[syllo_mood][type_][conclusion_mood] += 1



data = conclusion_count
columns = ["A", "E", "I", "O", "NVC"]


df = pd.DataFrame(index=data.keys(), columns=columns).fillna(0)
for key, inner_dict in data.items():
    for inner_key, count in inner_dict.items():
        df.at[key, inner_key] = count

df.reset_index(inplace=True)
df.rename(columns={"index": "syllogism"}, inplace=True)


excel_file_path = "mistral_syllogism_conclusions2.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"DataFrame saved to {excel_file_path}")


flattened_data = []
for mood, types in type_count.items():
    for type_, moods in types.items():
        row = {"syllogism": mood, "type": type_, "A": 0, "E": 0, "I": 0, "O": 0, "NVC": 0}
        for conclusion_mood, count in moods.items():
            row[conclusion_mood] = count
        flattened_data.append(row)

# Create a DataFrame
columns = ["syllogism", "type", "A", "E", "I", "O", "NVC"]
df = pd.DataFrame(flattened_data, columns=columns)

# Save the DataFrame to an Excel file
excel_file_path = "mistral_syllogism_type_conclusions2.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Excel file created at: {excel_file_path}")

