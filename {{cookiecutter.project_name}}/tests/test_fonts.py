from enum import EnumMeta
from inspect import ismethod
import {{cookiecutter.module_name}}
import pytest


@pytest.mark.parametrize("attr", {{cookiecutter.module_name}}.__all__)
def test_icons(attr):
    fonticon = getattr({{cookiecutter.module_name}}, attr)
    assert isinstance(fonticon, EnumMeta)
    assert ismethod(fonticon._font_file)
    assert isinstance(fonticon._font_file(), str)
    assert fonticon._font_file().lower().endswith((".ttf", ".otf"))
    for member in list(fonticon):
        assert len(member.value) == 1
        assert isinstance(member.value, str)
