from transformers import AutoModelForCausalLM, AutoTokenizer
import syllos

access_token = ""

model = AutoModelForCausalLM.from_pretrained("mistralai/Mixtral-8x7B-v0.1", token= access_token, device_map="auto")

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mixtral-8x7B-v0.1")

model_conclusions = []
for pro in syllos.Complete_prompts:
    prompt = pro

    model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")

    generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)

    model_conclusion =tokenizer.batch_decode(generated_ids)[0]

    model_conclusions.append(model_conclusion)
