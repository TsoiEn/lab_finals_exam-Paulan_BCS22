class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def vertical_order_traversal(root):
    if not root:
        return []
    vertical_order = {}

    queue = [(root, 0)]

    while queue:
        node, distance = queue.pop(0)

        if distance in vertical_order:
            vertical_order[distance].append(node.data)
        else:
            vertical_order[distance] = [node.data]

        if node.left:
            queue.append((node.left, distance - 1))

        if node.right:
            queue.append((node.right, distance + 1))

    sorted_distances = sorted(vertical_order.keys())

    result = []
    for distance in sorted_distances:
        result.extend(vertical_order[distance])

    return result

# to revese the output
def reverse_list(input_list):
    start, end = 0, len(input_list) - 1
    
    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1
    
    return input_list


def print_vertical_order(output_list):
    for val in output_list:
        print(f"{val:^3}", end=" ")
    print()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)

result = vertical_order_traversal(root)
reversed_result = reverse_list(result)
print_vertical_order(reversed_result)