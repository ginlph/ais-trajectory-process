#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: lph time:2021/9/27

import numpy as np
from math import *


class DouglasPeucker():
    """
        Ramer–Douglas–Peucker algorithm
        reference: <https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm>
    """

    def __init__(self):
        pass

    def douglasPeucker(self, pointList, epsilon):
        """
            Douglas-Peucker

        """
        dmax = 0
        index = 0
        end = len(pointList)
        for i in range(1, end-1):
            d = self.pointLineDistance(pointList[i], pointList[0], pointList[ -1])
            if d > dmax:
                dmax = d
                index = i

        if dmax > epsilon:
            recursive1 = self.douglasPeucker(pointList[: index + 1], epsilon)
            recursive2 = self.douglasPeucker(pointList[index: ], epsilon)
            return np.vstack((recursive1[:-1], recursive2))
        else:
            return np.stack((pointList[0], pointList[-1]))


    def pointLineDistance(self, point, linePoint1, linePoint2):
        """
            点到直线的距离
        """
        x0, y0 = point[0], point[1]
        x1, y1 = linePoint1[0], linePoint1[1]
        x2, y2 = linePoint2[0], linePoint2[1]
        numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
        denominator = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
        distance = numerator / denominator
        return distance