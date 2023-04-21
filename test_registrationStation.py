import unittest
from io import StringIO
import sys
from unittest.mock import patch
import RegistrationStation


class MyTestCase(unittest.TestCase):

    @patch("sys.stdin", StringIO("elomkhDBN2022\ny\n"))
    def test_valid_username_lowercase(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual("Select username: 4 April - Johannesburg Physical - No prior experience\n", text_capture.getvalue())

    @patch("sys.stdin", StringIO("elomkhDBN2022\nY\n"))
    def test_valid_username_Uppercase(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual("Select username: 4 April - Johannesburg Physical - No prior experience\n", text_capture.getvalue())


    @patch("sys.stdin", StringIO("elokhDBN2022\nelomkhDBN2022\ny\n"))
    def test__invalid_username(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual("""Select username: Please enter valid existing username
Select username: 4 April - Johannesburg Physical - No prior experience\n""", text_capture.getvalue())

    @patch("sys.stdin", StringIO("elomkhDBN2022\ny\n"))
    def test_valid_confirmation(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual("""Select username: 4 April - Johannesburg Physical - No prior experience
Is this correct? (Y/n): """, text_capture.getvalue())

    @patch("sys.stdin", StringIO("elonkhDBN2022\nelomkhDBN2022\ny\n"))
    def test_valid_confirmation_invalid_username(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual("""Select username: Please enter valid existing username
Select username: 4 April - Johannesburg Physical - No prior experience
Is this correct? (Y/n): """, text_capture.getvalue())

    @patch("sys.stdin", StringIO("elomkhDBN2022\nn\n"))
    def test_incorrect_user_details(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual("""Select username: 4 April - Johannesburg Physical - No prior experience
Is this correct? (Y/n): """, text_capture.getvalue())

    @patch("sys.stdin", StringIO("elomkhDBN2022\nn\nelomkhDBN2022 - 4 April - Johannesburg Physical - No prior experience\n"))
    def test_incorrect_user_details_corrected(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual("""Select username: 4 April - Johannesburg Physical - No prior experience
Is this correct? (Y/n): Username - Date - Location - Experience: 4 April - Johannesburg Physical - No prior experience\n""", text_capture.getvalue())   
 
 
    @patch("sys.stdin", StringIO("colootsJHB2023\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\n"))
    def test_incorrect_user_details_corrected_additional(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual("""Select username: 13 May - Johannesburg Physical - No Prior Experience
Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience\n""", text_capture.getvalue())   
 
    @patch("sys.stdin", StringIO("colootsJHB2023\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\ny"))
    def test_incorrect_user_details_incorrect_addition(self):

        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual("""Select username: 13 May - Johannesburg Physical - No Prior Experience
Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience
Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience\n""", text_capture.getvalue())   
 
if __name__ == '__main__':
    unittest.main()

