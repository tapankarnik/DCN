from load_balancer_sliced import load_balancer
import json
import pytest

@pytest.fixture
def client():
    with load_balancer.test_client() as client:
        yield client

def test_hello_connection_test(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 2,
        num_jobs = 12,
        job_duration = 2,
        )
    result = client.post('/first_hello', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_loadbalancer1_valid_input(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 4,
        num_jobs = 11,
        job_duration = 3,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"OK" in result.data

def test_loadbalancer2_invalid_jobname_1(client):
    payload = dict(
        job_name = None,
        job_id = 1,
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer3_invalid_jobname_2(client):
    payload = dict(
        job_name = "",
        job_id = 1,
        num_jobs = 2,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer4_invalid_jobid_1(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 3,
        num_jobs = 2,
        job_duration = 15,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer5_invalid_jobname_3(client):
    payload = dict(
        job_name = "j-1234858585858585858588585948359348594385983",
        job_id = 1,
        num_jobs = 50,
        job_duration = 2,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer6_invalid_numjobs_1(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 101,
        job_duration = 29,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer7_invalid_jobduration_1(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 99,
        job_duration = 0,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer8_invalid_jobduration_2(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 1,
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer9_invalid_jobid_2(client):
    payload = dict(
        job_name = "Tapan",
        job_id = -1,
        num_jobs = 100,
        job_duration = 31,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer10_invalid_jobid_3(client):
    payload = dict(
        job_name = "Tapan",
        job_id = 102,
        num_jobs = 100,
        job_duration = 20,
        )
    payload = json.dumps(payload)
    result = client.post('/DCN', data=payload, content_type='application/json')
    assert b"Invalid Input" in result.data

def test_loadbalancer11_all_invalid(client):
    payload = dict(
        job_name = "",
        job_id = -1,
        num_jobs = 0,
        job_duration = 0,
        )

    result = client.post('/DCN', json=payload)
    assert b"Invalid Input" in result.data
