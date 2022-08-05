class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        l, r = 1, num // 2
        
        while (l <= r):
            m = (l + r) // 2
            
            itr = m*m
            
            if(itr == num):
                return True
            elif(itr > num):
                r = m - 1
            else:
                l = m + 1
                
        return False