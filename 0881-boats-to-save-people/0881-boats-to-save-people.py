class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums, ans, cal, ori = 0, 0, False, len(people)
        people.sort(reverse=True)
        print(people)
        while nums!=ori:
            if people[0]==limit:
                ans+=1
                nums+=1
                people.pop(0)

            else:
                for x in range(len(people)-1,0,-1):
                    if people[x]+people[0]<=limit:
                        ans+=1
                        nums+=2
                        people.pop(x)
                        people.pop(0)
                        cal=True
                        break

                if cal==False:    
                    ans+=1
                    nums+=1
                    people.pop(0)
                cal=False
            
        return ans