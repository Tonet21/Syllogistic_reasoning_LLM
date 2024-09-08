from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from long_prompt import prompts, system_message
import re

access_token = "hf..."

model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    token=access_token
)

import re

def extract_conclusion(text):
    # Regex pattern to match the conclusion
    pattern = r"Conclusion:\s*(All.*?|Some.*?|No.*?|NVC.*?)\s*\n"

    # Search for the pattern in the provided text
    match = re.search(pattern, text, re.DOTALL)

    if match:
        return match.group(1).strip()
    else:
        return None


# Initialize an empty list to store the model's responses
model_conclusions = []

# Process each prompt
for prompt in prompts:
    # Combine the system message and user prompt
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]

    # Apply chat template to format the conversation
    input_ids = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    ).to(model.device)


    # Define the terminators
    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("")
    ]

    # Generate a response using the model with the specified temperature and top_p
    outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    pad_token_id=tokenizer.eos_token_id,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
        )

    # Decode the generated tokens to text
    response = outputs[0][input_ids.shape[-1]:]
    decoded_response = tokenizer.decode(response, skip_special_tokens=True)
    #decoded_response = extract_conclusion(decoded_response)
    model_conclusions.append(decoded_response)
