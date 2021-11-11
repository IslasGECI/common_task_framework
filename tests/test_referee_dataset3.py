from ..common_task_framework import Referee
import pytest

path_to_complete_dataset = "tests/test_dataset3/complete_dataset.csv"


def test_exceptions_raised_when_no_values():
    with pytest.raises(
        ValueError, match="^There is a record with no values for any explanatory variable$"
    ):
        Referee(path_to_complete_dataset)