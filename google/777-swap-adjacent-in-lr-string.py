from re import S, search


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        sln = len(start)

        idx = 0
        while idx < sln:
            sch = start[idx]
            ech = end[idx]

            if sch == ech:
                idx += 1
                continue

            if idx+1 == sln or sch == "L":
                return False

            # Assume sch is "R" 
            # Need to search for "X" in start array such that end array has "R" at that index
            search_char, oppo_char, block_char = ("X", "R", "L") if sch == "R" else ("L", "X", "R")
            
            count = 1
            idx += 1
            while idx < sln and count > 0:
                sch = start[idx]
                ech = end[idx]
                

                if sch == oppo_char and ech == search_char:
                    # if start array has same character repeated in the a sequence 
                    # then increase the count where start array has "R" and end array has "X"
                    count += 1 
                elif sch == search_char and ech == oppo_char:
                    # if start array has search character and end array has opposite character
                    # decrease the counter
                    count -= 1
                elif sch == block_char or ech == block_char:
                    # both array are not allowed to have "L" in the search range
                    return False

                idx += 1

            if count > 0:
                return False

        return True


# print(Solution().canTransform(
#     "XLXRRXXRXX",
#     "LXXXXXXRRR"))

print(Solution().canTransform(
    "RLX",
    "XLR"))
