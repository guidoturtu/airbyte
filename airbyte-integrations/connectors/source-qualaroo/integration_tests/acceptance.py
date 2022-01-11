#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import pytest

pytest_plugins = ("source_acceptance_test.plugin",)


@pytest.fixture(scope="session", autouse=True)
def connector_setup():
    yield
