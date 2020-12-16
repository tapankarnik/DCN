from load_balancer_sliced import load_balancer
import json
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
        job_id = 4,
        num_jobs = 11,
        job_duration = 3,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_loadbalancer2(client):
    payload = dict(
        job_name = None,
        job_id = 1,
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer3(client):
    payload = dict(
        job_name = "",
        job_id = 1,
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer4(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 0,
        job_duration = 15,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer5(client):
    payload = dict(
        job_name = "j-1234858585858585858588585948359348594385983",
        job_id = 1,
        num_jobs = 50,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data
def test_loadbalancer6(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 101,
        job_duration = 29,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer7(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 99,
        job_duration = 0,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer8(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer9(client):
    payload = dict(
        job_name = "Tapan",
        job_id = -1,
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer10(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 102,
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer11(client):
    payload = dict(
        job_name = "",
        job_id = -1,
        num_jobs = 0,
        job_duration = 0,
        )

    result = client.post('/DCN', json=payload)
    assert b"Invalid Input" in result.data
