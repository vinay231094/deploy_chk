import math

import numpy as np

from deploy_chk.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_no_predictions = 250

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.float32)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions