import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.lvl = 0


class Tree:
    def __init__(self):
        self.root = None
        self.mat = []
        
    
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
        if self.root == None:
            obj.lvl = 1
            self.root = obj
            self.mat.append(obj.lvl)
            return obj
        
        s, p, fl_node = self.__find(self.root, None, obj.data)
        
        if s and not fl_node:
            obj.lvl = s.lvl + 1
            self.mat.append(obj.lvl)
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        
        return obj
    
    
    def print_ans(self):
        return ' '.join(map(str, self.mat))
    
        
def main():
    v = list(map(int, input().split()))
    t = Tree()
    for i in v[0:-1]:
        t.append(Node(i))

    return t.print_ans()

if __name__ == '__main__':
    print(main())