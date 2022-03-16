import math
import numpy as np
import os
import sys
import spectral as sp
from skimage import io
import numpy as np
import warnings
warnings.filterwarnings("ignore")

c1 = 14390
c2 = 119100000
r2 = 11.88

with open('C:/PcModWin5/bin/channels.out', 'r') as f1:
    # 按行读
    f2 = f1.readlines()
    # 存成列表形式
    f3 = list(f2)
    # 第6行
    f4 = str(f3[5])
    f5 = f4.split("  ")
    rad = 10000 * float(f5[5]) / 0.9641
    #print(rad)
    x = math.log(1 + (c2 / (rad * (r2 * r2 * r2 * r2 * r2))))
    lw = c1 / (r2 * x)
    print(lw)

