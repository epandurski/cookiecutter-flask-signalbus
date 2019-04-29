from {{cookiecutter.app_slug}} import __version__


def test_version(db_session):
    assert __version__
