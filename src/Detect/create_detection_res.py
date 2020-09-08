
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

import numpy as np
from os import listdir
import os.path as osp
import os
import cv2 as cv
import json
import xml.etree.ElementTree as ET
import random
import argparse


from detectron2.engine import DefaultTrainer

parser = argparse.ArgumentParser()
parser.add_argument('--input_path',default='')
parser.add_argument('--output_path',default='')
parser.add_argument('--model_path',default='model_weights/Detect/Bright/output/model_final.pth')
args = parser.parse_args()

cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
cfg.DATALOADER.NUM_WORKERS = 2
cfg.MODEL.WEIGHTS = args.model_path 
# model_weights/Detect/Dark/output/model_final.pth  3,5,8,11,13,15,17,19
# model_weights/Detect/Bright/output/model_final.pth '1','2','4','6','7','9','10','12','14','16','18','21','23','24'
# model_weights/Detect/black_white/output/model_final.pth 20,22,25
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.00025 
cfg.SOLVER.MAX_ITER = 110000                                  #set cao hơn so với pretrain, pretrain 1000 thì ở đây 1001 trở lên
cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128  
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 14

cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.65   # set a custom testing threshold
predictor = DefaultPredictor(cfg)

def output_detection(input_path,output_path):
	out = open(output_path,'w')
	for file in listdir(input_path):
		filename = file[6:-4]
		file = osp.join(input_path, file)
		image = cv.imread(file, cv.IMREAD_GRAYSCALE)
		cv.imwrite('tmp.png',image)
		image = cv.imread('tmp.png')
		predictions = predictor(image)["instances"]
		boxes = predictions.pred_boxes if predictions.has("pred_boxes") else None
		classes = predictions.pred_classes if predictions.has("pred_classes") else None
		scores = predictions.scores if predictions.has("scores") else None
		if boxes != None:
			for bbox, label, score in zip(boxes, classes, scores):
				string = ' '.join([filename,'-1',str(float(bbox[0])),str(float(bbox[1])),\
					str(float(bbox[2])-float(bbox[0])),str(float(bbox[3])-float(bbox[1])),str(float(score)),str(float(label)),'-1','-1'])
				out.write(string)
				out.write('\n')
	out.close()

output_detection(args.input_path,args.output_path)
    	