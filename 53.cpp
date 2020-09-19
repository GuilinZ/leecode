//一定要注意定义的dp的含义，不一定要直接求出答案，只要dp数组里能找出想要的答案就行
//本题，dp[i]表示到第i个元素为止，包含第i个元素的连续数组的最大sum
//因此在状态转移时，就能考虑dp[i]和dp[i-1]的关系了，等于是定义状态时强加了限制，而不需要在状态转移时来考虑不连续的情况
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int dp[n];
        dp[0]=nums[0];
        int out=dp[0];
        if (nums.size()==1){
            return dp[0];
        }
        for (int i=1; i<n; i++){
            dp[i] = max(nums[i],nums[i]+dp[i-1]);
            if (dp[i]>out){
                out=dp[i];
            }
        }
        return out;
    }
};