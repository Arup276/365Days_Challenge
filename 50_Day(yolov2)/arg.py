import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--img',type=str,help='path of the image')
arg = parser.parse_args()
imgcv = cv2.imread(arg.img)
cv2.imshow('img',imgcv)
cv2.waitKey(0)
