# [Cong-Thanh Vu](https://sites.google.com/view/vuthanhcdt/home) packages for Agribot
These packages made by [Thanh](https://sites.google.com/view/vuthanhcdt/home) from [Networked robotic systems laboratory](https://sites.google.com/site/yenchenliuncku). If you use any packages from this repository, please cite this repository and my name.

## Preparing a custom dataset for YOLOv8
- Generate datasets with [Roboflow](https://app.roboflow.com/) and download this to ``data``
- Trainning
### YOLOv8 Instance Segmentation
```
python3 train_seg.py 
```
- Validate data with image name: ``test_predict.jpg``
```
python3 predict_seg.py
```
After that, go to ``runs/segment/predict`` to check the model

### YOLOv8 Object detection

```
python3 train.py 
```
- Validate data with image name: ``test_predict.jpg``
```
python3 predict.py
```
After that, go to ``runs/detec/predict`` to check the model
# Filaria-Detection
