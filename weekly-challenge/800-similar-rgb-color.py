class Solution:

    def __init__(self) -> None:
        self.possible_tone = []
        self.cache = {}

        for i in range(17):
            itr = hex(i)[2:]
            hexcode = itr + itr
            self.possible_tone.append((self.toInt(hexcode), hexcode))

    def toInt(self, hexch):
        if hexch not in self.cache:
            self.cache[hexch] = int(hexch, 16)
        return self.cache[hexch]

    def similarRGB(self, color: str) -> str:

        def get_min_diff(x):
            x = self.toInt(x)
            min_diff = 300
            ch = None

            for itr, ich in self.possible_tone:
                diff = abs(x - itr)
                if diff < min_diff:
                    min_diff = diff
                    ch = ich
                else:
                    return ch

            return ch

        return "#" + "".join([get_min_diff(color[1:3]), get_min_diff(color[3:5]), get_min_diff(color[5:])])


print(Solution().similarRGB("#09f166"))
