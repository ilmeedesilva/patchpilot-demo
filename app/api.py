from marshmallow import Schema, fields, validate


class SignupRequest(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    plan = fields.Str(missing="free", validate=validate.OneOf(["free", "pro"]))
    newsletter = fields.Bool(missing=False)


class UserResponse(Schema):
    username = fields.Str()
    plan = fields.Str(default="free")
    seats = fields.Int(default=1)


def load_signup(data: dict) -> dict:
    return SignupRequest().load(data)


def dump_user(user: dict) -> dict:
    return UserResponse().dump(user)
