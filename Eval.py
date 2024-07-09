import re
from syllo import syllogisms
from collections import defaultdict
import pandas as pd
from mixtral import model_conclusions


conclusions = []  
i = 0
for prem1, prem2,mood in syllogisms:
            
        conclusion = model_conclusions[i]
        if re.search("^Some", conclusion):
            if re.search(".+not", conclusion):
                conclusion = [mood, conclusion, "O"]
            else:
                conclusion = [mood, conclusion, "I"]
        elif re.search("^All", conclusion):
            conclusion = [mood, conclusion, "A"]
        elif re.search("^No", conclusion):
            conclusion = [mood, conclusion, "E"]
        else: 
            conclusion = [mood, conclusion, "NVC"]
    
        conclusions.append(conclusion)
        i += 1 


conclusion_count = defaultdict(dict)
for syllo_mood, _, conclusion_mood in conclusions:
  conclusion_count[syllo_mood][conclusion_mood] = conclusion_count[syllo_mood].get(conclusion_mood, 0) + 1


 
data = conclusion_count
columns = ["A", "E", "I", "O", "NVC"]


df = pd.DataFrame(index=data.keys(), columns=columns).fillna(0)
for key, inner_dict in data.items():
    for inner_key, count in inner_dict.items():
        df.at[key, inner_key] = count

df.reset_index(inplace=True)
df.rename(columns={"index": "syllogism"}, inplace=True)


excel_file_path = "syllogism_conclusions.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"DataFrame saved to {excel_file_path}")

