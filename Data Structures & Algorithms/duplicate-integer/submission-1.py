class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        searchset= set()
        for num in nums:
            if num in searchset:
                return True
            searchset.add(num)
        return False
    
            

        