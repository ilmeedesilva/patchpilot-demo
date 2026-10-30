import pytest
from app.api import dump_user, load_signup
from marshmallow import ValidationError


def test_signup_fills_in_defaults():
    assert load_signup({"username": "ilmee", "email": "ilmee@example.com"}) == {
        "username": "ilmee",
        "email": "ilmee@example.com",
        "plan": "free",
        "newsletter": False,
    }


def test_signup_rejects_unknown_plan():
    with pytest.raises(ValidationError, match="plan"):
        load_signup({"username": "ilmee", "email": "ilmee@example.com", "plan": "gold"})


def test_signup_rejects_short_username():
    with pytest.raises(ValidationError, match="username"):
        load_signup({"username": "il", "email": "ilmee@example.com"})


def test_user_response_fills_in_defaults():
    assert dump_user({"username": "ilmee"}) == {"username": "ilmee", "plan": "free", "seats": 1}
