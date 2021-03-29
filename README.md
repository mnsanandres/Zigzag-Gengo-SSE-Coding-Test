# Table of Contents

* [palindrome](#palindrome)
  * [is\_palindrome](#palindrome.is_palindrome)
  * [get\_longest\_palindrome](#palindrome.get_longest_palindrome)
  * [get\_minimum\_palindrome\_cut](#palindrome.get_minimum_palindrome_cut)

<a name="palindrome"></a>
# palindrome

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

**Example**:

```
    >>> palindrome.py -i noonabbad -v -l -c
    palindrome: False
    longest palindrome: noon
    minimum palindrome cut: 2
```

<a name="palindrome.is_palindrome"></a>
#### is\_palindrome

```python
is_palindrome(string)
```

Determines whether a string is a palindrome. An assertion is first made to verify if the input is valid.
The string is checked against the reverse of itself and if both strings are equal, the input string is deemed
a palindrome.

Time and space complexity: O(n)

**Arguments**:

- `string`: The string to check

**Returns**:

`True` if the string is a palindrome. Otherwise, `False`

<a name="palindrome.get_longest_palindrome"></a>
#### get\_longest\_palindrome

```python
get_longest_palindrome(string)
```

Returns the longest substring that is a palindrome. All substrings of the main string is first generated.
We iterate over these substrings and check if it is longer than the current longest substring and
if it is a palindrome. If both conditions are satisfied, the substring replaces the current longest substring.

Time and space complexity: O(n!) since we are retrieving all the substring combinations of the parent string

**Arguments**:

- `string`: The string to check

**Returns**:

The longest substring that is a palindrome

<a name="palindrome.get_minimum_palindrome_cut"></a>
#### get\_minimum\_palindrome\_cut

```python
get_minimum_palindrome_cut(string)
```

Returns the minimum number of cuts needed such that all substrings will be a palindrome.
All substrings are generated and are sorted by length in descending order to ensure that the maximum length
palindrome substrings are first checked. We iterate over these substrings and check if it is a palindrome and is
found in the current parent string. If both conditions are satisfied, a counter for substring is increment and we
remove the substring from the parent string. The minimum cut will be one less than the number of substrings found.

Time and space complexity: O(n!) since we are retrieving all the substring combinations of the parent string

**Arguments**:

- `string`: The string to check

**Returns**:

The number of cuts needed such that all substrings will be a palindrome

