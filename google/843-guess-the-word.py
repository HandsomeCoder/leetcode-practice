from typing import List


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        def get_similarity(word1, word2):
            count = 1
            for idx in range(6):
                if word1[idx] == word2[idx]:
                    count += 1
            return count

        wln = len(words)
        for i in range(wln):
            similarity = 0
            for j in range(i+1, wln):
                similarity = max(similarity, get_similarity(words[i], words[j]))
            
            words[i] = (similarity, words[i])

        words.sort()
        
        match_count = 0
        blacklisted_letters = [set() for _ in range(6)]
        whitelisted_word = None

        for idx in range(wln):
            is_p_word = False
            word = words[idx][1]

            for idx, wch in enumerate(word):
                if wch in blacklisted_letters[idx]:
                    is_p_word = False
                    break

                if whitelisted_word == None:
                    is_p_word = True
                    continue
                
                if wch == whitelisted_word[idx]:
                    is_p_word = True
            
            if not is_p_word:
                continue
   
            count = master.guess(word)

            if count == 0:
                for idx, wch in enumerate(word):
                    blacklisted_letters[idx].add(wch)
            elif count > match_count:
                match_count = count
                whitelisted_word = word
                if match_count == 6:
                    break