from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from deploy_chk.config.core import config
from deploy_chk.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    dat = pd.read_csv("C:/deep_learning_gpu/deployment/api/app/tests/test_deploy_chk.csv")
    dat["Date"] = ""
    dat["StateHoliday"] = dat["StateHoliday"].astype("str")
    dat = dat.drop("Customers", axis=1)

    return dat


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
