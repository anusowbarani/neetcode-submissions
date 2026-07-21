class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^\w]', '', s).lower() 
        reversed_s = cleaned_s[::-1]
        if cleaned_s == reversed_s:
            return True
        else:
            return False
   



        