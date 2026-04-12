from typer.testing import CliRunner

from typer_chucknorris.main import app

runner = CliRunner()


def test_chuck():
    """
    Simple test to make sure response happens.
    """
    result = runner.invoke(app, ["chuck"])
    assert result.exit_code == 0


def test_version():
    """
    Test version output.
    """

    result = runner.invoke(app, ["chuck", "-v"])
    assert "Awesome Chuck " in result.output
