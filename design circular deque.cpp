class MyCircularDeque {
public:
  /** Initialize your data structure here. Set the size of the deque to be k. */
  MyCircularDeque(int k): k_(k), q_(k), head_(1), tail_(-1), size_(0) {}
 
  /** Adds an item at the front of Deque. Return true if the operation is successful. */
  bool insertFront(int value) {
    if (isFull()) return false;
    head_ = (head_ - 1 + k_) % k_;
    q_[head_] = value;
    if (size_ == 0) tail_ = head_;
    ++size_;
    return true;
  }
 
  /** Adds an item at the rear of Deque. Return true if the operation is successful. */
  bool insertLast(int value) {
    if (isFull()) return false;
    tail_ = (tail_ + 1 + k_) % k_;
    q_[tail_] = value;
    if (size_ == 0) head_ = tail_;
    ++size_;
    return true;  
  }
 
  /** Deletes an item from the front of Deque. Return true if the operation is successful. */
  bool deleteFront() {
    if (isEmpty()) return false;
    head_ = (head_ + 1 + k_) % k_;
    --size_;
    return true;
  }
 
  /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
  bool deleteLast() {
    if (isEmpty()) return false;
    tail_ = (tail_ - 1 + k_) % k_;
    --size_;
    return true;
  }
 
  /** Get the front item from the deque. */
  int getFront() {
    if (isEmpty()) return -1;
    return q_[head_];
  }
 
  /** Get the last item from the deque. */
  int getRear() {
    if (isEmpty()) return -1;
    return q_[tail_];
  }
 
  /** Checks whether the circular deque is empty or not. */
  bool isEmpty() {
    return size_ == 0;
  }
 
  /** Checks whether the circular deque is full or not. */
  bool isFull() {
    return size_ == k_;
  }
private:
  const int k_;
  int head_;
  int tail_;
  int size_;
  vector<int> q_;
};
