from imutils import contours
import numpy as np
import argparse
import cv2
import myutils


def cv_show(name,img):
	cv2.imshow(name, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
##############################################################################################	
dirpath=r'C:\Users\haojiang66\Desktop\gcdz\image3.png'
img   = cv2.imread(dirpath)
ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,refCnts,-1,(0,0,255),3)
refCnts = contours.sort_contours(refCnts, method="left-to-right")[0] #排序，从左到右，从上到下
digits = {}
for (i, c) in enumerate(refCnts):
	(x, y, w, h) = cv2.boundingRect(c)
	roi = ref[y:y + h, x:x + w]
	roi = cv2.resize(roi, (57, 88))
	digits[i] = roi
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))


import cv2
import json
import numpy as np
dirpath="proc2.png"
img  = cv2.imread(dirpath)#读取数据
class Point:
    def __init__(self,x:np.int32=-1,y:np.int32=-1,Black=False):
        if Black:
            self.lord=self
            if x>-1:
                self.w1=x
                self.w2=x
                self.h1=y
                self.h2=y
            self.num=np.int32(1)
            self.x=x
            self.y=y
            self.son=[]
            self.type=-1
            self.isnum=True
        else:
            self.lord=None
    def GetLord(self):
        if self.lord==self or self.lord==None:
            return self.lord
        res=self.lord.GetLord()
        self.lord=res
        return res
    def Merge(self,b):
        al=self.GetLord()
        bl=b.GetLord()
        if al!=bl:
            al.lord=bl
            bl.num=bl.num+al.num
            bl.w1=min(al.w1,bl.w1)
            bl.w2=max(al.w2,bl.w2)
            bl.h1=min(al.h1,bl.h1)
            bl.h2=max(al.h2,bl.h2)
w=len(img)
h=len(img[0])
all_black=[]

for i in range(w):
    for j in range(h):
        if all(img[i][j]==[0,0,0]):
            all_black.append(Point(i,j,Black=True))
            for id in reversed(range(len(all_black))):
                if all_black[id].x<i-1:
                    break
                if all_black[id].y>=j-1 and all_black[id].y<=j+1:
                    all_black[-1].Merge(all_black[id])
    if i%100==0:
        print(f"{i} over")
cnt=0

for p in all_black:
    if p==p.lord:
        # print("!")
        cnt=cnt+1
        img[p.x][p.y][0]=(cnt%5)*50
        img[p.x][p.y][1]=(cnt%7)*36
        img[p.x][p.y][2]=(cnt%9)*28

for p in all_black:
    if p!=p.lord:
        # print(p)
        # print(p.lord==None)
        p.GetLord()
        img[p.x][p.y][0]=img[p.lord.x][p.lord.y][0]
        img[p.x][p.y][1]=img[p.lord.x][p.lord.y][1]
        img[p.x][p.y][2]=img[p.lord.x][p.lord.y][2]
cv2.imwrite("proc3.png",img)

pass

dirpath=r'C:\Users\haojiang66\Desktop\gcdz\proc2.png'
img   = cv2.imread(dirpath)
all_lord=[]

for p in all_black:
    if(p.lord not in all_lord):
        all_lord.append(p.lord)

for a in all_lord:
    for p in all_black:
        if(p.lord==a):
            a.son.append(p)

def judge (p):
    
    # 找到当前数值的轮廓，resize成合适的的大小
    roi = img[p.w1:p.w2,p.h1:p.h2,0]
    if len(roi):
        if len(roi[0]):
            roi = cv2.resize(roi, (55,87))
            #roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            
            # 计算匹配得分
            scores = []
                    # 在模板中计算每一个得分
            for (digit, digitROI) in digits.items():
                # 模板匹配
                result = cv2.matchTemplate(roi, digitROI,cv2.TM_CCOEFF)
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)
                # 得到最合适的数字
            print(f"{max(scores)} {max(scores)-min(scores)}")
            #cv_show('roi',roi)
            if (max(scores)<6000000):
                p.isnum==False
                for s in p.son:
                    img[s.x][s.y]=[255,255,255]
            return 


for a in all_lord:
    judge(a)

for a in all_lord:
    if(a.isnum==False):
        for s in a.son:
            img[s.x][s.y]=[255,255,255]

cv2.imwrite("proc4.png",img)







