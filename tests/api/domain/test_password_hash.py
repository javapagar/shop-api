from api.domain.password_hash import PasswordHashValue


def test_password_hash():
    plain_password = "123"
    password_hash = PasswordHashValue(value=plain_password)

    assert plain_password != password_hash.value
    assert password_hash.verify_password(plain_password)
