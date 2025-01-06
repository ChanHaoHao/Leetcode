class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left, right = 0, 0
        if boxes[0]=='1':
            left = 1
        
        steps = 0
        for x in range(1, len(boxes)):
            if boxes[x]=='1':
                right += 1
                steps += x
        
        ans = [steps]
        for x in range(1, len(boxes)):
            if boxes[x]=='1':
                steps -= 1
                right -= 1
            steps += left-right
            ans.append(steps)
            if boxes[x]=='1':
                left += 1
        
        return ans