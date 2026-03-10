import os
import base64
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

# Create output folder
folder = "system2_duerer_caps"
os.makedirs(folder, exist_ok=True)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

prompt_template = """
Capital letter {letter} in the geometric Renaissance typeface construction style of Albrecht Dürer (1525).

Cream aged parchment background.
Deep burgundy letter (#5C1F1B).
Visible geometric construction grid with compass circles and Fibonacci spirals faintly in the background.
Consistent stroke thickness.
Elegant small Renaissance serifs.
Hand-drawn compass-and-straightedge aesthetic.
Renaissance manuscript illumination style.
Square composition.
"""

for letter in letters:

    prompt = prompt_template.format(letter=letter)

    
    result = client.images.generate(
    	model="gpt-image-1",
    	size="1024x1024",
    	prompt=prompt
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    filename = f"{folder}/{letter}_system2_duerer_caps.png"

    with open(filename, "wb") as f:
        f.write(image_bytes)

    print(f"saved {filename}")
