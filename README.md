# LED bulb light colors white red green blue dataset for YOLO

```
parent
├── yolov5
├── darknet
└── datasets
    └── wrgb  ← git clone here
```

## works with pytorch <https://github.com/ultralytics/yolov5>

    cd yolov5

To train:

    python train.py --epochs 55 --data ../datasets/wrgb/obj.yaml --cfg ../datasets/wrgb/yolov5s.yaml --imgsz 416 --workers 4 --project runs/yolov5s_wrgb

To detect:

    python detect.py --weights runs/yolov5s_wrgb/exp/weights/best.pt --img-size 416 --source SOME.jpg

To mobile optimized model exported to `yolov5s.ptl`:

    python export.py --weights runs/yolov5s_wrgb/exp/weights/best.pt --include torchscript
    cd ../datasets/wrgb
    cp ../../yolov5/runs/yolov5s_wrgb/exp/weights/best.torchscript ./
    python pt2ptl.py

## works with darknet <https://github.com/AlexeyAB/darknet>

    cd datasets/wrgb

To train:

    C:\proj\yolo\darknet\darknet detector train obj.data yolov2-tiny.cfg

To detect:

    C:\proj\yolo\darknet\darknet detector test obj.data yolov2-tiny.cfg backup/yolov2-tiny_last.weights SOME.jpg
