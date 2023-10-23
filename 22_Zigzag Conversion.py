class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        dic={row:"" for row in range(1,numRows+1)}
        curr_dir=-1
        row=1
        for i in range(len(s)):
            dic[row]+=s[i]
            if row==1 or row==numRows:
                curr_dir=-(curr_dir)
            row+=curr_dir   
        res=""
        for i in dic.values():
            res+=i
        return res