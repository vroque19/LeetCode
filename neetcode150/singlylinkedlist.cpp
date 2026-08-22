#include <vector>
#include <iostream>
using namespace std;

class SinglyLinkedList {
  private:
    struct Node {
      int val;
      Node* next;
      Node(int v): val(v), next(nullptr) {}

    };
    Node* dummy;
    Node* tail;
    void print_vals(vector<int> vals) {
      cout << "linked list vals: ";
      for(auto v: vals) {
        cout << v << "  ";
      }
      cout << endl;
    }

  public:
    SinglyLinkedList() {
      dummy = new Node(-1); // points to start of the list
      tail = dummy;
    }

    vector<int> getVals() {
      vector<int> vals;
      Node* curr = dummy->next;
      while(curr) {
        vals.push_back(curr->val);
        curr = curr->next;
      }
      print_vals(vals);
      return vals;
    }

    int getHead() {
      if(dummy->next == nullptr) {
        return -1;
      }
      cout << dummy->next->val << endl;
      return dummy->next->val;
    }

    int getTail() {
      return tail->val;
    }

    void reverse() {
      if(!dummy) {
        cout << "No list to reverse\n";
        return;
      }
      Node* prev = nullptr;
      Node* curr = dummy->next;

      tail = curr;
      while(curr) {
        Node* next = curr->next;
        curr->next = prev;
        prev = curr; // prev is new head
        curr = next; // increment current
      }
      dummy->next = prev; // dummy must point to prev
    }
    

    void insertHead(int val) {
      // get the first node
      Node* new_head = new Node(val);
      Node* curr = dummy->next;
      dummy->next = new_head;
      new_head->next = curr;
      // if the tail is the dummy, make new head the tail
      if(dummy == tail) {
        tail = new_head;
      }
    }

    void insertTail(int val) {
      // get the curr tail and have
      // tail->next point to new tail
      Node* new_tail = new Node(val);
      tail->next = new_tail;
      tail = new_tail;
    }

    bool removeNode(int idx) {
      if(idx<0) { return false; }
      if(dummy == nullptr) {
        cout << "cant remove from empty list" << endl;
        return false;
      }
      Node* prev = dummy;
      Node* curr = dummy->next;
      int i = 0;
      while(i < idx && curr) {
        prev = prev->next;
        curr = curr->next;
        i++;
      }
      if(!curr) {
        // index out of range
        cout << "out of range" << endl;
        return false;
      }
      prev->next = curr->next;
      if(curr == tail) {
        tail = prev;
      }
      delete curr;
      return true;
    }
    bool insertNode(int idx, int val) {
      if(idx < 0) {
        return false;
      }
      Node* new_node = new Node(val);
      Node* prev = dummy;
      Node* curr = dummy->next;
      int i = 0;

      while(i < idx && curr) {
        curr = curr->next;
        prev = prev->next;
        i++;
      }
      if(i < idx) {
        cout << "index out of range" << endl;
        return false;
      }
      if(!curr) {
        insertTail(val);
      }
      prev->next = new_node;
      new_node->next = curr;
      // cant insert at node after tail->next
      return true;
    }

    int get(int idx) {
      Node* curr = dummy;
      int i = 0;
      while(i <= idx && curr) {
        curr = curr->next;
        i++;
      }
      if(!curr) {
        cout << "index out of range of this list" << endl;
        return -1;
      }
      cout << "Got val: " << curr->val << " at " << idx << endl;
      return curr->val;

    }

    ~SinglyLinkedList() {
      Node* curr = dummy;
      while(curr) {
        Node* next = curr->next;
        delete curr;
        curr = next;
      }
    }
};


int main() {
  SinglyLinkedList mylist;
  // mylist.getVals();
  mylist.insertHead(2);
  int head = mylist.getHead();
  mylist.getVals();
  mylist.insertTail(8);
  mylist.insertNode(8, 9);
  mylist.insertNode(0, 1);
  mylist.insertNode(0, 4);
  mylist.insertNode(0, 9);
  mylist.getVals();
  mylist.getHead();  
  int val = mylist.get(1);
  mylist.get(0);
  mylist.get(4);
  mylist.get(5);
  mylist.getVals();
  mylist.reverse();
  mylist.getVals();
  return 0;
}
