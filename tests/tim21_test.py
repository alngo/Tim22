from .context import tim22


def test_tim22(capsys):
    tim22.Tim22.run()
    captured = capsys.readouterr()

    assert "Hello, I'm Tim22." in captured.out
