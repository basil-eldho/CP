class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1);

        int len1 = nums1.size();
        int len2 = nums2.size();
        int totalLeft = (len1 + len2 + 1) / 2;

        int left = 0, right = len1;
        while (left <= right) {
            int p1 = left + (right - left) / 2;
            int p2 = totalLeft - p1;

            int l1 = (p1 == 0) ? INT_MIN : nums1[p1 - 1];
            int r1 = p1 == len1 ? INT_MAX : nums1[p1];

            int l2 = (p2 == 0) ? INT_MIN : nums2[p2 - 1];
            int r2 = (p2 == len2) ? INT_MAX : nums2[p2];

            if (l1 <= r2 && l2 <= r1) {
                return (len1 + len2) % 2 ? max(l1, l2)
                                 : (max(l1, l2) + min(r1, r2)) / 2.0;
            } else if (l1 > r2) {
                right = p1 - 1;
            } else
                left = p1 + 1;
        }
        return 0.0;
    }
};