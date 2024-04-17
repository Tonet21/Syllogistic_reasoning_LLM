import csv
import syllos
import v_syllos

# Define your headers
headers = ["First Premise", "Second Premise", "Model Conlusions", "Conclusions"]

# Open the CSV file in write mode
with open("data.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)

  # Write the header row
  writer.writerow(headers)

  # Extract first and second elements using list comprehension
  first_premises = [premise[0] for premise in syllos.premises]
  second_premises = [premise[1] for premise in syllos.premises]

  # Write each element to a separate column
  for first_premise, second_premise, model_conclusion, conclusion in zip(first_premises, second_premises, v_syllos.CsMood, v_syllos.vcMood):
    writer.writerow([first_premise, second_premise, model_conclusion, conclusion])

print("CSV file created successfully!")


