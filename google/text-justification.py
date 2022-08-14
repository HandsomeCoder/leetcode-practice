from pprint import pprint
from typing import List


class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:

        spacing_repo = {}

        def justify_line(words, words_width, space_required, max_width):
            no_words = len(words)
            remaining_width = max_width - words_width
            space_between = None

            if space_required != 0:
                no_space_between_words = (remaining_width // space_required)
                total_spacing = no_space_between_words * space_required
                space_between = [no_space_between_words] * space_required
                remaining_width = max_width - (words_width + total_spacing)
                for i in range(remaining_width):
                    space_between[i] += 1
            else:
                space_between = [max_width - words_width]

            for idx, space in zip(range(1, no_words, 2), space_between):
                if space not in spacing_repo:
                    spacing_repo[space] = " " * space
                words[idx] = spacing_repo[space]
            return "".join(words)

        result = []

        word_width, spacing, line = 0, -1, []

        for word in words:
            wl = len(word)

            if (word_width + wl + spacing + 1) > max_width:
                result.append(justify_line(
                    line, word_width, spacing, max_width))
                word_width, spacing, line = 0, -1, []

            word_width += wl
            spacing += 1

            line.append(word)
            line.append("")


        line.pop()
        for idx in range(1, len(line), 2):
            line[idx] = " "

        last_line = "".join(line)
        remaining_width = max_width - len(last_line)
        result.append(last_line + " " * remaining_width)

        return result
