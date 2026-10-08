class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        answer = []
        f_row = "qwertyuiop"
        s_row = "asdfghjkl"
        t_row = "zxcvbnm"
        for word in words:
            flag = 1
            word_low = word.lower()
            if word_low[0] in f_row:
                poss_row = f_row
            elif word_low[0] in s_row:
                poss_row = s_row
            else:
                poss_row = t_row

            for char in word_low:
                if char not in poss_row:
                    flag = 0
                    break

            if flag:
                answer.append(word)
        return answer
