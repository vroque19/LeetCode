from collections import defaultdict


def longest_substring_without_repeats(s: str):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    l, r = 0, 1
    freq_map = defaultdict(lambda: -1)
    print(freq_map)
    # return
    freq_map[s[l]] = l
    largest_length = 1
    # ## aabcacd
    # ##      lr
    while r < len(s):
        if freq_map[s[r]] != -1:
            for i in range(l, freq_map[s[r]]):
                freq_map[s[i]] = -1
            print(l, freq_map[s[r]])
            l = freq_map[s[r]] + 1
            freq_map[s[l]] = l
        freq_map[s[r]] = r
        r += 1
        largest_length = max(largest_length, r - l)  # ll = 3

    print(r, l, largest_length)
    return largest_length


res = longest_substring_without_repeats("aabcabd")
print(res)
