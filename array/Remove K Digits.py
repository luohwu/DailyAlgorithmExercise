# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k or len(num)==0:
            return '0'
        if k==0:
            return num
        if num[1]=='0':
            idx=1
            while idx<len(num) and num[idx]=='0':
                idx+=1
            return self.removeKdigits(num[idx:],k-1)
        else:
            if num[0]>num[1]:
                return self.removeKdigits(num[1:],k-1)
            else:
                idx=1
                while idx<len(num) and num[idx]>=num[idx-1]:
                    idx+=1
                return self.removeKdigits(num[:idx-1]+num[idx:],k-1)

if __name__=='__main__':
    print(Solution().removeKdigits(
        "1234567890",
    9
    ))

# 1 2 3 1
# 23
# 13
# 12

# 931
# 131
# 191
# 193