import re

def load_data():
    with open("../data/fifa2026.txt") as f:
        fifa = f.readlines()
    fifa = [item.strip() for item in fifa if item != '\n']
    msgs = []
    for i, text in enumerate(fifa):
        match = re.search(r'\[@([^\s]+)', text)
        rest, post = text.rsplit(sep="M]")
        if match and post:
            msgs.append({"user_id":match.group(1), "message":post})
        else:
            print(f"{i}: Not found")
load_data()