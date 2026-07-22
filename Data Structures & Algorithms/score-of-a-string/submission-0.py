class Solution:
    def scoreOfString(self, s: str) -> int:
        new = list(s)
        value = 0
        for i in range(len(new) -1 ):
             value += abs(ord(new[i+1]) - ord(new[i]))

        return value

            
            
