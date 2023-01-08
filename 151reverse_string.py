# !/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        m = []
        for n in l[::-1]:
            if n != '':
                m.append(n)
        # print(m)
        return ' '.join(m)

if __name__ =='__main__':
    a = Solution().reverseWords('a good   example')
    print(a)
