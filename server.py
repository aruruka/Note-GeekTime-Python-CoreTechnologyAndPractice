import os
from shutil import copyfile
import time

"""
我们假设 server 电脑上的所有的文件都在 BASR_DIR 中，为了简化不考虑文件夹结构，网盘的路径在 NET_DIR
"""

BASE_DIR = 'server/'
NET_DIR = 'net/'

def main():
    filenames = os.listdir(BASE_DIR)
    for i, filename in enumerate(filenames):
        print('copying {} into net drive... {}/{}'.format(filename, i + 1, len(filenames)))
        copyfile(BASE_DIR + filename, NET_DIR + filename)
        print('copied {} into net drive, waiting client complete... {}/{}'.format(filename, i + 1, len(filenames)))

        while os.path.exists(NET_DIR + filename):
            time.sleep(3)
    
        print('transferred {} into client. {}/{}'.format(filename, i + 1, len(filenames)))

if __name__ == '__main__':
    main()
