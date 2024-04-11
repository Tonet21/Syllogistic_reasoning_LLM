from transformers import AutoModelForCausalLM, AutoTokenizer
from syllos import Complete_prompts

model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-v0.1", device_map="auto")

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-v0.1")


for pro in Complete_prompts:
    prompt = pro

    model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

    generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)

    tokenizer.batch_decode(generated_ids)[0]