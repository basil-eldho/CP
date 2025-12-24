class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];

        int sum{nums[0]}, res{nums[0]};
        for (int i = 1; i < nums.size(); i++) {
            if (sum + nums[i] > nums[i])
                sum += nums[i];
            else
                sum = nums[i];
            res = max(res, sum);
        }
        return res;
    }
};