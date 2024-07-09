When installing the requirements, change the cuda version of torch to your cuda. Now it is set to cu121 (12.1 version).

The model is quite heavy; consider using quantization (these changes have to be made in the Mixtral.py file; to use this method, you
need GPU):



        quantization_config = BitsAndBytesConfig(

                load_in_4bit=True,

                bnb_4bit_quant_type="nf4",

                bnb_4bit_compute_dtype="torch.float16", 
        )        

        model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-Instruct-v0.1", token= access_token, quantization_config=True, device_map="auto




There are a few files: 
syllos: produces a list of the 64 from a dictionary called sylloExamples, which can be changed.
Mixtral: runs the mixtral model and creates a list with its responses. In this file, you need an access token from hugging face; just add your token as the variable acccess_token.
Eval: This file creates an Excel file with the count of the times a given conclusion is given for each of the 16 moods.

To create the CSV file directly, run Eval.py.

If you want to use more models, you have to use the same template but change the model name on the Mixtral.py file (make sure that transformers of huggingface support the model).

###DISCLAIMER###

This project was part of my internship. I'm currently working on optimizing it and expanding it to different models and languages. But this repo won't change.



