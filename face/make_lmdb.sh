#!/bin/sh
path=`~/caffe/build/tools/convert_imageset ./ train.txt train_lmdb --gray --shuffle`
path=`~/caffe/build/tools/convert_imageset ./ test.txt test_lmdb --gray --shuffle`
path=`~/caffe/build/tools/convert_imageset ./ val.txt val_lmdb --gray --shuffle`
echo $path
