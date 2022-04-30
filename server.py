import argparse
import io
from PIL import Image

import torch
from flask import Flask, request

app = Flask(__name__)


@app.route('/predict', methods=["POST"])
def predict():
    if not request.method == "POST":
        return

    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()

        img = Image.open(io.BytesIO(image_bytes))

        results = model(img, size=640)
        data = results.pandas().xyxy[0].to_json(orient="records")
        return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask api exposing yolov5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load(
         "ultralytics/yolov5", "custom", path="last.pt", force_reload=True)
    model.eval()
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat
