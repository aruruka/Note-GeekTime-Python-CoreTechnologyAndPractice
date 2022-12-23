import os
from shutil import copyfile
import time

"""
我们假设 client 电脑上要删除的文件夹在 BASR_DIR ，网盘的路径在 NET_DIR
"""

BASE_DIR = 'client/'
NET_DIR = 'net/'

def main():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print('downloading {} into local disk...'.format(filename))
            copyfile(NET_DIR + filename, BASE_DIR + filename)
            os.remove(NET_DIR + filename) # 我们需要删除这个文件，网盘会替我们同步这个操作，从而 server 知晓已完成
            print('doanloaded {} into local disk.'.format(filename))
        time.sleep(3)

if __name__ == "__main__":
    main()