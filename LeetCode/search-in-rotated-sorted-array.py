from collections import deque

class Solution(object):
    def search(self, nums, target):
        nums = deque(nums)
        cnt = 1
        while len(nums)>1 and nums[0]<nums[1]:
            nums.rotate(-1)
            cnt += 1
        nums.rotate(-1)
        
        l,r = 0,len(nums)-1
        print(nums)
        while l<=r:
            print(l,r)
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] == target:
                return (mid+cnt)%len(nums)
            else:
                r = mid-1
                
        return -1
        