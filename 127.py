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


    def is_balanced(self, node):
        if node is None:
            return 0, True
        
        left_height, left_balanced = self.is_balanced(node.left)
        right_height, right_balanced = self.is_balanced(node.right)
        
        current_height = max(left_height, right_height) + 1
        height_diff = abs(left_height - right_height)
        current_balanced = height_diff <= 1
        
        return current_height, left_balanced and right_balanced and current_balanced


def main():
    v = list(map(int, input().split()))
    t = Tree()
    for i in v[0:-1]:
        t.append(Node(i))
    
    s = t.is_balanced(t.root)
    if s[1]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    print(main())