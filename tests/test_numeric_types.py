import ast
import numbers
import unittest
from pathlib import Path

import numpy as np


class NumericTypesTest(unittest.TestCase):
    def test_numpy_numeric_scalars_are_numeric(self):
        source_path = Path(__file__).resolve().parents[1] / "Models" / "BN_single_model.py"
        syntax = ast.parse(source_path.read_text(encoding="utf-8"))
        class_node = next(
            node
            for node in syntax.body
            if isinstance(node, ast.ClassDef) and node.name == "BN_Single"
        )
        function = next(
            node
            for node in class_node.body
            if isinstance(node, ast.FunctionDef) and node.name == "is_numeric"
        )
        namespace = {"numbers": numbers}
        exec(
            compile(ast.Module(body=[function], type_ignores=[]), str(source_path), "exec"),
            namespace,
        )
        is_numeric = namespace["is_numeric"]

        self.assertTrue(is_numeric(None, np.int64(7)))
        self.assertTrue(is_numeric(None, np.float64(7.5)))
        self.assertFalse(is_numeric(None, "7"))


if __name__ == "__main__":
    unittest.main()
