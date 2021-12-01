from typing import Sequence
from django.test import SimpleTestCase
from .models import Amino
# Create your tests here.

class BacktranslationTestCase(SimpleTestCase):
    def setup(self):
        return

    def test_single_lower_amino_acid(self):

        am = Amino()
        seq = 'f'
        expected = ['UUC','UUU']
        valid, response = am.backtranslate(seq)

        self.assertTrue(response in expected)

    def test_single_upperr_amino_acid(self):
        #Can be done for all characters
        am = Amino()
        seq = 'F'
        expected = ['UUC','UUU']
        valid, response = am.backtranslate(seq)

        self.assertTrue(response in expected)

    def test_faulty_char_error_code(self):

        am = Amino()
        seq = '1'
        valid, response = am.backtranslate(seq)

        self.assertEqual(response,"Invalid Amino Acid {} at index {} ".format(1,0))

    def test_faulty_char_error_valid(self):

        am = Amino()
        seq = '1'
        valid, response = am.backtranslate(seq)
        self.assertFalse(valid)

    def test_faulty_in_sequence(self):

        am = Amino()
        seq = 'fli*xbw'
        valid, response = am.backtranslate(seq)

        self.assertEqual(response,"Invalid Amino Acid {} at index {} ".format('x'.upper(),seq.index('x')))

    def test_len_sequence(self):
        am = Amino()
        seq ='fliflifli'
        valid, response = am.backtranslate(seq)
        self.assertEqual(len(response), 3*len(seq))