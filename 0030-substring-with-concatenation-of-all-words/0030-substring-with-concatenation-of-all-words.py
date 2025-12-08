import copy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # TLE
        # N = len(s)
        # n = len(words[0])
        # ans = []

        # words_count = {}
        # for word in words:
        #     if word not in words_count:
        #         words_count[word] = 1
        #     else:
        #         words_count[word] += 1
        
        # num_words = len(words)
        # i = 0
        # while i<=N-n:
        #     j = 0
        #     seen = {}
        #     while j < num_words:
        #         sub_string = s[i+j*n:i+(j+1)*n]
        #         if sub_string in words_count:
        #             if sub_string not in seen:
        #                 seen[sub_string] = 1
        #             elif seen[sub_string]<words_count[sub_string]:
        #                 seen[sub_string] += 1
        #             else:
        #                 break
        #         else:
        #             break
        #         j += 1
        #     if j == num_words:
        #         ans.append(i)
        #     i += 1
        
        # return ans

        n = len(words[0])
        word_count = Counter(words)
        ans = []

        # there will only be n possible start positions
        for i in range(n):
            start = i
            window = defaultdict(int)
            words_used = 0

            # iterate through all possible chars
            for j in range(i, len(s)-n+1, n):
                word = s[j:j+n]

                # restart the whole dict if it is interrupted
                if word not in word_count:
                    start = j + n
                    window = defaultdict(int)
                    words_used = 0
                    continue
                
                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start:start+n]] -= 1
                    start += n
                    words_used -= 1
                if words_used == len(words):
                    ans.append(start)
        return ans