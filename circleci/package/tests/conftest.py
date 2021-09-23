import pytest

from deploy_chk.config.core import config
from deploy_chk.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.test_data_file)