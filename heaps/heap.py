"""
Implementation of a min heap:
- insert() - Time complexity: O(log n)
- remove_min() - Time complexity: O(log n)
- get_min() - Time complexity: O(1)
- heapify() - Time complexity: O(n log n) and O(n) solution
"""

class minHeap:
    def __init__(self):
        self.data = []
    
    def get_min(self):
        return self.data[0] if len(self.data) else "No data inserted yet!"
    
    def sift_up(self, idx):
        child_idx = idx
        parent_idx = (child_idx - 1)//2

        # go as long as parents index is greater than or equal to zero
        while parent_idx >= 0 and self.data[child_idx] < self.data[parent_idx]:
            self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2
    
    def sift_down(self, idx):
        parent_idx = idx
        left_child_idx = (parent_idx * 2) + 1
        right_child_idx = (parent_idx * 2) + 2

        # sift down
        while left_child_idx < len(self.data) or right_child_idx < len(self.data):

            # parent have both left and right child - consider the smallest
            if left_child_idx < len(self.data) and right_child_idx < len(self.data):
                consider = (left_child_idx
                            if self.data[left_child_idx] < self.data[right_child_idx]
                                else right_child_idx)
                
            # parent has only a left child
            elif left_child_idx:
                consider = left_child_idx
            
            else:
                consider = right_child_idx

            if self.data[parent_idx] < self.data[consider]:
                # found its place
                break

            else:
                self.data[consider], self.data[parent_idx] = self.data[parent_idx], self.data[consider]

                # update
                parent_idx = consider
                left_child_idx = (consider * 2) + 1
                right_child_idx = (consider * 2) + 2

    def insert(self, value):
        """
        Time Complexity: Log(n) - sift up height of the tree
        Inserts value in heap maintaining its min property
        The idea is to append to the last position sift up. 
        As long as parent is parent is lesser, swap their values

        Facts: parent index from child: child_index - 1 // 2

        eg. For the heap
                2
            3       5 

        Inserting 1 :
        * append at last position
                2
            3       5
        1

        * sift up
        (i)                     (ii)        
                2                           1
            1       5                   2       5
        3                           3

        """
        self.data.append(value)
        self.sift_up(len(self.data) - 1)

    def remove_min(self):
        """
        Time: Log(n)
        eg. remove
    
                     0                  4              1
                 1       2    =>    1       2  =>   4      2
             4
        """
        # removes the minimum element
        if not self.data:
            return "No data inserted yet"
        min_value = self.get_min()
        if len(self.data) == 1:
            self.data.pop()
            return min_value
        else:
            # swap last with first 
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            # remove last value
            self.data.pop()
            # sift down new root
            self.sift_down(0)

    def sub_optimal_heapify(self, values):
        """
        The william's method
        start with an empty heap and insert n elements one after the other
        time: O(nlogn), insertion takes logn

        [4,3,1,2,5] -> [1,2,3,4,5]

        In diagram
                             1
                         2      3
                    4      5
        """
        self.data = []
        for val in values:
            self.insert(val)
        return self.data
    
    def optimal_heapify(self, values):
        """
        Full explanation: 
        (1) https://www.wikiwand.com/en/Binary_heap#Building_a_heap
        (2) https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        
        Summary:
        The idea is to apply sift down on each node starting from the bottom layer. 
        It will take 0 operations to siftdown n/2 nodes at the bottom
        It will take (h = log n - height of tree) operations to siftdown 1 node (the root)

        The total time taken:
            (0 * n/2) + (1 * n/4) + (2 * n/8) + ... + (h * 1)
        The finite series above is not more than the infinite series which converges at N

        So time complexity is O(N)
        """
        self.data = values
        for i in range(len(values)-1, -1, -1):
            self.sift_down(i)
        print(self.data)


# Testing
myHeap = minHeap()
print(myHeap.get_min())

# insert elements in right order
# myHeap.insert(1)
# myHeap.insert(2)
# myHeap.insert(3)
# myHeap.insert(4)

# print(myHeap.get_min())

# switch order of elements
myHeap.insert(4)
myHeap.insert(2)
myHeap.insert(1)
myHeap.insert(0)

print(myHeap.get_min())

# remove 0
myHeap.remove_min()
print(myHeap.get_min())

# remove 1
myHeap.remove_min()
print(myHeap.get_min())

# sub optimal heapify
print(myHeap.sub_optimal_heapify([4,3,1,2,5]))

# optimal heapify
print(myHeap.sub_optimal_heapify([4,3,1,2,5]))

