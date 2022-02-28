from collections import deque
from heapq import *
from operator import itemgetter
from typing import List


class Solution:

    def getSkyline_queue(self, buildings: List[List[int]]) -> List[List[int]]:
        pos_height = []
        # maxQueue
        heightq: List = []
        answer: List =[]

        # acending from pos, followed by acending from smallest first
        for b in buildings:
            heappush(pos_height, [b[0], -b[2]])
            heappush(pos_height, [b[1], b[2]])
            
        prev = 0
        heappush(heightq, 0)
        
        while pos_height:
            b = heappop(pos_height)
            # if it's left, entering
            if (b[1] < 0):
                heappush(heightq, b[1])
            # if it's right, exiting                
            else:
                # remove the value from height_q
                heightq.remove(-b[1])
                # must retain this order
                heapify(heightq)

            height = -heightq[0]
            if (prev != height):
                answer.append([b[0], height])
                prev = height
            
        return answer

s = Solution()
input = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
s.getSkyline(input)
            
            
                            
                