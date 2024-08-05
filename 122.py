import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        
        
    def __find(self, node, parent, value):
        if node == None:
            return None, parent, False
        
        if value == node.data:
            return node, parent, True
        
        if value < node.data:
            if node.left:
                return self.__find(node.left, parent, value)
            
        if value > node.data:
            if node.right:
                return self.__find(node.right, parent, value)
        
        return node, parent, False


    def append(self, obj):
        if self.root == None:
            self.root = obj
            return obj
        
        s, p, fl_node = self.__find(self.root, None, obj.data)
        
        if s and not fl_node:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
            
        return obj
    
    
    def find_max_2(self):
        node = self.root
        parent = None
        
        while node.right:
            parent = node
            node = node.right
            
        if node.left:
            node = node.left
            while node.right:
                node = node.right
            return node.data
        
        if parent:
            return parent.data
        

def main():
    v = list(map(int, input().split()))
    t = Tree()
    for i in v[0:-1]:
        t.append(Node(i))
        
    m = t.find_max_2()
    print(m)


if __name__ == '__main__':
    main()