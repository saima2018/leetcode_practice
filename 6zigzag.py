# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/1/24 15:08
# @Author : masai
# @Email : sai.ma@spacexwalk.com
# @File : 6zigzag.py
# @Software: PyCharm

# https://learncodingfast.com/python-programming-challenge-9-zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [""] * numRows
        rowNumber = 0
        direction = 1

        for i in range(len(s)):
            result[rowNumber] = result[rowNumber] + s[i]

            # sink down, till touches the bottom row, and switch direction
            if rowNumber < numRows-1 and direction == 1:
                rowNumber += 1

            # float up, till reaches the first row, and switch direction
            elif rowNumber > 0 and direction == -1:
                rowNumber -= 1

            # touches top or bottom, switch direction, and adjust rowNumber accordingly
            else:
                direction *= -1
                rowNumber += direction
        return ''.join(result)

    def self_convert(self, s:str, numRows:int)->str:
        result = [""]*numRows
        current_row = 0
        direction = 1
        for i in range(len(s)):
            result[current_row] = result[current_row]+s[i]
            if current_row<numRows-1 and direction == 1:
                current_row +=1
            elif current_row>0 and direction == -1:
                current_row -=1
            else:
                direction *=-1
                current_row += direction
        return ''.join(result)

if __name__ == '__main__':
    a = Solution()
    print(a.self_convert('PAYPALISHIRING',3))

