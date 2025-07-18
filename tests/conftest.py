import pytest

@pytest.fixture
def dbops_instance(mocker):
    return mocker.patch("database_ops.DatabaseOps")