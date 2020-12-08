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
    result = client.post('/first_hello', data=payload)
    assert b"OK" in result.data


