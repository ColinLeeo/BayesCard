import unittest

import numpy as np
import pandas as pd

from Models.tools import discretize_series


class DiscretizeSeriesTest(unittest.TestCase):
    def test_continuous_series_with_missing_values(self):
        series = pd.Series([1.0, 2.0, np.nan])

        discretized, _, _, _, mapping, _, _, _ = discretize_series(
            series,
            n_mcv=30,
            n_bins=30,
            is_continous=True,
        )

        self.assertFalse(discretized.isna().any())
        self.assertTrue(mapping)
        self.assertTrue(all(isinstance(interval, pd.Interval) for interval in mapping.values()))


if __name__ == "__main__":
    unittest.main()
