# pydantic-demo

A tiny app written against **pydantic v1**, used to try out `patchpilot upgrade`.
Upgrading to pydantic v2 breaks it in three ways:

- `BaseSettings` moved to the separate `pydantic-settings` package
- `@root_validator` without `skip_on_failure=True` is an error in v2
- `.dict()` / `.parse_obj()` are deprecated in favour of `.model_dump()` / `.model_validate()`

This repo exists so you can watch [patchpilot](https://github.com/ilmeedesilva/patchpilot) fix it.

👉 **[See the pull request patchpilot opened](https://github.com/ilmeedesilva/patchpilot-demo/pull/1)**. It's left open on purpose, as a live example, so this branch stays on pydantic v1.

## patchpilot runs here every week

[`.github/workflows/patchpilot.yml`](.github/workflows/patchpilot.yml) runs the [patchpilot GitHub Action](https://github.com/ilmeedesilva/patchpilot) every Monday, and you can also start it from the **Actions** tab. Each run picks the next outdated package, upgrades it, fixes the code, and opens a pull request.

The app also uses **marshmallow 3** ([`app/api.py`](app/api.py)). marshmallow 4 removed the `missing=` and `default=` field options, so upgrading it breaks the app. pydantic already has an open PR, so the Action skips it and moves on to marshmallow.
