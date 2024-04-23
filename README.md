When installing the requirements, change the cuda version of torch to your cuda. Now it is set at cu121 (12.1 version).

There are a few files: 
syllos: produces a list of the 256 from a dictionary called sylloExamples, which can be changed.
v_syllos: produces two lists; one produces the conclusions of the valid syllogisms (using the same dictionary), and one formats the models' conclusions.
Mixtral: runs the mixtral model and creates a list with its responses. In this file you need an access token from hugging face, just add your token as the variable acccess_token.
Eval: Create a CSV file with four columns: the first premise of the syllogism, the second premise, the model's conclusion, and the theoretical conclusion.

To create the CSV file directly, run Eval.py.
