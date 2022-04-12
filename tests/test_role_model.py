import pytest

from app.models import Permission, User


def test_add_permission():
    roles = {
        'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE], }
    assert User.p
