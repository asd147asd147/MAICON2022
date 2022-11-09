import os
import glob
import cv2
import numpy as np
from tqdm import tqdm

pred_dir = '20221109_023523_20221109_121507'
prj_dir = os.path.dirname('../baseline/results/')
train_dirs = os.path.join(prj_dir, 'pred', pred_dir)
train_img_paths = glob.glob(os.path.join(train_dirs, 'mask', '*.png'))
os.mkdir(os.path.join('./results/',pred_dir))

for path in tqdm(train_img_paths):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    img_R = np.zeros((img.shape[0], img.shape[1]))
    img_G = np.zeros((img.shape[0], img.shape[1]))
    img_B = np.zeros((img.shape[0], img.shape[1]))
    img_R[np.where(img==2)] = 255
    img_G[np.where(img==1)] = 255
    img_B[np.where(img==3)] = 255
    img_color = np.stack([img_G, img_B, img_R], axis=2)
    cv2.imwrite(os.path.join('./results/',pred_dir,os.path.basename(path)), img_color)