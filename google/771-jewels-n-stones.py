class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(list(jewels))
		
        counter = 0
        for sch in stones:
            if sch in jewel_set:
                counter += 1
        return counter        