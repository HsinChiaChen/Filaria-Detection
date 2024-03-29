# Hsin-Chia Chen packages for Filaria Detect
These packages are produced by Hsin-Chia Chen of the [Network Robotic Systems Laboratory](https://sites.google.com/site/yenchenliuncku).
## File conversion
Convert files with extension '.tiff' in the "TIFF" folder to '.png'
````
python3 train_seg.py
````
After that, go into the "PNG" folder and check the files

## Use this data set for detection
````
python3 predict_seg.py
````
After that, go to the “Result” folder to check the results
The detected range will be surrounded by a red frame, and details will be filled in red.
The total number detected will be displayed in the upper left corner of the picture.

## Prepare custom dataset for YOLOv8
- Use [Roboflow](https://app.roboflow.com/) to generate a data set and download it to "data"

- Trainning

### YOLOv8 instance segmentation
````
python3 train_seg.py
````
After that, enter "runs/segment/train" to check the training results
