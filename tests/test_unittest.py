import calculate
import unittest
from unittest import mock
from io import StringIO

class Test_Calculate(unittest.TestCase):

    # runs main with mocked input and output to test main
    @mock.patch('sys.stdout', new_callable=StringIO)
    def main_op(self, tst_str, mock_stdout):
        with mock.patch('builtins.input', side_effect=tst_str):
            calculate.main()
        return mock_stdout.getvalue()

    # default output used for testing errors and validation
    expected = '{\n"monthly payment": "152.81",\n"total interest": "1168.56",\n"total payment": "11168.56"\n}\n'

    def test_valid(self):
        self.assertEqual(self.main_op(['10000', '5.5', '2000', '5']), self.expected)

    def test_largernums(self):
        largeroutput = '{\n"monthly payment": "6098.75",\n"total interest": "165480.22",\n"total payment": "615480.22"\n}\n'
        self.assertEqual(self.main_op(['450000', '8.75', '30000', '8']), largeroutput)    

    def test_hugenums(self):
        hugeoutput = '{\n"monthly payment": "8974123.65",\n"total interest": "3311855227.99",\n"total payment": "3771675576.99"\n}\n'
        self.assertEqual(self.main_op(['459820349', '23.54345', '2543645', '35']), hugeoutput)    

    def test_too_big_int(self):
        em = 'Please input a value with less than 15 digits\n'
        self.assertEqual(self.main_op(['230498572945872480975902395823745', '10000', '5.5', '2000', '5']), em + self.expected)    

    def test_too_big_float(self):
        em = 'Please input a value with less than 15 digits\n'
        self.assertEqual(self.main_op(['10000', '43985729458727958.243895724485', '5.5', '2000', '5']), em + self.expected)    

    def test_string_int(self):
        em = 'This is not an integer. Please enter a valid integer (ex. 1000)\n'
        self.assertEqual(self.main_op(['abc', '10000', '5.5', '2000', '5']), em + self.expected)    
    
    def test_string_float(self):
        em = 'This is not a floating point number. Please enter a valid floating point number (ex. 5.5)\n'
        self.assertEqual(self.main_op(['10000', '5.9f', '5.5', '2000', '5']), em + self.expected) 

    def test_neg_int(self):
        em = 'Please enter a positive number\n'
        self.assertEqual(self.main_op(['-5000', '10000', '5.5', '2000', '5']), em + self.expected)    
  
    def test_neg_float(self):
        em = 'Please enter a positive number\n'
        self.assertEqual(self.main_op(['10000', '-35.5', '5.5', '2000', '5']), em + self.expected)   

    def test_empty_int(self):
        em = 'This is not an integer. Please enter a valid integer (ex. 1000)\n'
        self.assertEqual(self.main_op(['', '10000', '5.5', '2000', '5']), em + self.expected) 

    def test_empty_float(self):
        em = 'This is not a floating point number. Please enter a valid floating point number (ex. 5.5)\n'
        self.assertEqual(self.main_op(['10000', '', '5.5', '2000', '5']), em + self.expected) 

    def test_injection_attack_int(self):
        em = 'Please input a value with less than 15 digits\n'
        self.assertEqual(self.main_op(['drop database master', '10000', '5.5', '2000', '5']), em + self.expected)    

    def test_injection_attack_float(self):
        em = 'Please input a value with less than 15 digits\n'
        self.assertEqual(self.main_op(['10000', 'drop database master', '5.5', '2000', '5']), em + self.expected)    

if __name__ == '__main__':
    unittest.main()