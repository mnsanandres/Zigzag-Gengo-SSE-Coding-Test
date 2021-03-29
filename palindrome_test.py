import unittest

import palindrome


class MyTestCase(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            palindrome.is_palindrome(1)

    def test_palindrome(self):
        self.assertEqual(palindrome.is_palindrome(''), True)
        self.assertEqual(palindrome.is_palindrome('a'), True)
        self.assertEqual(palindrome.is_palindrome('ab'), False)
        self.assertEqual(palindrome.is_palindrome('abba'), True)
        self.assertEqual(palindrome.is_palindrome('racecar'), True)
        self.assertEqual(palindrome.is_palindrome('madamimadam'), True)
        self.assertEqual(palindrome.is_palindrome('madamimeve'), False)

    def test_longest_palindrome(self):
        self.assertEqual(palindrome.get_longest_palindrome('abaxyzzyxf'), 'xyzzyx')
        self.assertEqual(palindrome.get_longest_palindrome('madam referred a civic racecar model'), ' racecar ')
        self.assertEqual(palindrome.get_longest_palindrome('aaaaaaaaaaaaaa'), 'aaaaaaaaaaaaaa')
        self.assertEqual(palindrome.get_longest_palindrome('a'), 'a')
        self.assertEqual(palindrome.get_longest_palindrome('a22'), '22')

    def test_minimum_palindrome_cut(self):
        self.assertEqual(palindrome.get_minimum_palindrome_cut('noonabbad'), 2)  # noon|abba|d
        self.assertEqual(palindrome.get_minimum_palindrome_cut('racecar'), 0)  # racecar
        self.assertEqual(palindrome.get_minimum_palindrome_cut('11racecarevents'), 5)  # 11|racecar|eve|n|t|s
        self.assertEqual(palindrome.get_minimum_palindrome_cut('ddcbdd'), 3)  # dd|cb|dd
        self.assertEqual(palindrome.get_minimum_palindrome_cut('axaaabad'), 3)  # axa|a|aba|d
        self.assertEqual(palindrome.get_minimum_palindrome_cut('madamx'), 1)  # madam|x


if __name__ == '__main__':
    unittest.main()
