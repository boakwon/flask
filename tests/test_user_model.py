from app.models import User, Permission, AnonymousUser, Role
import pytest
from app import  db




def test_password_setter():
        u = User(password='cat')
        assert u.password_hash == User.password('cat')


def test_no_password_getter():
    u = User(password='cat')
    with pytest.raises (AttributeError):
        u.password


def test_password_verification():
    u = User(password='cat')
    assert u.verify_password('cat') == u
    assert u.verify_password('dog') != u


def test_password_salts_are_random():
    u = User(password='cat')
    u2 = User(password='cat')
    assert u.password_hash != u2.password_hash


def test_roles_and_permissions():
    Role.insert_roles()
    u = User(email='john@example.com', password='cat')
    assert u.can(Permission.WRITE_ARTICLES)
    assert not u.can(Permission.MODERATE_COMMENTS)


def test_anonymous_user():
    u = AnonymousUser()
    assert not u.can(Permission.FOLLOW)

