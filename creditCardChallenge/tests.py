import pytest

@pytest.mark.parametrize(
    'username,password,status',[
        ('test','123senha123',400),
        ('admin','123senha123',200)
    ]
)