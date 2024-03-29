from ultralytics import YOLO
import os
import cv2
from PIL import Image

dirPath = os.path.dirname(os.path.realpath(__file__))
# print(dirPath)

# Load a model
model = YOLO(dirPath + '/weight/Filaria.pt')  # load a custom trained
# Enter file directory
image_dir = dirPath + '/PNG/'
print("Read from :", image_dir)

# Output file directory
png_dir = dirPath + "/Result/"
print("Save to :", png_dir)

# Traverse PNG archive directories
for filename in os.listdir(image_dir):
    # Get input file path
    read_path = os.path.join(image_dir, filename)

    # Get storage file path
    png_path = os.path.join(png_dir, filename[:-4] + ".png")

    img = cv2.imread(read_path)
    result = model.predict(img)

    # Count the number of detected
    count = len(result[0].boxes)
    # print(len(result[0].boxes))

    result_plot = result[0].plot(labels=False, conf=False)

    # Show quantity on picture
    cv2.putText(result_plot, str(count), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imwrite(png_path, result_plot)
print("Finish!")
