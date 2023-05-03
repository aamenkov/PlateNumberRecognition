import yolov5


class PlateDetector:
    def __init__(self, weights_path):
        self.model = yolov5.load(weights_path)
        self.model.conf = 0.25  # NMS confidence threshold
        self.model.iou = 0.45  # NMS IoU threshold
        self.model.agnostic = False  # NMS class-agnostic
        self.model.multi_label = False  # NMS multiple labels per box
        self.model.max_det = 1000  # maximum number of detections per image

    def detect(self, image_path):
        results = self.model(image_path, augment=True)
        predictions = results.pred[0]
        boxes = predictions[:, :4][0].numpy()  # x1, y1, x2, y2
        scores = predictions[:, 4]
        return {'boxes': boxes, 'scores': scores}
