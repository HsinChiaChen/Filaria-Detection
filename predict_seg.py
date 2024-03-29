from ultralytics import YOLO
import os
import cv2
from PIL import Image

dirPath = os.path.dirname(os.path.realpath(__file__))
# print(dirPath)

# Load a model
model = YOLO(dirPath + '/weight/Filaria.pt')  # load a custom trained
# 輸入檔案目錄
image_dir = dirPath + '/Image/'
print("Read from :", image_dir)

# 輸出檔案目錄
png_dir = dirPath + "/Result/"
print("Save to :", png_dir)

# 遍歷 Image 檔案目錄
for filename in os.listdir(image_dir):
    # 獲取檔案路徑
    read_path = os.path.join(image_dir, filename)

    # 獲取檔案路徑
    png_path = os.path.join(png_dir, filename[:-4] + ".png")
    
    # img = Image.open(tif_path)
    img = cv2.imread(read_path)
    # 進行目標檢測
    result = model.predict(img)

    # # 計算檢測到的數量
    count = len(result[0].boxes)
    print(len(result[0].boxes))

    result_plot = result[0].plot(labels=False, conf=False)

    # # 在圖片上顯示數量
    cv2.putText(result_plot, str(count), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # # # 顯示圖片
    # cv2.imshow(result)
    # cv2.waitKey(0)
    cv2.imwrite(png_path, result_plot)