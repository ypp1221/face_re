import os
import sys
filepath = sys.argv[1]
all_path = os.listdir(filepath)

for path in all_path:
    all_filepath = os.sep.join([filepath,path])
    print(all_filepath)
    print(path)
    echo = 'python make_txt.py {} {}.txt'.format(all_filepath,path)
    print(echo)
    os.system(echo)
