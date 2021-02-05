import pytest
import requests
import json

@pytest.mark.parametrize(
    'username,password,status',[
        ('test','123senha123',400),
        ('admin','123senha123',200)
    ]
)

def test_token_authentication(username,password,status):
    user = {
        "username":username,
        "password":password
    }

    response = requests.post('http://localhost:8000/token/',user)

    assert response.status_code == status

@pytest.mark.parametrize(
    'exp_date,holder,number,cvv,status',[
        ("07/21","Test 1","4539578763621486","123",201),#succes
        ("07/21","Test 2","4539578763621486","1234",201),#succes
        ("07/2021","Test 3","4539578763621486","",201),#succes
        ("07-21","Test 5","4539578763621486","123",201),#succes
        ("12/20","Test 4","4539578763621486","123",400),#exp_date is in the past!!
        ("07-21","Te","4539578763621486","123",400),#Holder has less than 3 characters
        ("07-21","Test 7","4539578763620000","124",400),#Credit Card is not valid
        ("07-21","Test 8","4539578763621486","14",400),#cvv has less tha 3 digits
        ("07-21","Test 9","4539578763621486","14681",400)#cvv has more than 4 digits
    ]
)

def test_post_creditcard(exp_date,holder,number,cvv,status):
    credit_card = {
        "exp_date":exp_date,
        "holder":holder,
        "number":number,
        "cvv":cvv
    }
    auth = {'Authorization': 'Token b96dc5862a760c6a860cf2366b7b028b3503390b'}
    response = requests.post('http://localhost:8000/credit-card/',headers=auth,data=json.dumps(credit_card))
    assert response.status_code == status