# Fake File Generator
# A small python program to generate a bunch of fake files that should light up cybersecurity heuristics and detections
#
# Blog Post: https://appliedscience.group/blog/tutorials/data-exfiltration-with-github-com-as-a-vector/
# 
#

import random
import os

# A list of words that sound like they have to do with cybersecurity
software_words = [
    "Techify",
    "DataFlow",
    "NetGuard",
    "CyberLink",
    "InfoSecure",
    "CloudSync",
    "WebSphere",
    "CodeMaster",
    "PixelPro",
    "FireWall",
    "SoftWave",
    "DataBridge",
    "QuantumCore",
    "LogicGate",
    "BitStream",
    "DataWizard",
    "NetSentry",
    "CodeGenius",
    "PixelCraft",
    "FireFence",
    "SoftSentry",
    "DataShield",
    "QuantumLink",
    "LogicStream",
    "BitGuard",
]

# A list of fake words / lorem ipsum for generating fake files
fake_words = [
    "lorem",
    "ipsum",
    "dolor",
    "sit",
    "amet",
    "consectetur",
    "adipiscing",
    "elit",
]

# Generate random IP addresses that are valid
def generate_random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# Generate fake content for files
def generate_fake_content():
    content = []
    content.append("Words:")
    content.extend(random.sample(fake_words, 4))
    content.append("\nIP Addresses:")
    content.extend([generate_random_ip() for _ in range(3)])
    content.append("\nOther Information:")
    content.append("Sample Text")
    return "\n".join(content)

# Generate 50 random textfiles full of content that should light up heuristics
for i in range(50):
    # Randomly select a software-sounding word for the filename
    software_word = random.choice(software_words)
    filename = f"{software_word}_{i}.txt"
    
    # Generate fake content for the file
    content = generate_fake_content()
    
    # Write the fake content to the file
    with open(filename, "w") as file:
        file.write(content)
    
    print(f"File '{filename}' created with fake content.")
