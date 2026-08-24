/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    vector<int> toList(ListNode* h) {
        vector<int> li;
        ListNode* node = h;
        while(node) {
            cout << node->val;
            li.push_back(node->val);
            node = node->next;
        }
        return li;
    }
public:
    ListNode* middleNode(ListNode* head) {
        vector<int> arr = toList(head);
        if(size(arr) == 1) {
            return head;
        }
        ListNode* res = head;
        int p1 = 0;
        int p2 = size(arr) - 1;
        while(p1 <= p2) {
            p1++;
            p2--;
        }
        for(int i = 0; i <= p2; i++) {
            res = res->next;
        }
        return res;
    }
};
