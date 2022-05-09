# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
        # n=len(s)
        # if n==0:
        #     return 0
        # dp_table=dict()
        # dp_table[0]={'char':s[0],'length':1,'k_remaining':k}
        # for idx,char in enumerate(s[1:],start=1):
        #     if char == dp_table[idx-1]['char']:
        #         dp_table[idx]={'char':dp_table[idx-1]['char'],\
        #                        'length':dp_table[idx-1]['length']+1,\
        #                        'k_remaining':dp_table[idx-1]['k_remaining']}
        #     elif dp_table[idx-1]['k_remaining']>0:
        #         dp_table[idx]={'char':dp_table[idx-1]['char'],\
        #                        'length':dp_table[idx-1]['length']+1,\
        #                        'k_remaining':dp_table[idx-1]['k_remaining']-1}
        #     else:
        #         pre_idx=idx-1
        #         current_length=1
        #         while pre_idx>=0 and s[pre_idx]==char:
        #             current_length+=1
        #             pre_idx-=1
        #
        #
        #         dp_table[idx]={'char':char,\
        #                        'length':current_length,\
        #                        'k_remaining':k}
        # final_length=[1]*n
        # for idx_start,values in dp_table.items():
        #     idx_start=idx_start-values['length']+1
        #     frontest=max(0,idx_start-values['k_remaining'])
        #     preceding_str=s[frontest:(idx_start)]
        #     num_same_char=preceding_str.count(values['char'])
        #     final_length[idx_start]=min(n,values['length']+values['k_remaining']+num_same_char)
        #
        # return max(final_length)

if __name__=='__main__':
    print(Solution().characterReplacement(
        "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH",
    7
    ))

