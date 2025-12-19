# 🔥 30-Day Hardcore DSA Mastery Plan (C++)

**Goal:** Crack ANY DSA interview question in 30 days  
**Time Investment:** 10–12 hours/day  
**Approach:** Hybrid — Learn + Implement + Solve + Review

---

## 📋 Correct Learning Order (CRITICAL)

Follow this order strictly:

1. Arrays & Strings (Days 1–4)
2. Hashing (Days 5–6)
3. Stack (Day 7)
4. Queue / Deque (Day 8)
5. Linked List (Days 9–10)
6. Recursion (Days 11–12)
7. Backtracking (Day 13)
8. Trees (Days 14–17)
9. Heap (Day 18)
10. Graph (Days 19–22)
11. Binary Search (Day 23)
12. Greedy (Days 24–25)
13. Dynamic Programming (Days 26–30)

---

## ⏱️ Problems Target per Data Structure

| Data Structure   | Problems |
|------------------|----------|
| Arrays/Strings   | 15–20    |
| Hashing          | 10–15    |
| Stack            | 8–12     |
| Queue/Deque      | 5–8      |
| Linked List      | 8–12     |
| Trees            | 20–25    |
| Heap             | 8–12     |
| Graph            | 15–20    |
| DP               | 25–30    |

---

## 📅 Daily Structure (10–12 hours)

1. **Learn & Read** (1.5–2 hrs) — Theory, patterns, watch videos
2. **Implement Templates** (1–2 hrs) — Write clean C++ code
3. **Solve Problems** (4–6 hrs) — Timed practice (easy: 20m, medium: 35m, hard: 60m)
4. **Review & Notes** (1 hr) — Editorial analysis, cheat-sheet updates
5. **Quick Practice** (1–2 hrs) — Redo mistakes, flashcards, mock interview

**Weekly Assessment:** Every 7 days — 2-hour timed contest + 1-hour review

---

# 📚 Day-by-Day Breakdown

## Days 1–4: ARRAYS & STRINGS

### Key Patterns:
- Two Pointers
- Sliding Window
- Prefix Sum / Suffix Sum
- Kadane's Algorithm
- Dutch National Flag

### Implement in C++:
```cpp
// Two pointers template
void twoPointers(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        // logic
        left++; right--;
    }
}

// Sliding window template
int slidingWindow(vector<int>& arr, int k) {
    int window_sum = 0, max_sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        window_sum += arr[i];
        if (i >= k - 1) {
            max_sum = max(max_sum, window_sum);
            window_sum -= arr[i - k + 1];
        }
    }
    return max_sum;
}

// Prefix sum
vector<int> prefixSum(vector<int>& arr) {
    vector<int> prefix(arr.size() + 1, 0);
    for (int i = 0; i < arr.size(); i++)
        prefix[i + 1] = prefix[i] + arr[i];
    return prefix;
}

// Kadane's algorithm (max subarray)
int maxSubArray(vector<int>& nums) {
    int max_so_far = nums[0], max_ending = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        max_ending = max(nums[i], max_ending + nums[i]);
        max_so_far = max(max_so_far, max_ending);
    }
    return max_so_far;
}
```

### LeetCode Problems (15–20):

**Easy:**
1. [Two Sum](https://leetcode.com/problems/two-sum/)
2. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
3. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
4. [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
5. [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Medium:**
6. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
7. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
8. [3Sum](https://leetcode.com/problems/3sum/)
9. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
10. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
11. [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
12. [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
13. [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
14. [Rotate Image](https://leetcode.com/problems/rotate-image/)
15. [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

**Hard:**
16. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
17. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
18. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

### Patterns Learned:
✓ Two pointers for sorted/unsorted arrays  
✓ Sliding window for subarray problems  
✓ Prefix sum for range queries  
✓ Kadane for max subarray  
✓ In-place array manipulation  

---

## Days 5–6: HASHING

### Key Patterns:
- Frequency counting
- Two-sum variants
- Anagram detection
- Subarray with sum/product

### Implement in C++:
```cpp
#include <unordered_map>
#include <unordered_set>

// Frequency map
unordered_map<int, int> freq;
for (int x : arr) freq[x]++;

// Check existence
unordered_set<int> seen;
if (seen.count(target - num)) { /* found */ }
seen.insert(num);

// Group anagrams helper
string getKey(string s) {
    sort(s.begin(), s.end());
    return s;
}
```

### LeetCode Problems (10–15):

**Easy:**
1. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
2. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
3. [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
4. [Happy Number](https://leetcode.com/problems/happy-number/)

**Medium:**
5. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
6. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
7. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
8. [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
9. [4Sum II](https://leetcode.com/problems/4sum-ii/)
10. [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
11. [LRU Cache](https://leetcode.com/problems/lru-cache/)

**Hard:**
12. [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
13. [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)

### Patterns Learned:
✓ Hash maps for O(1) lookups  
✓ Frequency counting  
✓ Complement search (two-sum pattern)  
✓ Prefix sum + hashing  

---

## Day 7: STACK

### Key Patterns:
- Monotonic stack
- Expression parsing
- Valid parentheses
- Next Greater/Smaller Element

### Implement in C++:
```cpp
#include <stack>

// Monotonic decreasing stack (next greater element)
vector<int> nextGreaterElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> st; // stores indices
    
    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            result[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return result;
}

// Valid parentheses
bool isValid(string s) {
    stack<char> st;
    unordered_map<char, char> pairs = {{')', '('}, {']', '['}, {'}', '{'}};
    
    for (char c : s) {
        if (pairs.count(c)) {
            if (st.empty() || st.top() != pairs[c]) return false;
            st.pop();
        } else {
            st.push(c);
        }
    }
    return st.empty();
}
```

### LeetCode Problems (8–12):

**Easy:**
1. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
2. [Min Stack](https://leetcode.com/problems/min-stack/)
3. [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

**Medium:**
4. [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
5. [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
6. [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
7. [Online Stock Span](https://leetcode.com/problems/online-stock-span/)
8. [Decode String](https://leetcode.com/problems/decode-string/)
9. [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)

**Hard:**
10. [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
11. [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
12. [Basic Calculator](https://leetcode.com/problems/basic-calculator/)

### Patterns Learned:
✓ Monotonic stack for next/prev greater/smaller  
✓ Stack for expression parsing  
✓ Balanced parentheses validation  

---

## Day 8: QUEUE / DEQUE

### Key Patterns:
- BFS traversal
- Sliding window with deque
- Level-order operations

### Implement in C++:
```cpp
#include <queue>
#include <deque>

// BFS template
void bfs(Node* root) {
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        
        // Process curr
        for (Node* child : curr->children)
            q.push(child);
    }
}

// Sliding window maximum using deque
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq; // stores indices
    vector<int> result;
    
    for (int i = 0; i < nums.size(); i++) {
        // Remove out of window
        if (!dq.empty() && dq.front() <= i - k)
            dq.pop_front();
        
        // Maintain decreasing order
        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
        
        dq.push_back(i);
        
        if (i >= k - 1)
            result.push_back(nums[dq.front()]);
    }
    return result;
}
```

### LeetCode Problems (5–8):

**Easy:**
1. [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

**Medium:**
2. [Number of Islands](https://leetcode.com/problems/number-of-islands/)
3. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
4. [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
5. [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

**Hard:**
6. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)
7. [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

### Patterns Learned:
✓ BFS for level-order traversal  
✓ Deque for sliding window optimization  
✓ Queue for FIFO processing  

---

## Days 9–10: LINKED LIST

### Key Patterns:
- Fast & Slow pointers (cycle detection)
- Reverse linked list
- Merge operations
- In-place modifications

### Implement in C++:
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Reverse linked list
ListNode* reverse(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    
    while (curr) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

// Detect cycle (Floyd's algorithm)
bool hasCycle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

// Find middle
ListNode* findMiddle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
```

### LeetCode Problems (8–12):

**Easy:**
1. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
2. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
3. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
4. [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
5. [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

**Medium:**
6. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
7. [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
8. [Reorder List](https://leetcode.com/problems/reorder-list/)
9. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
10. [Sort List](https://leetcode.com/problems/sort-list/)
11. [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

**Hard:**
12. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

### Patterns Learned:
✓ Fast & slow pointers  
✓ In-place reversal  
✓ Dummy node technique  
✓ Two-pointer for nth node  

---

## Days 11–12: RECURSION

### Key Patterns:
- Base case + recursive case
- Divide and conquer
- Tree recursion
- Memoization

### Implement in C++:
```cpp
// Basic recursion template
int solve(int n, vector<int>& memo) {
    // Base case
    if (n <= 1) return n;
    
    // Memoization check
    if (memo[n] != -1) return memo[n];
    
    // Recursive case
    memo[n] = solve(n-1, memo) + solve(n-2, memo);
    return memo[n];
}

// Tree recursion (depth calculation)
int maxDepth(TreeNode* root) {
    if (!root) return 0;
    return 1 + max(maxDepth(root->left), maxDepth(root->right));
}

// Generate all subsets
void generateSubsets(vector<int>& nums, int idx, vector<int>& curr, 
                     vector<vector<int>>& result) {
    if (idx == nums.size()) {
        result.push_back(curr);
        return;
    }
    
    // Don't include current
    generateSubsets(nums, idx + 1, curr, result);
    
    // Include current
    curr.push_back(nums[idx]);
    generateSubsets(nums, idx + 1, curr, result);
    curr.pop_back();
}
```

### LeetCode Problems (8–10):

**Easy:**
1. [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
2. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
3. [Power of Two](https://leetcode.com/problems/power-of-two/)

**Medium:**
4. [Pow(x, n)](https://leetcode.com/problems/powx-n/)
5. [Subsets](https://leetcode.com/problems/subsets/)
6. [Subsets II](https://leetcode.com/problems/subsets-ii/)
7. [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
8. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

**Hard:**
9. [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
10. [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)

### Patterns Learned:
✓ Base case identification  
✓ Recursive state management  
✓ Memoization for optimization  

---

## Day 13: BACKTRACKING

### Key Patterns:
- Generate all combinations/permutations
- Constraint satisfaction
- Pruning
- State restoration

### Implement in C++:
```cpp
// Backtracking template
void backtrack(vector<int>& candidates, int target, int start,
               vector<int>& current, vector<vector<int>>& result) {
    // Base case (success)
    if (target == 0) {
        result.push_back(current);
        return;
    }
    
    // Base case (failure)
    if (target < 0) return;
    
    for (int i = start; i < candidates.size(); i++) {
        // Choose
        current.push_back(candidates[i]);
        
        // Explore
        backtrack(candidates, target - candidates[i], i, current, result);
        
        // Unchoose (backtrack)
        current.pop_back();
    }
}

// Permutations with visited tracking
void permute(vector<int>& nums, vector<bool>& used,
             vector<int>& current, vector<vector<int>>& result) {
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }
    
    for (int i = 0; i < nums.size(); i++) {
        if (used[i]) continue;
        
        used[i] = true;
        current.push_back(nums[i]);
        
        permute(nums, used, current, result);
        
        current.pop_back();
        used[i] = false;
    }
}
```

### LeetCode Problems (8–10):

**Medium:**
1. [Permutations](https://leetcode.com/problems/permutations/)
2. [Permutations II](https://leetcode.com/problems/permutations-ii/)
3. [Combination Sum](https://leetcode.com/problems/combination-sum/)
4. [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
5. [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
6. [Word Search](https://leetcode.com/problems/word-search/)
7. [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

**Hard:**
8. [N-Queens](https://leetcode.com/problems/n-queens/)
9. [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
10. [Word Search II](https://leetcode.com/problems/word-search-ii/)

### Patterns Learned:
✓ Choose → Explore → Unchoose pattern  
✓ Pruning for optimization  
✓ State restoration  
✓ Constraint checking  

---

## Days 14–17: TREES

### Key Patterns:
- DFS traversals (inorder, preorder, postorder)
- BFS (level-order)
- Tree DP
- BST properties
- LCA (Lowest Common Ancestor)

### Implement in C++:
```cpp
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// Inorder traversal (recursive)
void inorder(TreeNode* root, vector<int>& result) {
    if (!root) return;
    inorder(root->left, result);
    result.push_back(root->val);
    inorder(root->right, result);
}

// Level-order traversal (BFS)
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int size = q.size();
        vector<int> level;
        
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}

// BST search
TreeNode* searchBST(TreeNode* root, int val) {
    if (!root || root->val == val) return root;
    return val < root->val ? searchBST(root->left, val) 
                           : searchBST(root->right, val);
}

// Lowest Common Ancestor
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    
    if (left && right) return root;
    return left ? left : right;
}
```

### LeetCode Problems (20–25):

**Easy:**
1. [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
2. [Same Tree](https://leetcode.com/problems/same-tree/)
3. [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
4. [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
5. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
6. [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
7. [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

**Medium:**
8. [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
9. [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
10. [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
11. [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
12. [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
13. [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
14. [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
15. [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
16. [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
17. [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
18. [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

**Hard:**
19. [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
20. [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
21. [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/)
22. [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)

### Patterns Learned:
✓ Recursive tree traversals  
✓ Level-order (BFS) processing  
✓ Tree DP (height, diameter, path sum)  
✓ BST properties and operations  
✓ LCA algorithms  

---

## Day 18: HEAP (Priority Queue)

### Key Patterns:
- Top K elements
- Merge K sorted
- Median maintenance
- Custom comparators

### Implement in C++:
```cpp
#include <queue>

// Max heap
priority_queue<int> maxHeap;

// Min heap
priority_queue<int, vector<int>, greater<int>> minHeap;

// Custom comparator (for pairs)
struct CompareSecond {
    bool operator()(pair<int,int> a, pair<int,int> b) {
        return a.second > b.second; // min heap based on second element
    }
};
priority_queue<pair<int,int>, vector<pair<int,int>>, CompareSecond> pq;

// Top K frequent elements
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) freq[num]++;
    
    auto cmp = [](pair<int,int> a, pair<int,int> b) {
        return a.second > b.second;
    };
    priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
    
    for (auto& p : freq) {
        pq.push(p);
        if (pq.size() > k) pq.pop();
    }
    
    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top().first);
        pq.pop();
    }
    return result;
}

// Median finder using two heaps
class MedianFinder {
    priority_queue<int> maxHeap; // left half
    priority_queue<int, vector<int>, greater<int>> minHeap; // right half
    
public:
    void addNum(int num) {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        if (maxHeap.size() > minHeap.size())
            return maxHeap.top();
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
```

### LeetCode Problems (8–12):

**Easy:**
1. [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
2. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

**Medium:**
3. [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
4. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
5. [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
6. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)
7. [Reorganize String](https://leetcode.com/problems/reorganize-string/)
8. [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

**Hard:**
9. [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
10. [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
11. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
12. [IPO](https://leetcode.com/problems/ipo/)

### Patterns Learned:
✓ Top K selection with heaps  
✓ Custom comparators  
✓ Two-heap technique for median  
✓ Merge K sorted structures  

---

## Days 19–22: GRAPHS

### Key Patterns:
- BFS / DFS traversal
- Cycle detection
- Topological sort
- Shortest paths (Dijkstra, Bellman-Ford)
- Union-Find (Disjoint Set)
- Minimum Spanning Tree

### Implement in C++:
```cpp
#include <vector>
#include <queue>

// Graph representation
vector<vector<int>> adj; // adjacency list

// DFS
void dfs(int node, vector<bool>& visited) {
    visited[node] = true;
    // Process node
    
    for (int neighbor : adj[node]) {
        if (!visited[neighbor])
            dfs(neighbor, visited);
    }
}

// BFS
void bfs(int start) {
    queue<int> q;
    vector<bool> visited(adj.size(), false);
    
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

// Cycle detection (undirected)
bool hasCycleDFS(int node, int parent, vector<bool>& visited) {
    visited[node] = true;
    
    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            if (hasCycleDFS(neighbor, node, visited))
                return true;
        } else if (neighbor != parent) {
            return true;
        }
    }
    return false;
}

// Topological sort (Kahn's algorithm)
vector<int> topologicalSort(int n, vector<vector<int>>& adj) {
    vector<int> indegree(n, 0);
    for (int i = 0; i < n; i++)
        for (int j : adj[i])
            indegree[j]++;
    
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (indegree[i] == 0)
            q.push(i);
    
    vector<int> result;
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        result.push_back(node);
        
        for (int neighbor : adj[node]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0)
                q.push(neighbor);
        }
    }
    
    return result.size() == n ? result : vector<int>();
}

// Dijkstra's algorithm
vector<int> dijkstra(int start, int n, vector<vector<pair<int,int>>>& graph) {
    vector<int> dist(n, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    
    dist[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if (d > dist[u]) continue;
        
        for (auto [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

// Union-Find (Disjoint Set Union)
class UnionFind {
    vector<int> parent, rank;
public:
    UnionFind(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        if (rank[px] == rank[py]) rank[px]++;
        return true;
    }
};
```

### LeetCode Problems (15–20):

**Easy:**
1. [Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/)
2. [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)

**Medium:**
3. [Number of Islands](https://leetcode.com/problems/number-of-islands/)
4. [Clone Graph](https://leetcode.com/problems/clone-graph/)
5. [Course Schedule](https://leetcode.com/problems/course-schedule/)
6. [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
7. [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
8. [Number of Provinces](https://leetcode.com/problems/number-of-provinces/)
9. [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
10. [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
11. [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)
12. [Network Delay Time](https://leetcode.com/problems/network-delay-time/)
13. [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
14. [Accounts Merge](https://leetcode.com/problems/accounts-merge/)

**Hard:**
15. [Word Ladder](https://leetcode.com/problems/word-ladder/)
16. [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
17. [Minimum Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/)
18. [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)
19. [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)
20. [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)

### Patterns Learned:
✓ Graph traversal (BFS/DFS)  
✓ Cycle detection  
✓ Topological sorting  
✓ Shortest path algorithms  
✓ Union-Find for connectivity  
✓ MST algorithms  

---

## Day 23: BINARY SEARCH (Search on Answer)

### Key Patterns:
- Binary search on sorted array
- Search in rotated array
- Parametric search (search on answer space)
- First/last occurrence

### Implement in C++:
```cpp
// Standard binary search
int binarySearch(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

// First occurrence
int firstOccurrence(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    int result = -1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            result = mid;
            right = mid - 1; // continue searching left
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return result;
}

// Search on answer template
bool isPossible(int mid, /* parameters */) {
    // Check if 'mid' is a valid answer
    return true;
}

int searchOnAnswer(int low, int high) {
    int result = -1;
    
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        if (isPossible(mid)) {
            result = mid;
            // Depending on problem: minimize or maximize
            high = mid - 1; // or low = mid + 1
        } else {
            low = mid + 1; // or high = mid - 1
        }
    }
    return result;
}
```

### LeetCode Problems (8–12):

**Easy:**
1. [Binary Search](https://leetcode.com/problems/binary-search/)
2. [First Bad Version](https://leetcode.com/problems/first-bad-version/)
3. [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
4. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

**Medium:**
5. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
6. [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
7. [Find Peak Element](https://leetcode.com/problems/find-peak-element/)
8. [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
9. [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
10. [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
11. [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

**Hard:**
12. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
13. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

### Patterns Learned:
✓ Monotonic predicate for binary search  
✓ Search on answer space  
✓ First/last occurrence techniques  
✓ Rotated array handling  

---

## Days 24–25: GREEDY

### Key Patterns:
- Activity selection
- Interval scheduling
- Huffman coding
- Fractional knapsack
- Greedy choice property + proof

### Implement in C++:
```cpp
// Interval scheduling (activity selection)
int maxEvents(vector<vector<int>>& events) {
    sort(events.begin(), events.end(), [](auto& a, auto& b) {
        return a[1] < b[1]; // sort by end time
    });
    
    int count = 0, lastEnd = 0;
    for (auto& event : events) {
        if (event[0] >= lastEnd) {
            count++;
            lastEnd = event[1];
        }
    }
    return count;
}

// Jump game
bool canJump(vector<int>& nums) {
    int maxReach = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (i > maxReach) return false;
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}
```

### LeetCode Problems (10–15):

**Easy:**
1. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
2. [Assign Cookies](https://leetcode.com/problems/assign-cookies/)
3. [Lemonade Change](https://leetcode.com/problems/lemonade-change/)

**Medium:**
4. [Jump Game](https://leetcode.com/problems/jump-game/)
5. [Jump Game II](https://leetcode.com/problems/jump-game-ii/)
6. [Gas Station](https://leetcode.com/problems/gas-station/)
7. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
8. [Partition Labels](https://leetcode.com/problems/partition-labels/)
9. [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/)
10. [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
11. [Task Scheduler](https://leetcode.com/problems/task-scheduler/)

**Hard:**
12. [Candy](https://leetcode.com/problems/candy/)
13. [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)
14. [Remove Boxes](https://leetcode.com/problems/remove-boxes/)

### Patterns Learned:
✓ Greedy choice property identification  
✓ Interval scheduling problems  
✓ Proving correctness of greedy approach  
✓ When to use greedy vs DP  

---

## Days 26–30: DYNAMIC PROGRAMMING (INTERVIEW GOLD)

### Key Patterns:
- Memoization (top-down)
- Tabulation (bottom-up)
- 0/1 Knapsack
- Unbounded Knapsack
- LCS, LIS
- Edit Distance
- DP on grids
- State machine DP

### Implement in C++:
```cpp
// Memoization template
int solveMemo(int idx, int target, vector<int>& arr, vector<vector<int>>& dp) {
    // Base cases
    if (target == 0) return 1;
    if (idx < 0 || target < 0) return 0;
    
    // Check memo
    if (dp[idx][target] != -1) return dp[idx][target];
    
    // Recurrence: take or not take
    int take = solveMemo(idx - 1, target - arr[idx], arr, dp);
    int notTake = solveMemo(idx - 1, target, arr, dp);
    
    return dp[idx][target] = take + notTake;
}

// Tabulation template (0/1 Knapsack)
int knapsack(vector<int>& wt, vector<int>& val, int W) {
    int n = wt.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            dp[i][w] = dp[i-1][w]; // not take
            
            if (w >= wt[i-1]) {
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - wt[i-1]] + val[i-1]);
            }
        }
    }
    return dp[n][W];
}

// LIS (Longest Increasing Subsequence)
int lengthOfLIS(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}

// LCS (Longest Common Subsequence)
int longestCommonSubsequence(string s1, string s2) {
    int m = s1.size(), n = s2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i-1] == s2[j-1])
                dp[i][j] = 1 + dp[i-1][j-1];
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[m][n];
}
```

### LeetCode Problems (25–30):

**Easy:**
1. [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
2. [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
3. [House Robber](https://leetcode.com/problems/house-robber/)
4. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

**Medium:**
5. [House Robber II](https://leetcode.com/problems/house-robber-ii/)
6. [Coin Change](https://leetcode.com/problems/coin-change/)
7. [Coin Change II](https://leetcode.com/problems/coin-change-ii/)
8. [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
9. [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
10. [Unique Paths](https://leetcode.com/problems/unique-paths/)
11. [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
12. [Jump Game](https://leetcode.com/problems/jump-game/)
13. [Decode Ways](https://leetcode.com/problems/decode-ways/)
14. [Word Break](https://leetcode.com/problems/word-break/)
15. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
16. [Target Sum](https://leetcode.com/problems/target-sum/)
17. [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
18. [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
19. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
20. [Triangle](https://leetcode.com/problems/triangle/)
21. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)

**Hard:**
22. [Edit Distance](https://leetcode.com/problems/edit-distance/)
23. [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)
24. [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
25. [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)
26. [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
27. [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
28. [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
29. [Burst Balloons](https://leetcode.com/problems/burst-balloons/)
30. [Interleaving String](https://leetcode.com/problems/interleaving-string/)

### Patterns Learned:
✓ State + transition identification  
✓ Overlapping subproblems  
✓ Memoization vs tabulation  
✓ Space optimization (1D DP)  
✓ Knapsack variations  
✓ Sequence DP (LIS, LCS)  
✓ Grid DP  
✓ State machine DP  

---

## 🎯 Weekly Assessment Schedule

**Week 1 (Day 7):** Arrays, Strings, Hashing, Stack  
- 2-hour timed contest (4 problems: 1 easy, 2 medium, 1 hard)  
- 1-hour review and pattern documentation

**Week 2 (Day 14):** All topics up to Linked List  
- 2-hour timed contest  
- Focus on pointer manipulation and recursion

**Week 3 (Day 21):** All topics up to Graphs  
- 2.5-hour timed contest  
- Heavy emphasis on trees and graphs

**Week 4 (Day 28):** All topics  
- 3-hour full mock interview  
- Solve 5 problems covering all topics

**Final Days (29–30):** Full revision + 2 complete contest simulations

---

## 🔧 C++ Template File Structure

Create a `template.cpp` with:

```cpp
#include <bits/stdc++.h>
using namespace std;

// Fast I/O
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);

// Type aliases
#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()

// Debug macro
#define debug(x) cerr << #x << " = " << x << endl;

// Constants
const int MOD = 1e9 + 7;
const int INF = 1e9;

// Utility functions
template<typename T>
void print(vector<T>& v) {
    for (auto x : v) cout << x << " ";
    cout << "\n";
}

int main() {
    fast_io;
    
    // Your code here
    
    return 0;
}
```

---

## ✅ Success Metrics

By Day 30, you should:
- ✓ Solve medium problems in 25–40 minutes
- ✓ Recognize patterns within 2–3 minutes
- ✓ Implement 15+ standard templates from memory
- ✓ Explain any solution in 2–3 minutes
- ✓ Complete 180+ LeetCode problems
- ✓ Handle 90% of interview questions confidently

---

## 💡 Pro Tips

1. **Timebox everything** — Don't spend >40 min on medium problems during practice
2. **Redo mistakes** — Reschedule failed problems within 48 hours
3. **Build a cheat-sheet** — 1-page summary of all patterns and templates
4. **Mock interviews** — Practice explaining solutions verbally
5. **Sleep & breaks** — 10–12 hrs/day is intense; take 10-min breaks every 90 min
6. **Track metrics** — Maintain a spreadsheet: problems solved, time taken, success rate
7. **Contest participation** — Join weekly LeetCode contests for speed building

---

## 🚀 Resources

- **Theory:** CP-algorithms, GeeksforGeeks, Striver's SDE Sheet
- **Practice:** LeetCode, Codeforces (Div2 A/B), AtCoder
- **Videos:** NeetCode, take U forward (Striver)
- **Books:** *Competitive Programming 3* by Steven Halim

---

**Good luck! 🔥 This is hardcore, but you'll emerge as a DSA beast!**