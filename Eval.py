import csv
from syllos import premises
from v_syllos import CsMood, vcMood

# Define your headers
headers = ["First Premise", "Second Premise", "Model Conlusions", "Conclusions"]

# Open the CSV file in write mode
with open("data.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)

  # Write the header row
  writer.writerow(headers)

  # Extract first and second elements using list comprehension
  first_premises = [premise[0] for premise in premises]
  second_premises = [premise[1] for premise in premises]

  # Write each element to a separate column
  for first_premise, second_premise, model_conclusion, conclusion in zip(first_premises, second_premises, CsMood, vcMood):
    writer.writerow([first_premise, second_premise, model_conclusion, conclusion])

print("CSV file created successfully!")


