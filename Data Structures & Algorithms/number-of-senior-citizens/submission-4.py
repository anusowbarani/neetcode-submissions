class Solution:
    def countSeniors(self, details: List[str]) -> int:
        i = 0
        count = 0
        for i in range(len(details)):
            split_no = details[i][11:]
            if int(split_no[:2]) > 60:
                count +=1
        return count
        

            
