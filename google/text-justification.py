from pprint import pprint
from typing import List


class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:

        def justify_line(words, words_width, space_required, max_width):
            no_words = len(words)

            remaining_width = max_width - (words_width + space_required)

            no_space_between_words = 1
            space_between = [no_space_between_words] * space_required

            if remaining_width > 0:

                if space_required != 0:
                    no_space_between_words += (remaining_width //
                                               space_required)
                    total_spacing = no_space_between_words * space_required
                    space_between = [no_space_between_words] * space_required
                    remaining_width = max_width - (words_width + total_spacing)
                    for i in range(remaining_width):
                        space_between[i] += 1
                else:
                    space_between = [max_width - words_width]

            for idx, space in zip(range(1, no_words, 2), space_between):
                words[idx] = " " * space

            return "".join(words)

        result = []

        word_width = 0
        spacing = -1
        line = []
        for word in words:
            wl = len(word)

            if (word_width + wl + spacing + 1) > max_width:
                result.append(justify_line(
                    line, word_width, spacing, max_width))
                line = []
                spacing = -1
                word_width = 0

            word_width += wl
            spacing += 1

            line.append(word)
            line.append("")

        if line:
            line.pop()

            for idx in range(1, len(line), 2):
                line[idx] = " "

            last_line = "".join(line)
            remaining_width = max_width - len(last_line)
            result.append(last_line + " " * remaining_width)

        return result


pprint(Solution().fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16))
pprint(Solution().fullJustify(
    ["What", "must", "be", "acknowledgment", "shall", "be"], 16))
pprint(Solution().fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
