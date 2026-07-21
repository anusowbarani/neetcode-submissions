class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sort = sorted(list(set(nums)))
        max_length = 1
        current_length = 1
        for i in range(len(sort)-1):
            if sort[i] + 1 == sort[i + 1]:
                current_length += 1
            else:
                current_length = 1
            max_length = max(max_length, current_length)
            
        return max_length