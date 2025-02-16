n = int(input())
origin_word = str(input())


def make_palindrome(word: str) -> str:
    chars = [[chr(65 + i), 0] for i in range(26)]
    for char in word:
        chars[ord(char)-65][1] += 1
    chars = [char for char in chars if char[1] != 0]

    middle_index = len(chars) - 1
    extra_char = None
    i = len(chars) - 1
    while i >= 0:
        if chars[i][1] % 2 == 1:
            if chars[i][1] > 1:
                chars[i][1] -= 1
                extra_char = chars[i][0]
                middle_index = len(chars)
            else:
                middle_index = i
        i -= 1
    if extra_char is not None:
        chars.append([extra_char, 1])
    middle = chars[middle_index][0] * chars[middle_index][1]
    tail = ""
    for i in range(len(chars)):
        if i == middle_index:
            continue
        tail += chars[i][0] * (chars[i][1]//2)
    return tail + middle + tail[::-1]


print(make_palindrome(word=origin_word))
