from src.users.application.user_saver import UserSaver


def test_user_saver(repo_user, user_email, user_password, user_enable):
    user_repository = repo_user
    saver = UserSaver(user_repository)

    user_uuid = saver.save(user_email, user_password, user_enable)

    user_list = user_repository.get_all()

    assert user_uuid is not None
    assert len(user_list) == 1
