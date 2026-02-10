import gradio as gr
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load once (Phi-3-mini = fast)
model_name = "Qwen/Qwen2.5-3B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

def generate(text, max_tokens, use_cache):
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    torch.cuda.empty_cache()
    
    start = time.time()
    with torch.no_grad():
        output = model.generate(
            **inputs, 
            max_new_tokens=int(max_tokens),
            do_sample=True, 
            temperature=0.7,
            use_cache=use_cache,
            pad_token_id=tokenizer.eos_token_id
        )
    elapsed = time.time() - start
    
    mem_peak = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else 0
    result = tokenizer.decode(output[0][len(inputs['input_ids'][0]):], skip_special_tokens=True)
    
    return result, f"Time: {elapsed:.2f}s | Mem: {mem_peak:.2f}GB"

# Live demo
demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt", value="Explain KV-cache"),
        gr.Slider(10, 100, 30, step=10, label="Max Tokens"),
        gr.Checkbox(label="Use KV-Cache", value=True)
    ],
    outputs=[
        gr.Textbox(label="Generation", lines=6),
        gr.Textbox(label="Performance")
    ],
    title="KV Cache Performance Demo",
    description="Toggle cache to see speedup/memory diff!"
)

demo.launch(share=True, debug=True)
