import os
import cv2
for file in os.listdir("DIV2K_train_HR/DIV2K_train_HR"):
    print(file)
    image = cv2.imread("DIV2K_train_HR/DIV2K_train_HR/" + file, cv2.IMREAD_COLOR)
    image_resized = cv2.resize(image, (256, 256))
    cv2.imwrite("DIV2K_train_HR/div2k_resized/" + file, image_resized)
