Results:

Image

![image2](https://github.com/KansaraT/Number-Plate-Detection-and-Recognition/assets/91043060/4e1af46f-8327-42a2-9bd8-cda83fbf6445)

Video

https://github.com/KansaraT/Number-Plate-Detection-and-Recognition/assets/91043060/e642c08f-0099-45dd-81c3-ec11fb84922b


## Steps to run Code

- Goto the cloned folder.
```
cd Automatic_Number_Plate_Detection_Recognition_YOLOv8
```
- Install the dependecies
```
pip install -e '.[dev]'

```

- Setting the Directory.
```
cd ultralytics/yolo/v8/detect
```


- Downloading a Weights from the Google Drive
```
gdown "https://drive.google.com/uc?id=1dIyJooVaowaNUj0R1Q-HUnu-utiGsEj8&confirm=t"
```
- Downloading a Sample Video from the Google Drive
```
gdown "https://drive.google.com/uc?id=1P-oVR0J35Dw40lzw47sE19oADSW-tyb1&confirm=t"

```
- Run the code with mentioned command below (For Licence Plate Detection).
```
python predict.py model='best.pt' source='demo.mp4'
```

- For Licence Plate Detection and Recognition

- Download the Updated predict.py file from the drive
```
gdown "https://drive.google.com/uc?id=1S6GkQcDq8W0ThaUeZ708UegHIRiVWzTo&confirm=t"
```
- Run the code with mentioned command below (For Licence Plate Detection and Recognition).
```
python predict.py model='best.pt' source='demo.mp4'
```



