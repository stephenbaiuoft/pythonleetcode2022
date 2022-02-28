class Solution:
    # https://leetcode.com/problems/multiply-strings/
    # 要点 
    # 每一位 x 每一位
    # reverse下 这样来算 i j相对应的值
    # i + j + 1这一位 需要 += 因为当 inner loop循环结束 outer loop循环的时候 i + j + 1是会有值的
    def multiply(self, num1: str, num2: str) -> str:
        if (num1 == "0" or num2 == "0"):
            return "0"
        
        total_n = len(num1) + len(num2)
        answer = [0] * total_n

        rn1 = num1[::-1]
        rn2 = num2[::-1]

        for i, vi in enumerate(rn1):
            for j, vj in enumerate(rn2):
                # keep carry as it's computation from previous j values
                carry = answer[i+j]
                val_compute = int(vi) * int(vj) + carry
                
                # now we'd need to set the new computed value for i+j
                answer[i+j] = val_compute % 10
                # in the next i iteration, (it has computed with all j)
                # this needs to be carried over too 
                answer[i+j+1] += val_compute //10
            
        # get rid of leading 0
        if (answer[-1] == 0):
            answer.pop()

        return ''.join([str(d) for d in reversed(answer)])
