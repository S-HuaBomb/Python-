from nose.tools import assert_equal

class TestUniqueChars:
    
    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Success: test_unique_chars!')
        
def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        unique_chars_in_place = UniquecharsInPlace()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        pass
    
if __name__ == '__main__':
    main()
    
