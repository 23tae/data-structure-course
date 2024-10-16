class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder(node: TreeNode):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)


def preorder(node: TreeNode):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


def postorder(node: TreeNode):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=' ')


def count_node(node: TreeNode):
    if node is None:
        return 0
    return 1 + count_node(node.left) + count_node(node.right)


def count_leaf(node: TreeNode):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    else:
        return count_leaf(node.left) + count_leaf(node.right)


def calc_height(node: TreeNode):
    if node is None:
        return 0
    left_height = calc_height(node.left)
    right_height = calc_height(node.right)
    if (left_height > right_height):
        return left_height + 1
    else:
        return right_height + 1


# 노드 생성
# Level 4 (말단 노드)
n15 = TreeNode('31')
n14 = TreeNode('30')
n13 = TreeNode('29')
n12 = TreeNode('28')
n11 = TreeNode('27')
n10 = TreeNode('26')
n9 = TreeNode('25')
n8 = TreeNode('24')
n7 = TreeNode('23')
n6 = TreeNode('22')
n5 = TreeNode('21')
n4 = TreeNode('20')
n3 = TreeNode('19')
n2 = TreeNode('18')
n1 = TreeNode('17')
n0 = TreeNode('16')

# Level 3
n7_3 = TreeNode('15', n14, n15)
n6_3 = TreeNode('14', n12, n13)
n5_3 = TreeNode('13', n10, n11)
n4_3 = TreeNode('12', n8, n9)
n3_3 = TreeNode('11', n6, n7)
n2_3 = TreeNode('10', n4, n5)
n1_3 = TreeNode('9',  n2, n3)
n0_3 = TreeNode('8',  n0, n1)

# Level 2
n3_2 = TreeNode('7', n6_3, n7_3)
n2_2 = TreeNode('6', n4_3, n5_3)
n1_2 = TreeNode('5', n2_3, n3_3)
n0_2 = TreeNode('4', n0_3, n1_3)

# Level 1
n1_1 = TreeNode('3', n2_2, n3_2)
n0_1 = TreeNode('2', n0_2, n1_2)

# Root node (Level 0)
root = TreeNode('1', n0_1, n1_1)
print('In-Order: ', end='')
inorder(root)
print('\nPre-Order: ', end='')
preorder(root)
print('\nPost-Order: ', end='')
postorder(root)
print()

print("노드의 개수: %d개" % count_node(root))
print("단말의 개수: %d개" % count_leaf(root))
print("트리의 높이: %d개" % calc_height(root))
