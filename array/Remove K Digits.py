# https://leetcode.com/problems/remove-k-digits/

class Solution:
    # O(k*n) method
    # too slow
    def removeKdigits_Slow(self, num: str, k: int) -> str:
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


    # O(n) method

    def removeKdigits(self, num: str, k: int) -> str:

        # stack
        res=[]
        for digit in num:
            # if the stack is empty
            # or
            # the last element of the stack is less than the current digit
            # just push the digit into the stack
            if res==[] or res[-1]<digit:
                res.append(digit)
            else:
                # remove the last elemnt of the stack if it is greater than the current digit
                # by this, we ensure that the smallest digit is always placed at the more significant position
                while res and res[-1]>digit and k>0:
                    k-=1
                    res.pop()
                res.append(digit)

        # if there are still digits to remove
        if k>0:
            res=res[:-k]

        # remove pre '0'
        if res:
            idx = 0
            while idx < len(res) and res[idx] == '0':
                idx += 1
            res = res[idx:]
        return ''.join(res) or '0'



if __name__=='__main__':
    print(Solution().removeKdigits(

        "1432219",
    3
    ))

# 1 2 3 1
# 23
# 13
# 12

# 931
# 131
# 191
# 193