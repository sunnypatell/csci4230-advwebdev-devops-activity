# test_app.py
# author: sunny patel (100867748)
# course: csci 4230 advanced web development
# activity 8: unit tests for flask api

import pytest  # inline: test runner
from app import create_app  # inline: app factory


@pytest.fixture()
def client():
    """return a flask test client per test."""
    app = create_app()  # inline: fresh app per test
    return app.test_client()  # inline: client for requests


def test_hello(client):
    """GET /hello returns expected greeting and status."""
    res = client.get("/hello")  # inline: call endpoint
    assert res.status_code == 200  # inline: ok
    assert res.get_json() == {"message": "Hello, World!"}  # inline: exact body


def test_echo(client):
    """POST /echo mirrors payload and uses 201 status."""
    payload = {"msg": "ping"}  # inline: sample data
    res = client.post("/echo", json=payload)  # inline: send as json
    assert res.status_code == 201  # inline: created
    assert res.get_json() == payload  # inline: mirrored


def test_put_then_delete_item(client):
    """PUT then DELETE flow for /items/<key>."""
    # put
    res_put = client.put("/items/k1", json={"value": "v1"})  # inline: store
    assert res_put.status_code == 200  # inline: ok
    assert res_put.get_json() == {"key": "k1", "value": "v1"}  # inline: saved pair

    # delete
    res_del = client.delete("/items/k1")  # inline: delete
    assert res_del.status_code == 200  # inline: ok
    assert res_del.get_json() == {"deleted": "k1"}  # inline: confirmation

    # delete again -> 404
    res_del2 = client.delete("/items/k1")  # inline: second attempt
    assert res_del2.status_code == 404  # inline: not found
