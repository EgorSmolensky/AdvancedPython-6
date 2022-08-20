import pytest
from ya_folder import ya_create_folder, token

fixtures = [
    (token, 'New folder', 201),
    (token, 'New folder', 409),
    (token, 'Свалка', 201),
    ('token', 'New', 401)
]


@pytest.mark.parametrize('ya_token, name, expect_result', fixtures)
def test_ya_create_folder(ya_token, name, expect_result):
    result = ya_create_folder(ya_token, name)
    assert expect_result == result


