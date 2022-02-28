hash_map = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y'],
    0: ['z']
}


def back_tracking(inp, idx, val):
    num = inp[idx]
    chars = hash_map[num]
    for c in chars:
        back_tracking(inp, idx + 1,val + c)

