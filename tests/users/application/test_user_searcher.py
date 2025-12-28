from uuid import uuid4

from src.users.application.user_searcher import UserSearcher
from tests.users.domain.user_builder import UserBuilder


def test_user_searcher_not_find_user(repo_user):
    user_uuid = uuid4().hex
    searcher = UserSearcher(repo_user)

    user = searcher.search(user_uuid)

    assert user is None


def test_user_searcher_must_find_user(repo_user):
    user_uuid = uuid4().hex
    searcher = UserSearcher(repo_user)
    user = UserBuilder().with_id(user_uuid).build()

    assert user is not None

    repo_user.save(user)

    user_finded = searcher.search(user_uuid)

    assert user_finded.get("uuid") == user.uuid
