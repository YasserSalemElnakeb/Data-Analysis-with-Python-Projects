import unittest
import sea_level_predictor
import numpy as np


class LinePlotTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()


    def test_plot_title(self):

        actual = self.ax.get_title()

        expected = "Rise in Sea Level"

        self.assertEqual(
            actual,
            expected
        )


    def test_plot_labels(self):

        self.assertEqual(
            self.ax.get_xlabel(),
            "Year"
        )

        self.assertEqual(
            self.ax.get_ylabel(),
            "Sea Level (inches)"
        )


    def test_number_of_lines(self):

        actual = len(
            self.ax.get_lines()
        )

        expected = 2

        self.assertEqual(
            actual,
            expected
        )


    def test_scatter_points(self):

        actual = len(
            self.ax.collections[0].get_offsets()
        )

        expected = 134

        self.assertEqual(
            actual,
            expected
        )


    def test_prediction_lines(self):

        line1 = self.ax.get_lines()[0]
        line2 = self.ax.get_lines()[1]


        self.assertEqual(
            len(line1.get_xdata()),
            171
        )


        self.assertEqual(
            len(line2.get_xdata()),
            51
        )


if __name__ == "__main__":
    unittest.main()