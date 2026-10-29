# pydantic-demo

A tiny app written against **pydantic v1**, used to try out `patchpilot upgrade`.
Upgrading to pydantic v2 breaks it in three ways:

- `BaseSettings` moved to the separate `pydantic-settings` package
- `@root_validator` without `skip_on_failure=True` is an error in v2
- `.dict()` / `.parse_obj()` are deprecated in favour of `.model_dump()` / `.model_validate()`

This repo exists so you can watch [patchpilot](https://github.com/ilmeedesilva/patchpilot) fix it.

👉 **[See the pull request patchpilot opened](https://github.com/ilmeedesilva/patchpilot-demo/pull/1)**. It's left open on purpose, as a live example, so this branch stays on pydantic v1.
