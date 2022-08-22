from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        if endWord == beginWord:
            return 1

        ln = len(beginWord)
        options = [set() for _ in range(ln)]

        for word in wordList:
            for idx in range(ln):
                options[idx].add(word[idx])

    
        options = [list(option) for option in options]
        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            word, ln = queue.popleft()

            if word in visited:
                continue

            visited.add(word)

            for idx, sch in enumerate(word):
                for och in options[idx]:
                    if och == sch:
                        continue
                    new_word = word[:idx] + och + word[idx+1:]
                    if new_word in words and new_word not in visited:                        
                        if new_word == endWord:
                            return ln + 1
                        queue.append((new_word, ln+1))
        return 0


print(Solution().ladderLength(beginWord="hit", endWord="cog",
      wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
