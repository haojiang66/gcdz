import cv2
import json
import numpy as np
dirpath="proc1.png"
img  = cv2.imread(dirpath)

w=len(img)
h=len(img[0])
flag=-1
len=0
for i in range(w):
    if flag<0:
        if np.min(img[i])<255:
            flag=i
            len=np.sum(img[i],dtype=np.int32)
    else:
        if(np.abs(np.sum(img[i],dtype=np.int32)-len)>5000):
            for k in range(flag,i):
                for j in range(h):
                    for l in range(3):
                        img[k][j][l]=255
            break
flag=-1
for i in reversed(range(w)):
    if flag<0:
        if np.min(img[i])<255:
            flag=i
            len=np.sum(img[i],dtype=np.int32)
            print(i)
            print("!")
    else:
        if(np.abs(np.sum(img[i],dtype=np.int32)-len)>5000):
            print(i)
            for k in range(i+1,flag+1):
                for j in range(h):
                    for l in range(3):
                        img[k][j][l]=255
            break
flag=-1
for j in range(h):
    if flag<0:
        if np.min(img[:,j])<255:
            flag=j
            len=np.sum(img[:,j],dtype=np.int32)
    else:
        if(np.abs(np.sum(img[:,j],dtype=np.int32)-len)>5000):
            for i in range(w):
                for k in range(flag,j):
                    for l in range(3):
                        img[i][k][l]=255
            break
flag=-1
for j in reversed(range(h)):
    if flag<0:
        if np.min(img[:,j])<255:
            flag=j
            len=np.sum(img[:,j],dtype=np.int32)
    else:
        if(np.abs(np.sum(img[:,j],dtype=np.int32)-len)>5000):
            for i in range(w):
                for k in range(j+1,flag+1):
                    for l in range(3):
                        img[i][k][l]=255
            break
cv2.imwrite("proc2.png",img)