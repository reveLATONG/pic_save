#coding=utf-8
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup as btfs
import os

num = 200
file = 'E:\worm\mini.txt'

with open(file, 'r') as f:
    content = [line.rstrip('\n') for line in f]

def save_pic(i, path):
    if(i==0):
        url = base+str(i)+".jpg"
    elif(i<10):
        url = base+"00"+str(i)+".jpg"
    elif(i<100):
        url = base+"0"+str(i)+".jpg"
    else:
        url = base+str(i)+".jpg"
    #dir = "E:\wormpic"
    #work_path = os.path.join(dir, '%d.jpg' % (i))
    work_path = os.path.join(path, '%d.jpg' % (i))
    print(url)
    urlretrieve(url, work_path)
i = 0
na = 0

for base in content:
    basedir = "E:\wormpic"
    newdir = os.path.join(basedir, '%d' % (na))
    na = na + 1

    os.mkdir(newdir)
    for i in range(num+2):
        try:
            save_pic(i, newdir)
        except:
            break




