# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :
class myStack:
    # Please read sample.java file before starting.
    # Kindly include Time and Space complexity at top of each file
    def __init__(self):
        self.arr=[]
    def isEmpty(self):
        if self.arr:
            return 0
        else:
            return 1
    def push(self, item):
        self.arr.append(item)
    def pop(self):
        if self.isEmpty() == 0:
            #self.arr.pop()
            pop= self.arr[-1]
            self.arr.remove(pop)
            return pop
        else:
            print("stack is empty")
    def peek(self):
        return self.arr[-1]
    def size(self):
        return len(self.arr)
    def show(self):
        print(self.arr)

s = myStack()
s.push('1')
s.push('2')
s.push('3')
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.show())