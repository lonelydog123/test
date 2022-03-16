import math
import numpy as np
import os
import sys
import spectral as sp
from skimage import io
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#输入光谱响应函数
iff = input("please input Instrument Filter File Name(.flt): ")
#输入预设表面温度
tpt = input("please input used surface temperature(0.1): ")
#输入表观反射率
albedo = input("please input surface albedo(0.01): ")
#输入观测天顶角
sza = input("please input zenith angle(0.01): ")
#输入起始频率
ifq = input("please input initial frequency(0.1): ")
ffq = input("please input final frequency(0.1): ")

with open('C:/PcModWin5/bin/tape5', 'r') as f1:
    # 按行读tape5
    f2 = f1.readlines()
    # print(f2)
    # 存成列表形式
    f3 = list(f2)
    #第一行
    f3[0] = 'T F 2    2    1    0    0    0    0    0    0    0    0    0    0 ' + str(tpt) + '00' + str(albedo)+'000\n'
    #第三行
    f3[2] = 'DATA/'+str(iff)+'\n'
    #第五行
    f6 = str(f3[4])
    f7 = f6.split("  ")
    f7[1] = '0.000000' + str(sza) + '0000'
    a = '  '
    new_f7 = a.join(f7)
    f3[4] = new_f7
    #第六行
    f8 = str(f3[5])
    f9 = f8.split(" ")
    f9[1] = str(ifq) + '0000' + str(ffq) + '0000'
    a = ' '
    new_f9 = a.join(f9)
    f3[5] = new_f9
  
with open('H:/testpy/tape5', 'w', encoding='utf-8') as fn:
    for line in f3:
        fn.write(line)

os.system("C:/PcModWin5/bin/Mod5.2.0.0.exe")
