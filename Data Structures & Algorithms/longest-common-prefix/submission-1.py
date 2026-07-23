class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result