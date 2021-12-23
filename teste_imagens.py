import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

H, M, S = time.localtime(time.time()).tm_hour, time.localtime(time.time()).tm_min, time.localtime(time.time()).tm_sec

print(f'H{H} M{M} S{S}')

