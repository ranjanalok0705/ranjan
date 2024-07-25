from collections import Counter
from collections import defaultdict


def minWindow(s, t):
    if not s or not t or len(t) > len(s):
        return "No"
    t_count = Counter(t)
    matches = l = r = 0
    required = len(t_count)
    window_count = defaultdict(int)
    ans = (float("inf"), 0, 0)
    while r < len(s):
        curr_char = s[r]
        window_count[curr_char] += 1

        if curr_char in t_count and window_count[curr_char] == t_count[curr_char]:
            matches += 1

        while l <= r and matches == required:

            to_remove = s[l]

            if r-l+1 < ans[0]:
                ans = (r-l+1, l, r)

            window_count[to_remove] -= 1
            if to_remove in t_count and window_count[to_remove] < t_count[to_remove]:
                matches -= 1

            l += 1

        r += 1

    return s[ans[1]:ans[2]+1] if ans[0] != float("inf") else ""


s = input()
t = input()
a = minWindow(s, t)
print(a)
# i
