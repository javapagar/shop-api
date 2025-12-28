import os
import pytest
from uuid import uuid4

from src.users.application.user_saver import UserSaver
from src.users.infrastructure.in_file_user_repository import InFileUserRepository


@pytest.fixture(autouse=True)
def create_repo():
    file_name = "user_test"
    repo = InFileUserRepository(file_name)
    yield repo
    os.remove(file_name)


def test_user_saver(create_repo, user_email, user_password, user_enable):
    user_repository = create_repo
    saver = UserSaver(user_repository)

    user_uuid = saver.save(user_email, user_password, user_enable)

    user_list = user_repository.get_all()

    assert user_uuid is not None
    assert len(user_list) == 1
