"""
Set of functions for palindrome checking
"""

def is_palindrome(string):
    """
    Determines whether a string is a palindrome. An assertion is first made to verify if the input is valid.
    The string is checked against the reverse of itself and if both strings are equal, the input string is deemed
    a palindrome.

    :param string: The string to check
    :return: True if the string is a palindrome. Otherwise, False
    """
    assert (isinstance(string, str) is True)
    return string == string[::-1]


def get_longest_palindrome(string):
    """
    Returns the longest substring that is a palindrome. All substrings of the main string is first generated.
    We iterate over these substrings and check if it is longer than the current longest substring and
    if it is a palindrome. If both conditions are satisfied, the substring replaces the current longest substring.

    :param string: The string to check
    :return: The longest substring that is a palindrome
    """
    combo = _subsets(string)
    longest = ''
    for word in combo:
        if len(word) > len(longest) and is_palindrome(word):
            longest = word
    return longest


def get_minimum_palindrome_cut(string):
    """
    Returns the minimum number of cuts needed such that all substrings will be a palindrome.
    All substrings are generated and are sorted by length in descending order to ensure that the maximum length
    palindrome substrings are first checked. We iterate over these substrings and check if is a palindrome and is found
    in the current parent string. If both conditions are satisfied, a counter for substring is increment and we remove
    the substring from the parent string. The minimum cut will be one less than the number of substrings found.

    :param string: The string to check
    :return: The number of cuts needed such that all substrings will be a palindrome
    """
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
