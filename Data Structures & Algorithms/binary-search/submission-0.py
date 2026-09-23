class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # right pointer will star at 0 and Left
        # will be the lenth of num minus one so the last number in    #the array
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1 
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1