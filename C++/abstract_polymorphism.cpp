#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
using namespace std;

struct Node{
   Node* next;
   Node* prev;
   int value;
   int key;
   Node(Node* p, Node* n, int k, int val):prev(p),next(n),key(k),value(val){};
   Node(int k, int val):prev(NULL),next(NULL),key(k),value(val){};
};

class Cache{
   
   protected: 
   map<int,Node*> mp; //map the key to the node in the linked list
   int cp;  //capacity
   Node* tail; // double linked list tail pointer
   Node* head; // double linked list head pointer
   virtual void set(int, int) = 0; //set function
   virtual int get(int) = 0; //get function
};

class LRUCache : public Cache {
  public:
    LRUCache(int capacity){
        cp = capacity;
    }
    void set(int a, int b){
        
        Node* p = new Node(a,b);
        
        if (mp.size() == 0){
            head = p;
            tail = p;
            mp[a] = p; 
            return;
        }
        
        auto it = mp.find(a);
        
        if (it != mp.end()){
            
            if (mp.size() == 1){
              mp[a] = p;
              head = p;
              tail = p;
              return;
            }

            Node* p1 = it->second;
            
            if (p1 == head){
                head = p1->next;
                head->prev = NULL;
            }
            else if (p1 == tail) {

                tail = p1->prev;
                tail->next = NULL;
            }
            else{
                Node * n1 = p1->prev;
                Node * n2 = p1->next;
                n1->next = n2;
                n2->prev = n1;
            }

            mp.erase(it);
            
        }
        
        if (mp.size() >= cp){
            Node* p1 = tail->prev;
            tail = p1;
            tail->next = NULL;
        }
      

        mp[a] = p; 
        
        p->next = head;
        head->prev = p;
        head = p;

    }
    
    int get(int a){
         auto it = mp.find(a);
         if (it != mp.end()){
            return mp[a]->value;
         }
         else return -1;
    }

    // void debug(){
      
    //   cout << "head: " << head << "    tail: " << tail << endl;
    //   Node* p = head;
    //   while (p != NULL){
    //      cout << p->prev << "----->" << p << ':' << p->next << ':' << p->key << '\n';
    //      p = p->next;
    //   } 
      
      
    //   printf("\n");
    // }
};

int main(){
   int n, capacity,i;
   cin >> n >> capacity;
   LRUCache l(capacity);
   for(i=0;i<n;i++) {
      string command;
      cin >> command;
      if(command == "get") {
         int key;
         cin >> key;
         cout << l.get(key) << endl;
      } 
      else if(command == "set") {
         int key, value;
         cin >> key >> value;
         l.set(key,value);
      }
   }


   return 0;

}