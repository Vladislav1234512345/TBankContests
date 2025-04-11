import sys
from typing import List


n, r = map(int, sys.stdin.readline().split())

tree = []

for i in range(n):
    tree.append(list(map(int, sys.stdin.readline().split())))


def check_balance(node):
    if node == -1:
        return 0  # Высота пустого дерева равна 0

    # Рекурсивно проверяем левое и правое поддеревья
    left_height = check_balance(tree[node][0])
    if left_height == -1:  # Если левое поддерево уже не сбалансировано
        return -1

    right_height = check_balance(tree[node][1])
    if right_height == -1:  # Если правое поддерево уже не сбалансировано
        return -1

    # Проверяем баланс текущего узла
    if abs(left_height - right_height) > 1:
        return -1  # Дерево не сбалансировано

    # Возвращаем высоту текущего узла
    return max(left_height, right_height) + 1


# Проверяем, является ли дерево AVL
if check_balance(r) != -1:
    print(1)
else:
    print(0)
