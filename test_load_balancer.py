from load_balancer import load_balancer

import pytest

@pytest.fixture
def client():
    with load_balancer.test_client() as client:
        yield client

def test_hello(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 2,
        num_jobs = 12,
        job_duration = 2,
        )
    result = client.post('/first_hello', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_loadbalancer1(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 2,
        num_jobs = 12,
        job_duration = 2,
        )

    result = client.post('/DCN', json=payload)
    assert b"OK" in result.data

def test_loadbalancer2(client):
    payload = dict(
        job_name = "",
        job_id = -1,
        num_jobs = 0,
        job_duration = 0,
        )

    result = client.post('/DCN', json=payload)
    assert b"Invalid Input" in result.data



