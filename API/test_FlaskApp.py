import pytest
import sys
sys.path.insert(0, '/MonitoringApp/API')
import FlaskApp 
import ast 

@pytest.fixture
def client():

    FlaskApp.app.config['TESTING'] = True

    with FlaskApp.app.test_client() as client:
        yield client

def CheckContent(data):
    decode = data.decode("UTF-8")
    mydata = ast.literal_eval(decode)
    return(len(mydata) > 0)
    
def assert_CPU(response):
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    if  CheckContent(response.data) == True :
        assert b'Time' in response.data
        assert b'CPU Utilization' in response.data

def assert_Others(response):
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    if  CheckContent(response.data) == True :
        assert b'Total' in response.data
        assert b'Free' in response.data
        assert b'Time' in response.data
        assert b'Used' in response.data
                       
def test_homepage(client):
    response = client.get("/")
    assert b'Hello' in response.data

def test_CPUPage(client):
    response = client.get("/CPU")
    assert_CPU(response)

def test_CPUNowPage(client):
    response = client.get("/CPU-Now")
    assert_CPU(response)

def test_MemoryPage(client):
    response = client.get("/Memory")
    assert_Others(response)

def test_MemoryNowPage(client):
    response = client.get("/Memory-Now")
    assert_Others(response)

def test_DiskPage(client):
    response = client.get("/Disk")
    assert_Others(response)

def test_DiskNowPage(client):
    response = client.get("/Disk-Now")
    assert_Others(response)
       
