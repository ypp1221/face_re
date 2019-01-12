import sys
import numpy as np
import cv2
sys.path.append('~/caffe/python')
import caffe
MEAN = 129.47
SCALE = 0.00390625

imglist = sys.argv[1]

caffe.set_mode_gpu()
caffe.set_device(0)
net = caffe.Net('face_test.prototxt', 'face.caffemodel',caffe.TEST)
net.blobs['data'].reshape(1,1,48,48)
with open(imglist,'r') as f:
    line = f.readline()
    while line:
        imgpath = line.split()[0]
        line = f.readline()
        
        image = cv2.imread(imgpath,cv2.IMREAD_GRAYSCALE)
        image = image.astype(np.float) - MEAN
        
        image *= SCALE
        net.blobs['data'].data[...] = image
        output = net.forward()
        pred_label = np.argmax(output['prob'][0])
        print('predicted image for {} is {}'.format(imgpath, pred_label))

print('end')
