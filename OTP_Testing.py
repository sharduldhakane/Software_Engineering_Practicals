import unittest
import OTP_Generator

class MyTestCase(unittest.TestCase):
    def test_1(self):
        email=OTP_Generator.validate_email()
        self.assertEqual(email, True)  # add assertion here
    def test_2(self):
        size=4
        email=OTP_Generator.generate_OTP()
        self.assertEqual(len(email), size)  # add assertion here
    def test_3(self):
        Email =OTP_Generator.sendOTP('8000')
        self.assertEqual(True,Email)
if __name__ == '__main__':
    unittest.main()
