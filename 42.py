  42
#force---------------------------------------------------------
        ans = 0
        for i, item in enumerate(height):
            left_max = 0
            right_max = 0
            left = height[:i]
            right = height[i:]
            if len(left)==0:
                left_max = max(0,item)
            else:
                left_max = max(max(left),item)

            if len(right)==0:
                right_max = max(0,item)
            else:
                right_max = max(max(right),item)
            cur_ans = min(left_max,right_max)-item
            ans+=cur_ans
        return ans
#     ----------------------------------------------------
 
