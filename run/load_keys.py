import os

# Read keys.txt from 2 dirs above
keys_path = ("../../keys.txt")
with open(keys_path) as f:
    keys = f.readlines()
    
for line in keys:
    if line.startswith("OpenAI: "):
        os.environ["OPENAI_API_KEY"] = line.split(": ")[1].strip()
    if line.startswith("HuggingFace: "):
        os.environ["HF_TOKEN"] = line.split(": ")[1].strip()
    if line.startswith("Claude: "):
        os.environ["ANTHROPIC_API_KEY"] = line.split(": ")[1].strip()
    if line.startswith("Gemini: "):
        os.environ["GEMINI_API_KEY"] = line.split(": ")[1].strip()
