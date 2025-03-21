from ultralytics import YOLO

# Carga el modelo preentrenado de YoLo11n
model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

# Ejecuta la detección de objetos en imágenes
results = model(["images/image_1.jpg"])

# Procesa los resultados
for result in results:
    boxes = result.boxes  # boxes de los objetos detectados
    masks = result.masks  # Máscaras de segmentación de los objetos detectados
    keypoints = result.keypoints  # Puntos clave de los objetos detectados
    probs = result.probs  # Probabilidades de los objetos detectados
    obb = result.obb  # Bounding boxes orientadas de los objetos detectados
    result.show()  # muestra los resultados
    result.save(filename="result" + str(0) + ".jpg")

print(result)