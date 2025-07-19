# rule34Py Tests Readme

This project is tested by an organic test suite based on `pytest`.


## Running the Test Suite

To run the unit tests on your repo's source code, install the test suite dependencies declared in `:pyproject.toml` and invoke pytest.

```bash
# From the top level of the project ...
poetry install
PYTHONPATH=. poetry run pytest tests/
```


## Test Code Layout

* `fixtures/` contains pytest Fixtures common to many testing contexts.
	* `mock34/` contains an implementation of the [`Responses`](https://pypi.org/project/responses/) module that intercepts and either proxies or replays `requests` calls to the rule34 API and website. This fixture allows you to test this project without making real requests over the internet.
* `unit/` contains tests that can be run against the rule34Py source code without building or installing the module.


## Updating the Mock34 Responses

The `mock34` test fixture maintains a registry of rule34.xxx responses in its `responses.yml` file. When you run the test suite normally, all `requests` calls will be intercepted and delivered a replayed response from this registry. If `requests` makes a call to a URL that is not in the registry, the mock34 Fixture will throw an error.

If you are confident that the requested content is well-formed (as when you are adding a new test case), or if you wish to generally update the registry after an update to the upstream Rule34 API, you can switch the mock34 Fixture into a "record" mode by asserting the environment variable `R34_RECORD_RESPONSES=True`. When asserted the mock34 Fixture will proxy requests through to the public servers and record their responses in the registry.

```bash
export R34_RECORD_RESPONSES=True
# From the top level of the project ...
PYTHONPATH=. poetry run pytest tests/
```

Remember to commit the registry file changes with your test changes.
