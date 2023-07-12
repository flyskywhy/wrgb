# ref to https://github.com/raedle/YOLOExample

import torch
from torch.utils.mobile_optimizer import optimize_for_mobile

## best.torchscript comes from e.g.
#     cd yolov5
#     python export.py --weights runs/yolov5s_wrgb/exp/weights/best.pt --include torchscript
#     cd ../datasets/wrgb
#     cp ../../yolov5/runs/yolov5s_wrgb/exp/weights/best.torchscript ./
torchscript_model = "best.torchscript"
export_model_name = "yolov5s.ptl"

model = torch.jit.load(torchscript_model)
optimized_model = optimize_for_mobile(model)
optimized_model._save_for_lite_interpreter(export_model_name)

print(f"mobile optimized model exported to {export_model_name}")
