def get_permutation(s):
    def generate(chars, result, start):
        if start == len(chars):
            result.append("".join(chars))

        for idx in range(start, len(chars)):
            l, r = start, idx
            chars[l], chars[r] = chars[r], chars[l]
            generate(chars, result, start+1)
            chars[l], chars[r] = chars[r], chars[l]

    result = []
    generate(list(s), result, 0)
    return result