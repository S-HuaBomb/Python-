from nose.tools import assert_equal

class TestPermutation:
    
    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('a ct', 'ca t'), True)
        assert_equal(func('dog', 'doggo'), False)
        print('Success: Test_permutation')

def main():
    test = TestPermutation()
    permutation = Permutation()
    test.test_permutation(permutation.is_permutation)
    try:
        permutation_alt = PermutationAlt()
        test.test_permutation(permutation_alt.is_permutauion)
    except NameError:
        # permutation_alt 仅在permutation_solution中定义
        pass

if __name__ == '__main__':
    main()
