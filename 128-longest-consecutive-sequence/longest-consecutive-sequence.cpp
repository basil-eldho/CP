class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int maxLen{0};
        for (int num : s) {
            if (!s.count(num - 1)) {
                int len{0};
                int curr{num};
                while (s.count(curr++)) {
                    len++;
                }
                maxLen = max(maxLen, len);
            }
        }
        return maxLen;
    }
};