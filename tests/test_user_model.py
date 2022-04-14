from app.models import User, Permission, AnonymousUser, Role
import pytest


def test_password_setter():
    u = User(password='cat')
    assert u.password_hash is not None


def test_no_password_getter():
    u = User(password='cat')
    with pytest.raises(AttributeError):
        u.password


def test_password_verification():
    u = User(password='cat')
    assert u.verify_password('cat') == True
    assert u.verify_password('dog') == False


def test_password_salts_are_random():
    u1 = User(password='cat')
    u2 = User(password='cat')
    assert u1.password_hash != u2.password_hash


def test_user_role():
    u = User(email='john@example.com', password='cat')
    assert u.can(Permission.FOLLOW) == True
    assert u.can(Permission.COMMENT) == True
    assert u.can(Permission.WRITE) == True
    assert u.can(Permission.MODERATE) == False
    assert u.can(Permission.ADMIN) == False

def test_moderator_role():
    r = Role.query.filter_by(name='Moderator').first()
    u = User(email='john@example.com', password='cat', role=r)
    assert u.can(Permission.FOLLOW) == True
    assert u.can(Permission.COMMENT) == True
    assert u.can(Permission.WRITE) == True
    assert u.can(Permission.MODERATE) == True
    assert u.can(Permission.ADMIN) == False


def test_administrator_role():
    r = Role.query.filter_by(name='Administrator').first()
    u = User(email='susan@example.com', password='cat', role=r)
    assert u.can(Permission.FOLLOW) == True
    assert u.can(Permission.COMMENT) == True
    assert u.can(Permission.WRITE) == True
    assert u.can(Permission.MODERATE) == True
    assert u.can(Permission.ADMIN) == True


def test_anonymous_user():
    u = AnonymousUser()
    assert u.can(Permission.FOLLOW) == False
    assert u.can(Permission.COMMENT) == False
    assert u.can(Permission.WRITE) == False
    assert u.can(Permission.MODERATE) == False
    assert u.can(Permission.ADMIN) == False


if __name__ == '__main__':
    pytest.main(['test_user_model.py'])