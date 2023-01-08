# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/20 16:38
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : topk_largest.py
# @Software: PyCharm
import heapq

class TopK:
    def findKthLargest(nums, k:int)->int:
        n = len(nums)
        hp = nums[:k]
        heapq.heapify(hp)
        for i in range(k,n):
            if hp[0] < nums[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, nums[i])
        return hp[0]

if __name__ =='__main__':
    a=    TopK.findKthLargest([3,43,345,345,34,257,72], 3)
    print(a)