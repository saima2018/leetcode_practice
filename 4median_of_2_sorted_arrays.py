# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/7 10:47
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 4median_of_2_sorted_arrays.py
# @Software: PyCharm
# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/#:~:text=Given%20two%20arrays%20are%20sorted.%20So%20they%20can,elements%20at%20index%20%28m%2Bn%29%2F2%20and%20%28%28m%2Bn%29%2F2%20%E2%80%93%201%29.
def getMedian(ar1, ar2, n, m):
    i = 0 # current index of input array ar1
    j = 0 # .. ar2
    m1, m2 = -1, -1

    if ((m+n) % 2 == 1): # case of odd total length
        for count in range(((m+n)//2)+1):
            if (i!=n and j!=m):
                if ar1[i]>ar2[j]:
                    m1 = ar2[j]
                    j += 1
                else:
                    m1 = ar1[i]
                    i += 1
            elif i<n:
                m1 = ar1[i]
                i+=1
            elif j<m:
                m1 = ar2[j]
                j+=1
        return m1
    else:
        for count in range(((m+n)//2)+1):
            m2 = m1
            if (i!=n and j!=m):
                if ar1[i]>ar2[j]:
                    m1 = ar2[j]
                    j+=1
                else:
                    m1 = ar1[i]
                    i+=1
            elif i<n:
                m1 = ar1[i]
                i+=1
            else:
                m1 = ar2[j]
                j+=1
        return (m1+m2)/2

ar1 = [23]
ar2 = [3,4,5,234,32]

n1 =len(ar1)
n2 = len(ar2)

# print(getMedian(ar1,ar2,n1,n2))
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0  # current index of input array nums1
        j = 0  # .. nums2
        m1, m2 = -1, -1

        if ((m + n) % 2 == 1):  # case of odd total length
            for count in range(((m + n) // 2) + 1):
                if (i != n and j != m):
                    if nums1[i] > nums2[j]:
                        m1 = nums2[j]
                        j += 1
                    else:
                        m1 = nums1[i]
                        i += 1
                elif i < n:
                    m1 = nums1[i]
                    i += 1
                elif j < m:
                    m1 = nums2[j]
                    j += 1
            return m1
        else:
            for count in range(((m + n) // 2) + 1):
                m2 = m1
                if (i != n and j != m):
                    if nums1[i] > nums2[j]:
                        m1 = nums2[j]
                        j += 1
                    else:
                        m1 = nums1[i]
                        i += 1
                elif i < n:
                    m1 = nums1[i]
                    i += 1
                else:
                    m1 = nums2[j]
                    j += 1
            return (m1 + m2) / 2