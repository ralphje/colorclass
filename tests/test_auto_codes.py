"""Test auto codes."""

import colorclass
import colorclass.codes
import colorclass.toggles


def test_toggle():
    """Make sure toggles work."""
    colorclass.toggles.set_light_background()
    assert colorclass.codes.ANSICodeMapping.LIGHT_BACKGROUND

    colorclass.toggles.set_dark_background()
    assert not colorclass.codes.ANSICodeMapping.LIGHT_BACKGROUND


def test_auto_codes():
    """Make sure colors change when toggled."""
    codes = colorclass.codes.ANSICodeMapping()

    key = '{autoblack}{autored}{autogreen}{autoyellow}{autoblue}{automagenta}{autocyan}{autowhite}'
    colorclass.toggles.set_light_background()
    assert '3031323334353637' == key.format(**codes)

    colorclass.toggles.set_dark_background()
    assert '9091929394959697' == key.format(**codes)

    assert len(colorclass.codes.BASE_CODES) == len(codes)
