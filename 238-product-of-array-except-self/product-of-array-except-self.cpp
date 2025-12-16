class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();

        vector<int> temp(len, 1);
        vector<int> output(len, 0);

        int numOfZero{0};
        for (int i = len - 1; i >= 0; i--) {
            if (i)
                temp[i - 1] = temp[i] * nums[i];
            if (!nums[i])
                numOfZero++;
        }

        if (numOfZero >= 2)
            return output;

        int left = 1;
        for (int i = 0; i < len; i++) {
            output[i] = left * temp[i];
            left *= nums[i];
        }

        return output;
    }
};