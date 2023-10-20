import pytest

from math_operations import MathOp


class TestMathOPInstantiation:

    def test_math_op_instantiate(self):
        with pytest.raises(TypeError):
            math_op = MathOp()
