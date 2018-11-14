import cv2
import os
import time
import sys

#预先定义的字符集，之后的像素值会映射到这里
charSet = '.,`^[]/\<>-=+ocvedaslzxBGHWNM*%$'

cap = cv2.VideoCapture("ba.mp4")

if(cap.isOpened()):
  #fps = cap.get(cv2.CAP_PROP_FPS)
  #width = (int)(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = (int)(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  ret,frame = cap.read()
  while ret:
    src = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #scale = 1/20
    #最终单个字符画的高度为命令行显示的最多行数(50)，这样连续输出可以保证基本流畅
    scale = 50/height#命令行高度
    #缩放图像，用一个字符代替1/scale * 1/scale个像素点
    dst = cv2.resize(src,None,fx = scale,fy = scale,interpolation = cv2.INTER_CUBIC)
    h = dst.shape[0]
    w = dst.shape[1]
    M = []
    for row in range(h):
        line = ""
        for col in range(w):
            pix = dst[row,col]
	    #将像素值映射到字符集，后接' '规范格式(默认输出有行间距没有字间距)
            i = (int)(pix/256*len(charSet))
            line +=charSet[i] + " "
            #print(charSet[i],end = ' ')
        #print(line)
        M.append(line)
    #简单的时间控制
    time.sleep(0.01)
    #可以通过清屏避免缩放到命令行高度，但会有闪屏
    #os.system('cls')
    #可以直接将单个字符画存储后再读取，也不用考虑固定高度的限制
    #sys.stdout = open("out.txt",'w')#重定向print
    #按序输出字符画形成动画
    for i in M:
        print(i)
    #print("-------")
    #cv2.waitKey(5)
    ret,frame = cap.read()
  cap.release()
'''
src = cv2.imread("1.png",0)
cv2.imshow("src",src)

scale = 1/10
dst = cv2.resize(src,None,fx = scale,fy = scale,interpolation = cv2.INTER_CUBIC)
h = dst.shape[0]
w = dst.shape[1]
for row in range(h):
    line = ""
    for col in range(w):
        pix = dst[row,col]
        i = (int)(pix/256*len(charSet))
        line +=charSet[i] + " "
        #print(charSet[i],end = ' ')
    print(line)
#cv2.imshow("src",dst)
#print(src.shape)
#print(dst.shape)
'''
cv2.waitKey(10000)

