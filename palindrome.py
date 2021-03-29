"""
Set of functions for palindrome checking

Usage:
```
    palindrome.py -i <input string> [-v] [-l] [-c]
    -h, --help      show this help message and exit
    -i, --input     input string
    -v, --valid     check if valid palindrome
    -l, --longest   get longest palindrome substring
    -c, --cut       get the minimum number of palindrome substring cuts
```
Example:
```
    >>> palindrome.py -i noonabbad -v -l -c
    palindrome: False
    longest palindrome: noon
    minimum palindrome cut: 2
```
"""
import getopt
import sys


def is_palindrome(string):
    """
    Determines whether a string is a palindrome. An assertion is first made to verify if the input is valid.
    The string is checked against the reverse of itself and if both strings are equal, the input string is deemed
    a palindrome.

    Time and space complexity: Revering the original list is at most `O(n)`

    :param string: The string to check
    :return: `True` if the string is a palindrome. Otherwise, `False`
    """
    assert (isinstance(string, str) is True)
    return string == string[::-1]


def get_longest_palindrome(string):
    """
    Returns the longest substring that is a palindrome. All substrings of the main string is first generated.
    We iterate over these substrings and check if it is longer than the current longest substring and
    if it is a palindrome. If both conditions are satisfied, the substring replaces the current longest substring.

    Time and space complexity: `O(n!)` since we are retrieving all the substring combinations of the parent string

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
    palindrome substrings are first checked. We iterate over these substrings and check if it is a palindrome and is
    found in the current parent string. If both conditions are satisfied, a counter for substring is incremented and we
    remove the substring from the parent string. The minimum cut will be one less than the number of substrings found.

    Time and space complexity: `O(n!)` since we are retrieving all the substring combinations of the parent string

    :param string: The string to check
    :return: The number of cuts needed such that all substrings will be a palindrome
    """
    current = string
    combo = _subsets(string)
    combo = sorted(combo, key=lambda x: len(x))[::-1]
    parts = 0
    for sub in combo:
        if is_palindrome(sub) and sub in current:
            while sub in current:
                parts += 1
                current = current.replace(sub, '', 1)
        if not current:
            break
    return parts - 1


def _subsets(string):
    return [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


def _main(argv):
    help_text = '''palindrome.py -i <input string> [-v] [-l] [-c]
    -h, --help      show this help message and exit
    -i, --input     input string
    -v, --valid     check if valid palindrome
    -l, --longest   get longest palindrome substring
    -c, --cut       get the minimum number of palindrome substring cuts'''
    try:
        opts, args = getopt.getopt(argv, "hi:vlc", ["input=", "valid", "longest", "cut"])
    except getopt.GetoptError:
        print('palindrome.py -i <input string> [-v] [-l] [-c]')
        sys.exit(2)
    input_string = ''
    ops = []
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-i", "--input"):
            input_string = arg
        elif opt in ("-v", "--valid"):
            ops.append(is_palindrome)
        elif opt in ("-l", "--longest"):
            ops.append(get_longest_palindrome)
        elif opt in ("-c", "--cut"):
            ops.append(get_minimum_palindrome_cut)
    if input_string and ops:
        for op in ops:
            print(f'{op.__name__.replace("is_", "").replace("get_", "").replace("_", " ")}: {op(input_string)}')
    else:
        print('palindrome.py -i <input string> [-v] [-l] [-c]')
        sys.exit(2)


if __name__ == '__main__':
    assert (is_palindrome('a') is True)
    assert (is_palindrome('ab') is False)
    assert (is_palindrome('abba') is True)
    assert (is_palindrome('madamimeve') is False)
    assert (get_longest_palindrome('abaxyzzyxf') == 'xyzzyx')
    assert (get_minimum_palindrome_cut('noonabbad') == 2)
    _main(sys.argv[1:])
