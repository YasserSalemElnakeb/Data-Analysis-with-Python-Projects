import unittest
import time_series_visualizer


class LinePlotTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]


    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected)


    def test_line_plot_labels(self):
        self.assertEqual(
            self.ax.get_xlabel(),
            "Date"
        )

        self.assertEqual(
            self.ax.get_ylabel(),
            "Page Views"
        )


    def test_line_plot_data_quantity(self):
        actual = len(self.ax.lines[0].get_ydata())
        expected = 1238
        self.assertEqual(actual, expected)



class BarPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]


    def test_bar_plot_labels(self):

        self.assertEqual(
            self.ax.get_xlabel(),
            "Years"
        )

        self.assertEqual(
            self.ax.get_ylabel(),
            "Average Page Views"
        )


    def test_bar_plot_years(self):

        actual = [
            label.get_text()
            for label in self.ax.get_xaxis().get_majorticklabels()
        ]

        expected = [
            '2016',
            '2017',
            '2018',
            '2019'
        ]

        self.assertEqual(actual, expected)


    def test_bar_plot_legend(self):

        actual = [
            label.get_text()
            for label in self.ax.get_legend().get_texts()
        ]

        expected = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]

        self.assertEqual(actual, expected)



class BoxPlotTestCase(unittest.TestCase):

    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()

        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]


    def test_number_of_boxplots(self):

        actual = len(self.fig.axes)
        expected = 2

        self.assertEqual(actual, expected)


    def test_titles(self):

        self.assertEqual(
            self.ax1.get_title(),
            "Year-wise Box Plot (Trend)"
        )

        self.assertEqual(
            self.ax2.get_title(),
            "Month-wise Box Plot (Seasonality)"
        )


    def test_labels(self):

        self.assertEqual(
            self.ax1.get_xlabel(),
            "Year"
        )

        self.assertEqual(
            self.ax1.get_ylabel(),
            "Page Views"
        )

        self.assertEqual(
            self.ax2.get_xlabel(),
            "Month"
        )

        self.assertEqual(
            self.ax2.get_ylabel(),
            "Page Views"
        )


    def test_year_labels(self):

        actual = [
            label.get_text()
            for label in self.ax1.get_xaxis().get_majorticklabels()
        ]

        expected = [
            '2016',
            '2017',
            '2018',
            '2019'
        ]

        self.assertEqual(actual, expected)


    def test_month_labels(self):

        actual = [
            label.get_text()
            for label in self.ax2.get_xaxis().get_majorticklabels()
        ]

        expected = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]

        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()