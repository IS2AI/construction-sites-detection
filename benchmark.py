from ultralytics.utils.benchmarks import benchmark
import os

os.environ["CUDA_VISIBLE_DEVICES"] = '4,5,6,7'

# Write the path to the trained model and to the .yaml file where in "val" line you should write the path to the folder with test images
benchmark(model='/raid/abylay_turekhassim/runs/segment/train26/weights/best.pt', data='/raid/abylay_turekhassim/v8/test.yaml', imgsz=600, half=False, device=[0,1,2,3])