##   42
# #force---------------------------------------------------------
#         ans = 0
#         for i, item in enumerate(height):
#             left_max = 0
#             right_max = 0
#             left = height[:i]
#             right = height[i:]
#             if len(left)==0:
#                 left_max = max(0,item)
#             else:
#                 left_max = max(max(left),item)

#             if len(right)==0:
#                 right_max = max(0,item)
#             else:
#                 right_max = max(max(right),item)
#             cur_ans = min(left_max,right_max)-item
#             ans+=cur_ans
#         return ans
# #     ----------------------------------------------------
 
 # 心得
 # DP 不一定直接得出答案。 可以用矩阵储存需要反复查询的量，即[0,i]和[i,n-1]范围内的最大高度
 # 只要是提前计算和存储需要反复查询的量，都可以叫DP。这里计算DP矩阵的方法也是类似于递推，并不需要将递推直接运用于求出答案
import numpy as np
class Solution(object):
    def trap(self,height):
        """
        :type height: List[int]
        :rtype: int
        """
        # define dpl[i] to be max height in the region[0,i]
        # dpr[i] to be max height in the region [i,n-1]
        n = len(height)
        dpl = np.zeros(n)
        dpr = np.zeros(n)
        if n == 0:
            return 0
        dpl[0] = height[0]
        for i in range(1, n):
            dpl[i] = max(height[i], dpl[i - 1])

        dpr[n - 1] = height[n - 1]
        for i in reversed(range(0, n - 1)):
            dpr[i] = max(height[i], dpr[i + 1])

        ans = 0
        for i in range(0, n):
            ans += min(dpl[i], dpr[i]) - height[i]
        return int(ans)

##two pointer， 掌握核心思想，就是左边比右边低，就放心加水，右边比左边低，也放心加水