from .context import Tim22


def test_init(capsys):
    bot = Tim22()  # noqa: F841
    captured = capsys.readouterr()
    assert "Tim22 init." in captured.out


def test_tim22(capsys):
    Tim22.run()
    captured = capsys.readouterr()
    assert "Hello, I'm Tim22." in captured.out
