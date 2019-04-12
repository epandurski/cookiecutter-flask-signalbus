from {{cookiecutter.app_slug}} import __version__


def test_version(db_session):
    assert __version__ == '0.1.0'
