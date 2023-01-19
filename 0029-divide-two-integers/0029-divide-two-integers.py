class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=0
        dividendABS=abs(dividend)
        divisorABS=abs(divisor)
        while dividendABS>=divisorABS:
            tmp=divisorABS
            mult=1
            while dividendABS>=tmp:
                dividendABS-=tmp
                tmp+=tmp
                ans+=mult
                mult+=mult
                
                
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            ans=0-ans
        if ans>2147483647:
            ans=2147483647
        elif ans<-2147483648:
            ans=-2147483648
        return ans
                    
        '''
        if abs(divisor)==1:
            if divisor<0:
                if dividend<=-2147483648:
                    return 2147483647
                elif dividend>2147483647:
                    return 0-2147483648
                return 0-dividend
            else:
                if dividend>2147483647:
                    return 2147483647
                elif dividend<-2147483648:
                    return -2147483648
                return dividend
        ans=0
        if dividend>0:
            if divisor>0:
                while dividend>=divisor:
                    ans+=1
                    dividend-=divisor
            else:
                while dividend>=abs(divisor):
                    ans-=1
                    dividend+=divisor
        else:
            if divisor>0:
                while abs(dividend)>=divisor:
                    ans-=1
                    dividend+=divisor
            else:
                while abs(dividend)>=abs(divisor):
                    ans+=1
                    dividend-=divisor
        if ans>2147483647:
            return 2147483647
        elif ans<-2147483648:
            return -2147483648
        return ans
        '''