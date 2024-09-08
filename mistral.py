from huggingface_hub import snapshot_download
from pathlib import Path
from mistral_inference.model import Transformer
from mistral_inference.generate import generate
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from long_prompt import prompts,system_message
from mistral_common.protocol.instruct.messages import SystemMessage



access_token = "hf..."


local_model_dir = ""
mistral_models_path = Path(local_model_dir)
mistral_models_path.mkdir(parents=True, exist_ok=True)

# Download the model
snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"],
    local_dir=local_model_dir,
    token=access_token
)



tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
model = Transformer.from_folder(mistral_models_path)


import re

import re

def extract_conclusion(text):

    pattern = r"(the correct answer is|the valid conclusion is|therefore)\s*(.*)"


    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        # Return the text that follows the matched phrase
        return match.group(2).strip()
    else:
        return text

def remove_quotes(text):

    return text.replace('"', '').replace("'", "")

def fix_comma_and_capitalization(text):

    text = text.lstrip(',').strip()

    if text:
        text = text[0].upper() + text[1:]

    return text

model_conclusions = []

system_message = SystemMessage(content=system_message)

for prompt in prompts:

    completion_request = ChatCompletionRequest(messages=[system_message, UserMessage(content=prompt)])

    tokens = tokenizer.encode_chat_completion(completion_request).tokens


    out_tokens, _ = generate([tokens], model, max_tokens=256, temperature=0.1, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
    result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])
    result = extract_conclusion(result)
    result = remove_quotes(result)
    result = fix_comma_and_capitalization(result)
    model_conclusions.append(result)
