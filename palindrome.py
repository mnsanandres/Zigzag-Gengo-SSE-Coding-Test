def is_palindrome(string):
    assert (isinstance(string, str) is True)
    return string == string[::-1]


def get_longest_palindrome(string):
    combo = _subsets(string)
    longest = ''
    for word in combo:
        if len(word) > len(longest) and is_palindrome(word):
            longest = word
    return longest


def get_minimum_palindrome_cut(string):
    current = string
    combo = _subsets(string)
    combo = sorted(combo, key=lambda x: len(x))[::-1]
    parts = 0
    for sub in combo:
        if is_palindrome(sub) and sub in current:
            # print(sub)
            parts += 1
            current = current.replace(sub, '')
        if not current:
            break
    return parts - 1


def _subsets(string):
    return [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


if __name__ == '__main__':
    assert (is_palindrome('a') is True)
    assert (is_palindrome('ab') is False)
    assert (is_palindrome('abba') is True)
    assert (is_palindrome('madamimeve') is False)
    assert (get_longest_palindrome('abaxyzzyxf') == 'xyzzyx')
    assert (get_minimum_palindrome_cut('noonabbad') == 2)
