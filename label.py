import json
import numpy as np

with open("hand_data.json", "r") as f:
    data = json.load(f)

X = []
y = []
labeled_data = {}  # <-- Add this line

for frame_str, hands in data.items():
    frame = int(frame_str)
    
    if not hands:
        continue  

   
    coords = [v for pt in hands[0] for v in (pt['x'], pt['y'], pt['z'])]

    #label
    if 0 <= frame <= 94:
        label = "one"
    elif 95 <= frame <= 195:
        label = "Hello"
    elif 196 <= frame <= 294:
        label = "okay"
    elif 295 <= frame <= 386:
        label = "four"
    elif 387 <= frame <= 447:
        label = "five"
    elif 448 <= frame <= 530:
        label = "A"
    elif 531 <= frame <= 648:
        label = "C"
    elif 649 <= frame <= 760:
        label = "E"
    elif 761 <= frame <= 838:
        label = "like"
    else:
        continue  # ngoài vùng

    X.append(coords)
    y.append(label)

    labeled_data[frame_str] = {  # <-- Move this inside the loop
        "landmarks": [hands[0]],  # Save as list of dicts, not flat list
        "label": label
    }

print(f"total: {len(X)}")
print(f"Label: {set(y)}")

with open("hand_data_labeled.json", "w") as f:
    json.dump(labeled_data, f, indent=2)
