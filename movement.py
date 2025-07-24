import json
import matplotlib.pyplot as plt
import time

def simulate_hand_movement(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    plt.ion()  
    fig, ax = plt.subplots()

    for frame_idx in sorted(data.keys(), key=int):
        ax.clear()  
        frame_data = data[frame_idx]
        
        if frame_data:  
            hand = frame_data[0]  
            x = [pt['x'] for pt in hand]
            y = [pt['y'] for pt in hand]

            ax.scatter(x, y, c='blue')  
            ax.set_title(f"Frame {frame_idx}")
            ax.set_xlim(0, 1)
            ax.set_ylim(1, 0)  

        plt.pause(0.03)  

    plt.ioff()
    plt.show()

simulate_hand_movement("hand_data.json")

