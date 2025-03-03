import sys
from typing import Tuple, List


def is_avl_tree(left: int, right: int, array: List[Tuple[int, ...]], origin: int) -> Tuple[int, bool]:
    current_tree_height = 0
    current_tree_is_avl = False

    if abs(right - left) < 2:
        if abs(right - left) != 0:
            if array[left][0] == array[left][1] == -1:
                current_tree_is_avl = True
            else:
                current_tree_is_avl = False
        else:
            current_tree_is_avl = True
        return current_tree_height, current_tree_is_avl

    index = left

    while index < right:
        if array[index][0] < origin < array[index][1]:
            left_tree_height, left_tree_is_avl = is_avl_tree(left=left, right=index, array=array,
                                                             origin=array[index][0])
            right_tree_height, right_tree_is_avl = is_avl_tree(left=index + 1, right=right, array=array,
                                                               origin=array[index][1])

            if abs(right_tree_height - left_tree_height) < 2 and left_tree_is_avl and right_tree_is_avl:
                current_tree_is_avl = True
            else:
                current_tree_is_avl = False

            current_tree_height = max(left_tree_height, right_tree_height)

            return current_tree_height + 1, current_tree_is_avl

        index += 1

    return current_tree_height, current_tree_is_avl


n, root = tuple(map(int, sys.stdin.readline().split()))

children = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

tree_height, tree_is_avl = is_avl_tree(left=0, right=n, array=children, origin=root)

print(int(tree_is_avl))
