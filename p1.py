import cv2
import json
dirpath="in.png"
img  = cv2.imread(dirpath)

#进行黑度设置
w=len(img)
h=len(img[0])
for i in range(w):
    if i%100==0:
        print(f"{i}.")
    for j in range(h):
        
        if img[i][j][0]>190:
            img[i][j]=[255,255,255]
        else:
            img[i][j]=[0,0,0]
cv2.imwrite("proc1.png",img)
print("img_cv:",type(img))


# 基于机器学习和创新性算法的边坡分析和相关图例模型构建方法