from pydantic import BaseModel, field_validator, model_validator


class SignupForm(BaseModel):
    username: str
    email: str
    password: str
    password_confirm: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value):
        if "@" not in value:
            raise ValueError("not an email address")
        return value.strip().lower()

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("passwords do not match")
        return self


def to_public_dict(form: SignupForm) -> dict:
    return form.model_dump(exclude={"password", "password_confirm"})


def parse_signup(data: dict) -> SignupForm:
    return SignupForm.model_validate(data)
