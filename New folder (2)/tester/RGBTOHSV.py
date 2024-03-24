import cv2
import numpy as np

# Define the RGB values
target_color_start_rgb = np.uint8(242, 223, 41)
target_color_end_rgb = np.uint8(250, 192, 39)

# Convert RGB to HSV
target_color_start_hsv = cv2.cvtColor(target_color_start_rgb, cv2.COLOR_RGB2HSV)
target_color_end_hsv = cv2.cvtColor(target_color_end_rgb, cv2.COLOR_RGB2HSV)

# Print the HSV values
print("Target color start (HSV):", target_color_start_hsv)
print("Target color end (HSV):", target_color_end_hsv)