# LED bulb light colors white red green blue dataset for yolo

```
parent
├── darknet
└── datasets
    └── wrgb  ← git clone here
```

## darknet <https://github.com/AlexeyAB/darknet>

    cd datasets/wrgb

To train:

    C:\proj\yolo\darknet\darknet detector train obj.data yolov2-tiny.cfg

To detect:

    C:\proj\yolo\darknet\darknet detector test obj.data yolov2-tiny.cfg backup/yolov2-tiny_last.weights SOME.jpg
