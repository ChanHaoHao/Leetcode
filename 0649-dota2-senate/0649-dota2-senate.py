class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D, toBeBanR, toBeBanD = 0, 0, 0, 0

        # count how many senators are in each side
        for x in senate:
            if x=="R":
                R+=1
            else:
                D+=1

        senate = list(senate)
        # while opposite sides remains
        while R>0 and D>0:
            for index, current in enumerate(senate):
                if current == "R":
                    # if there are D ahead that did not use the right before
                    if toBeBanR>0:
                        toBeBanR-=1
                        senate[index]="X"
                        R-=1
                    # there is another senator to ban D
                    else:
                        toBeBanD+=1
                elif current == "D":
                    if toBeBanD>0:
                        toBeBanD-=1
                        senate[index]="X"
                        D-=1
                    else:
                        toBeBanR+=1
        
        if R>0:
            return "Radiant"
        else:
            return "Dire"