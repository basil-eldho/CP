class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int high{0}, low{0}, diff{0};

        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < prices[low]) {
                low = i;
                high = i;
            }

            if (prices[i] > prices[high])
                high = i;
            diff = max(diff, prices[high] - prices[low]);
        }
        return diff;
    }
};