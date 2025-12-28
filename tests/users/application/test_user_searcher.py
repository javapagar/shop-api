import os
import pytest
from uuid import uuid4

from src.users.application.user_searcher import UserSearcher
from src.users.infrastructure.in_file_user_repository import InFileUserRepository
from tests.users.domain.user_builder import UserBuilder


@pytest.fixture(autouse=True)
def create_repo():
    file_name = "user_test"
    repo = InFileUserRepository(file_name)
    yield repo
    os.remove(file_name)


def test_user_searcher_not_find_user(create_repo):
    user_uuid = uuid4().hex
    user_repository = create_repo
    searcher = UserSearcher(user_repository)

    user = searcher.search(user_uuid)

    assert user is None


def test_user_searcher_must_find_user(create_repo):
    user_uuid = uuid4().hex
    user_repository:InFileUserRepository = create_repo
    searcher = UserSearcher(user_repository)
    user = UserBuilder().with_id(user_uuid).build()

    assert user is not None

    user_repository.save(user)

    user_finded = searcher.search(user_uuid)

    assert user_finded.get("uuid") == user.uuid
