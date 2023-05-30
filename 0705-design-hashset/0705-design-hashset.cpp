class Node{
public:
    Node* next;
    int val;

    Node(int value){
        next = nullptr;
        val = value;
    }
};
#define seed 10001
class MyHashSet {
public:
    
    Node* myset[seed];
    
    MyHashSet() {
        for (int i = 0; i < seed; i++){
            myset[i] = nullptr;
        }
    }
    
    void add(int key) {
        if (contains(key)){
            return;
        }
        Node* newNode = new Node(key);
        int hashkey = key % seed;
        if (myset[hashkey] != nullptr){
            newNode->next = myset[hashkey];
        }
        myset[hashkey] = newNode;
    }
    
    void remove(int key) {
        int hashkey = key % seed;
        Node* curPtr = myset[hashkey];
        Node* prevPtr = myset[hashkey];
        while(curPtr != nullptr){
            if (curPtr->val == key){
                if (prevPtr == curPtr){
                    myset[hashkey] = curPtr->next;
                }
                else{
                    prevPtr->next = curPtr->next;
                }
            }
            prevPtr = curPtr;
            curPtr = curPtr->next;
        }
        
    }
    
    bool contains(int key) {
        int hashkey = key % seed;
        Node* curPtr = myset[hashkey];
        while(curPtr != nullptr){
            if (curPtr->val == key){
                return true;
            }
            curPtr = curPtr->next;
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */