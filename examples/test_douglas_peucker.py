#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2021/10/4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from aisTrajectoryProcess.douglas_peucker import DouglasPeucker

# 原始轨迹数据
path = "../examples/data/simple_data.txt"
df = pd.read_csv(path, delimiter=",", names=["x", "y"])
pointList = np.column_stack([df.x, df.y])

dp = DouglasPeucker()
epsilon = 8
resultArray = dp.douglasPeucker(pointList, epsilon)

compressedRatio = (1-len(resultArray) / len(pointList)) * 100
print("The Compressed ratio is: %.3f%%" % compressedRatio)

# draw raw data, draw resultArray
fig, ax = plt.subplots(figsize=(14, 8))
ax.scatter(df.x, df.y, marker="o", edgecolor="black", facecolor="white", s=80, label="raw data scatter")
ax.plot(df.x, df.y, color="green", label="raw data curve")
ax.set_xlabel("x", fontsize=16)
ax.set_ylabel("y", fontsize=16)

ax.scatter(resultArray[:, 0], resultArray[:, 1], marker="o", edgecolor="black", facecolor="red", s=100, label="compresseed data scatter")
ax.plot(resultArray[:, 0], resultArray[:, 1], color="red", label="compressed data curve")
ax.legend()
plt.savefig("./data/test-result/simple_data.png")
plt.show()
