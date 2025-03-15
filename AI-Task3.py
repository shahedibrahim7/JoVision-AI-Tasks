import cv2
import numpy as np
import pandas as pd
import os

folder = "C:\\Users\\Lenovo\\Desktop\\JV\\JoVision-AI-Tasks\\task3"
output_file = os.path.join(folder, "results.xlsx")

areas = {
    'thumb': (144, 250, 200, 231),
    'index': (120, 142, 3, 120),
    'middle': (80, 103, 2, 112),
    'ring': (48, 72, 1, 108),
    'little': (2, 22, 2, 112)
}

data = []

def check_line(img):
    bottom_part = img[-3:, :]
    avg_brightness = np.mean(bottom_part)
    return 1 if avg_brightness > 100 else 0

def check_pressure(img, threshold):
    if check_line(img) == 0:
        return [0] * len(areas)
    right_half = img[:, img.shape[1] // 2:]
    pressures = []
    for name, (y1, y2, x1, x2) in areas.items():
        section = right_half[y1:y2, x1:x2]
        pressures.append(1 if np.any(section >= threshold) else 0)
    return pressures

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Skipping:", file)
        continue
    right_half = img[:, img.shape[1] // 2:]
    threshold = np.mean(right_half) * 1.5
    pressures = check_pressure(img, threshold)
    data.append([file] + pressures)

columns = ['File'] + list(areas.keys())
df = pd.DataFrame(data, columns=columns)
df.to_excel(output_file, index=False)

print("Done! Check results.xlsx")
