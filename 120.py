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
        if node is None:
            return None, parent, False
        
        if value == node.data:
            return node, parent, True
        
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
            
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        
        return node, parent, False
    
    
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        
        s, p, fl_node = self.__find(self.root, None, obj.data)
        
        if s and not fl_node:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        
        return obj
    
    
    def depth(self, node):
        if node == None:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        
        if left > right:
            return left + 1
        else:
            return right + 1


def main():
    v = list(map(int, input().split()))
    t = Tree()
    for i in v[0:-1]:
        t.append(Node(i))
    
    print(t.depth(t.root))


if __name__ == '__main__':
    main()