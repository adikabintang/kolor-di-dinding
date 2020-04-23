# Runtime: 76 ms, faster than 9.23% of Python3 online submissions 
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions
class Solution:
    def __string_to_char_count(self, S):
        s = ""
        i = 0
        while i < len(S):
            s += S[i]
            ctr = 1
            j = i + 1
            while j < len(S):
                if S[j] == S[i]:
                    ctr += 1
                else:
                    break
                j += 1
            
            i = j
            s += str(ctr)
        
        return s

    def expressiveWords(self, S: str, words: [str]) -> int:
        counter = 0
        s_repr = self.__string_to_char_count(S)

        for word in words:
            word_repr = self.__string_to_char_count(word)
            if len(s_repr) == len(word_repr):
                i = 0
                is_expressive = True
                while i < len(word_repr):
                    if word_repr[i] != s_repr[i]:
                        is_expressive = False
                        break
                    else:
                        i += 1
                        if i < len(word_repr):
                            word_ctr = int(word_repr[i])
                            s_ctr = int(s_repr[i])
                            if word_ctr > s_ctr:
                                is_expressive = False
                                break
                            elif word_ctr < s_ctr and s_ctr < 3:
                                is_expressive = False
                                break
                    i += 1
                
                if is_expressive:
                    counter += 1

        return counter


s = Solution()
print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
