import os
import sys
input_path = sys.argv[1].rstrip(os.sep)
#datasets/train
out_path = sys.argv[2]#train.txt
filenames = os.listdir(input_path)

with open(out_path,'w') as f:
    for files in filenames:
        filepath = os.sep.join([input_path,files])
        label = files[:files.rfind('.')].split('_')[1]
        line = '{} {}\n'.format(filepath,label)
        f.write(line)
