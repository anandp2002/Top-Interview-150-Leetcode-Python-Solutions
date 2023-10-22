class Solution(object):
    def romanToInt(self, s):
        number=0
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        l=len(s)
        prev=0
        for char in s:
            curr=dic[char]
            if curr>prev:
                number+=(curr-2*prev)
            else:
                number+=curr
            prev=curr
        return number