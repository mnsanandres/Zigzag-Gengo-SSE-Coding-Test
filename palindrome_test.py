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

    def test_minimum_palindrome_cut(self):
        self.assertEqual(palindrome.get_minimum_palindrome_cut('noonabbad'), 2)
        self.assertEqual(palindrome.get_minimum_palindrome_cut('racecar'), 0)
        self.assertEqual(palindrome.get_minimum_palindrome_cut('11racecarevents'), 5)


if __name__ == '__main__':
    unittest.main()
