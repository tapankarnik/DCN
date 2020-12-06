from app import app

import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    payload = dict(
        job_name = app.config['JOB_NAME'],
        job_id = app.config['JOB_ID'],
        num_jobs = app.config['NUM_JOBS'],
        job_duration = app.config['JOB_DURATION'],
        )
    result = client.post('/first_hello', data=payload)
    assert b"OK" in result.data


