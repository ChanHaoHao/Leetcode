class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # My code, can process with cw and ccw, but if two distance are the same will fail
        # ans = 0
        # current = 0
        # n = len(ring)

        # dictionary = defaultdict(list)
        # for index, x in enumerate(ring):
        #     dictionary[x].append(index)

        # for curr_key in key:
        #     locations = dictionary[curr_key]
        #     tmp_dist = abs(locations[0]-current)
        #     tmp = min(tmp_dist, n-tmp_dist)
        #     next_loc = locations[0]
        #     for loc in locations[1::]:
        #         dist = min(abs(loc-current), abs(n-loc+current))
        #         if dist<tmp:
        #             tmp = dist
        #             next_loc = loc
        #         else:
        #             break
        #     ans += tmp+1
        #     current = next_loc
        
        # return ans

        # used to count whether to go cw or ccw
        def count_step(current_index, next_index):
            steps = abs(current_index-next_index)
            return min(ringLen-steps, steps)

        def try_lock(ring_index, key_index):
            # if the best_step is counted before, because it goes over the whole key string for each char
            if (ring_index, key_index) in best_steps:
                return best_steps[(ring_index, key_index)]

            # if it reaches the end of the key string
            if key_index==keyLen:
                return 0
            
            min_step = inf
            for char_index in range(ringLen):
                if ring[char_index]==key[key_index]:
                    min_step = min(min_step, count_step(ring_index, char_index)+1+try_lock(char_index, key_index+1))
            
            best_steps[(ring_index, key_index)] = min_step
            return min_step

        ringLen = len(ring)
        keyLen = len(key)
        best_steps = {}

        return try_lock(0, 0)
        