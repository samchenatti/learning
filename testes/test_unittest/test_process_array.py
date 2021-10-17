from unittest import TestCase
from hypothesis.strategies._internal.strategies import Ex
import numpy as np
from my_package.process_array import double_and_concat_array
from numpy.testing import assert_array_equal

import hypothesis
from hypothesis.extra.numpy import arrays


class TestProcessArray(TestCase):
    """
    Tests the functions in the module `process_array`
    """

    def test_double_and_concat_array(self):
        """
        Testing using static examples
        """
        original = np.ones(shape=(5,))

        expected = np.concatenate([original, 2*original])

        result = double_and_concat_array(original_array=original)

        # Usando o módulo de testes integrados do NumPy
        assert_array_equal(
            x=expected,
            y=result
        )

        # Alternativamente
        self.assertTrue(
            np.array_equal(expected, result),
            'The array should have been transformed in the expected way'
        )

    @hypothesis.given(arrays(dtype=np.short, shape=(5,)))
    @hypothesis.example(np.array([0, 0, 0, 0, 0]))
    def test_double_and_concat_array_with_examples(
            self, example_arr: np.array):
        """
        Testing using generated examples
        """
        expected = np.concatenate([example_arr, 2 * example_arr])

        result = double_and_concat_array(original_array=example_arr)

        # Usando o módulo de testes integrados do NumPy
        assert_array_equal(
            x=expected,
            y=result
        )

        # Alternativamente
        self.assertTrue(
            np.array_equal(expected, result),
            'The array should have been transformed in the expected way'
        )
