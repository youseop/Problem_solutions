import heapq as hq

class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        candidate = [(matrix[0][0],0,0)]
        matrix[0][0] = '*'
        cnt = 0
        while candidate:
            val,x,y = hq.heappop(candidate)
            cnt += 1
            if cnt == k:
                return val
            for _x,_y in [(x+1,y),(x,y+1)]:
                if 0<=_x<n and 0<=_y<n and matrix[_x][_y]!='*':
                    hq.heappush(candidate,(matrix[_x][_y],_x,_y))
                    matrix[_x][_y] = '*'
            
        
        