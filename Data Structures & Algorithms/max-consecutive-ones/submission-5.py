class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        current_length = 0
        max_length = 0
        for i in nums:
            if i == 1:
                current_length +=1
                max_length = max(max_length,current_length)
            else:
                current_length = 0
        return max_length