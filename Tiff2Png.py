import os

# 輸入 TIF 檔案目錄
tif_dir = "TIFF"

# 輸出 PNG 檔案目錄
png_dir = "PNG"

# 遍歷 TIF 檔案目錄
for filename in os.listdir(tif_dir):
    # 獲取 TIF 檔案路徑
    tif_path = os.path.join(tif_dir, filename)

    # 獲取 PNG 檔案路徑
    png_path = os.path.join(png_dir, filename[:-4] + ".png")

    # 使用 Pillow 將 TIF 檔案轉換為 PNG 格式
    from PIL import Image
    img = Image.open(tif_path)
    img.save(png_path)

print("Finish!")
