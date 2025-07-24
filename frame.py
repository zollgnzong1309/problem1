import json

with open("hand_data.json", "r") as f:
    data = json.load(f)

total_frames = len(data)
valid_frames = sum(1 for v in data.values() if v and len(v[0]) == 21)

print(f"Total frame: {total_frames}")
print(f"frame has data of hand: {valid_frames}")
