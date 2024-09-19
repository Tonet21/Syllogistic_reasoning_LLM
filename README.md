# SYLLOGISTIC REASONING IN LLMS


This project aims to know how many times an LLM draws every type of conclusion based on the two premises of the 64 available syllogisms.

When pip installing the requirements, change the Cuda version of torch to your Cuda. Now it is set to cu121 (12.1 version).
These particular models need a hugging face key; remember to use them in the models. The code already has a variable called "access_token", so you know where to set it. If you prefer using environment variables, remember to change the code.


There are a few files: 

- The syllos.py produces a list of 64 sets of premisses and its four possible conclusions based on triplets. You can modify the triplets list; for every triplet, you will get a set of 64 syllogisms (without the conclusion) and a list of the four possible conclusions (NVC is not considered here). For every triplet, you will get two nested lists (one list for 64 lists): the first one contains the  first premise, the second premise, the mood, and the figure. The second list is the possible conclusions. In this case, for 30 triplets, you will get two nested lists. Each list will contain 30 lists, and each of those lists will contain 64 lists.

- The prompt.py produces the prompts. It is fed with the lists from syllo.py to generate a prompt for each syllogism.

- The files llama3.py and mistral.py run the model, and the code also cleans its output. If a different output is needed, these functions can be modified. They use the prompts generated on the prompt.py file.

- The files mistal_conclusions and llama3_conclusions are fed the model's already-cleaned output; then, they refine the output to the desired format and classify the results. After that, two Excel files are produced: the first one contains a table that counts how many times a conclusion type (A, E, I, O, NVC) was drawn for the 16 possible moods. The second file counts how many times a conclusion type is drawn for every figure of the 16 moods (so, for the 64 syllogisms)


DISCLAIMER: This code may not be the most efficient, but it works. If you are concerned about efficiency, you are welcome to modify it.


