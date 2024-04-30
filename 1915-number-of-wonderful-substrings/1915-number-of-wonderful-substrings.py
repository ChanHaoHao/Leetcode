class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # going through every substring and initialize it evertime, TLE
        # ans = 0
        # n = len(word)

        # for start in range(n):
        #     ans += 1
        #     single = set()
        #     single.add(word[start])
        #     for end in range(start+1, n):
        #         if word[end] in single:
        #             single.remove(word[end])
        #         else:
        #             single.add(word[end])
                
        #         if len(single)<=1:
        #             ans+=1

        # return ans

        freq = {}
        freq[0]=1

        mask = 0
        ans = 0
        for x in word:
            # move a to 0, b to 1, etc...
            bit = ord(x)-97

            # we use bitmaps to store the frequecy easier
            # flip the current bit, if the current char is 'a' => 1 << 0 = 1
            # if the current char is 'b' => 1 << 1 = 2
            # the ^= (XOR) flips the bit
            mask ^= (1 << bit)

            # increase the freq of the mask by 1
            if mask in freq:
                print(mask)
                ans += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1

            # this flips one bit at a time to check if the substring 
            # will become wonderful when a bit if flipped (odd)
            for odd in range(0, 10):
                if (mask ^ (1 << odd)) in freq:
                    ans += freq[mask ^ (1 << odd)]
        
        return ans