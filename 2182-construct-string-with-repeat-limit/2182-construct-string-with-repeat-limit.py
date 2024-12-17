class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # counts how many times each char exist
        counts = Counter(s)
        # use priority queue to store the chars in reverse alphabetic order
        pq = [(-ord(char), count) for char, count in counts.items()]
        heapq.heapify(pq)

        result = []
        while pq:
            # get the lexicographically largest char
            ch, count = heapq.heappop(pq)
            used = min(count, repeatLimit)
            result.append(chr(-ch)*used)
            count -= used

            # if the char is not totally used
            if count>0:
                # if there is no remaining char rather than the current in the pq, end
                if not pq:
                    break
                # get the second largest lexicographically largest char and put one
                next_ch, next_count = heapq.heappop(pq)
                result.append(chr(-next_ch))
                next_count -= 1
                # if the remaining is greater than 0, push back into the pq
                if next_count>0:
                    heapq.heappush(pq, (next_ch, next_count))
                # push back into the pq
                heapq.heappush(pq, (ch, count))
        
        return "".join(result)