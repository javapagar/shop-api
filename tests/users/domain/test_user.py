from tests.users.domain.user_builder import UserBuilder


def test_build_user(user_id, user_email, user_password, user_enable):
    user = UserBuilder().build()

    assert user.uuid == user_id
    assert user.email == user_email
    assert user.password == user_password
    assert user.enable == user_enable
