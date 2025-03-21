from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # load an official model
model = YOLO("/home/rojaldo/cursos/ai/samples/runs/detect/train/weights/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category

# print metrics
# print(metrics)
print(metrics.box.map50)
print(metrics.box.map75)
print(metrics.box.map)
