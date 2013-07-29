import unittest
import switch_base

class TestSwitchBase(unittest.TestCase):
    """Tests for function switch_base."""

    def test_default_case_2a(self):
        """Test switch_case to convert 16 to base 2"""
        actual = switch_base.switch_base(16)
        expected = '10000'
        self.assertEqual(expected, actual)
 
    def test_default_case_2b(self):
        """Test switch_case to convert 17 to base 2"""
        actual = switch_base.switch_base(17)
        expected = '10001'
        self.assertEqual(expected, actual)

    def test_default_case_2c(self):
        """Test switch_case to convert 0 to base 2"""
        actual = switch_base.switch_base(0)
        expected = '0'
        self.assertEqual(expected, actual)

    def test_default_case_3a(self):
        """Test switch_case to convert 17 to base 3"""
        actual = switch_base.switch_base(17,3)
        expected= '122'
        self.assertEqual(expected, actual)

    def test_default_case_3b(self):
        """Test switch_case to convert 21 to base 3"""
        actual = switch_base.switch_base(21,3)
        expected= '210'
        self.assertEqual(expected, actual)

    def test_default_case_10a(self):
        """Test switch_case to convert 21 to base 10"""
        actual = switch_base.switch_base(21,10)
        expected= '21'
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
