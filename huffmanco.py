coded = " "
class Node:
    def __init__(self, data, arr):
        self.data = data
        self.arr = arr
        self.left = None
        self.right = None


def huffman(data, arr):
    nodes = [Node(data[i], arr[i]) for i in range(len(arr))]
    
    while len(nodes) > 1:

        nodes = sorted(nodes, key=lambda x: x.arr)
        
        left = nodes[0]
        right = nodes[1]

        temp = Node('', left.arr + right.arr)
        temp.left = left
        temp.right = right

        nodes = nodes[2:]
        nodes.append(temp)
    
    return nodes[0]


def print_codes(node, code=''):
    global coded
    if node is not None:
        # print("the first code is : " , code)
        if node.data != '':
            print(f'{node.data}: {code}')
            coded +=code
        print_codes(node.right, code +'1')        
        print_codes(node.left, code + '0')


data = list(map(chr, range(97, 123)))
arr = list(map(float, input("Enter input separated by spaces: ").split()))
root = huffman(data, arr)
print_codes(root)
print(coded)
