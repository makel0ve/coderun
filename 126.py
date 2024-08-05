import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
class Tree:
    def __init__(self):
        self.root = None
        self.mat = []
        
        
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
        
        
    def show_wolf_parent(self, node):
        if node == None:
            return
        
        self.show_wolf_parent(node.left)
        if (node.left != None and node.right == None) or (node.left == None and node.right != None):
            self.mat.append(node.data)
        self.show_wolf_parent(node.right)
        
        return self.mat
        
def main():
    v = list(map(int, input().split()))
    t = Tree()
    for i in v[0:-1]:
        t.append(Node(i))
        
    s = t.show_wolf_parent(t.root)
    return "\n".join(map(str, s))
    
if __name__ == '__main__':
    print(main())