import sys


def is_avl_tree(node: int, tree):
    if node == -1:
        return True, 0

    left_child, left_height = is_avl_tree(node=tree[node][0], tree=tree)
    right_child, right_height = is_avl_tree(node=tree[node][1], tree=tree)

    if not left_child or not right_child:
        return False, 0

    if left_height > right_height + 1 or right_height > left_height + 1:
        return False, 0

    current_height = max(left_height, right_height) + 1
    return True, current_height


n, r = map(int, sys.stdin.readline().split())
current_tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

is_avl, _ = is_avl_tree(node=r, tree=current_tree)
print(is_avl)
