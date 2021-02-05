import pytest
import requests

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

    response = resquests.post('http://localhost:8000/token/',user)

    assert response.status_code == status