When installing the requirements, change the cuda version of torch to your cuda. Now it is set to cu121 (12.1 version).

The model is quite heavy, consider using quantization (these changes have to be made in the Mixtral.py file):



        quantization_config = BitsAndBytesConfig(

                load_in_4bit=True,

                bnb_4bit_quant_type="nf4",

                bnb_4bit_compute_dtype="torch.float16", 
        )        

        model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-v0.1", token= access_token, quantization_config=True, device_map="auto




There are a few files: 
syllos: produces a list of the 256 from a dictionary called sylloExamples, which can be changed.
v_syllos: produces two lists; one produces the conclusions of the valid syllogisms (using the same dictionary), and one adapts the models' conclusions.
Mixtral: runs the mixtral model and creates a list with its responses. In this file you need an access token from hugging face, just add your token as the variable acccess_token.
Eval: Create a CSV file with four columns: the first premise of the syllogism, the second premise, the model's conclusion, and the theoretical conclusion.

To create the CSV file directly, run Eval.py.

If you want to use more models, you have to use the same template but change the model name on the Mixtral.py file (make sure that transformers of hugging face support the model)
