import unittest
import ch1

class matrix_zero(unittest.TestCase):
    """Tests for function switch_base."""

    def test_default_case_1(self):
        """Test matrix_zero for a matrix with one zero"""
        actual = ch1.matrix_zero([[1,2,3],[0,1,3],[1,3,4]])
        expected = ([[0, 2, 3],
           [0, 0, 0],
           [0, 3, 4]])
        self.assertTrue((actual==expected).all())

    def test_default_case_2(self):
        """Test matrix_zero for a matrix with one row"""
        actual = ch1.matrix_zero([2,3,1,0])
        expected = ([0, 0, 0, 0])
        self.assertTrue((actual==expected).all())
        
if __name__ == '__main__':
    unittest.main(exit=False)
