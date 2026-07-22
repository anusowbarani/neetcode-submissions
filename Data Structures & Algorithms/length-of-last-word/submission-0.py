class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        spaces_remove = s.strip()
        words = spaces_remove.split(" ")
        for i in range(len(words) + 1):
            length = len(words[i-1])
        return length