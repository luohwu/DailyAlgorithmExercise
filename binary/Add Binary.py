# https://leetcode.com/problems/add-binary/


class Solution:
    # ok, this simple method can beat 88% submissions, out of my expectation
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            short=b
            long=a
        else:
            short=a
            long=b

        result=''
        # '1'+'1' -> '0', carry=True
        carry=False
        for i in range(len(short)):
            if short[-1-i]=='1' and long[-1-i]=='1':
                if carry:
                    result='1'+result
                else:
                    result='0'+result
                carry=True
            elif short[-1-i]=='0' and long[-1-i]=='0':
                if carry:
                    result='1'+result
                    carry=False
                else:
                    result='0'+result
            else:
                if carry:
                    result='0'+result
                else:
                    result='1'+result
        i+=1
        while i<len(long):
            if long[-1-i]=='1':
                if carry:
                    result='0'+result
                else:
                    result='1'+result
            else:
                if carry:
                    result='1'+result
                    carry=False
                else:
                    result='0'+result
            i+=1
        if carry:
            result='1'+result


        return result

if __name__=='__main__':
    print(Solution().addBinary(
        '101'
      ,'1011'
    ))

    '10000'

