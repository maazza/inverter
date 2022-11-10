import pytest
from fastapi.testclient import TestClient

from .main import app, inverse

client = TestClient(app)


def test_inverse():
    res = inverse([1, 5, 7, 8, 6, 2, 9, 7], 3)
    assert res == [7, 2, 8, 7, 6, 5, 9, 1]


def test_inverse_endpoint():
    response = client.post(
        "/inverse",
        json={"N": 3, "Input": [1, 5, 7, 8, 6, 2, 9, 7]},
    )
    assert response.status_code == 200
    assert response.json() == [7, 2, 8, 7, 6, 5, 9, 1]
