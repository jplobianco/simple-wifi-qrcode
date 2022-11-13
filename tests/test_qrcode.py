""" Tests for simple_wifi_qrcode.wifi """

from unittest.mock import patch
import cv2
from simple_wifi_qrcode.qrcode import generate_wifi_qrcode


def test_generate_wifi_qrcode__with__verbose__and__without__random_password(
    capsys,
):
    """Tests generate_wifi_qrcode with verbose and no random password"""

    # GIVEN
    ssid = "net1"
    password = "pass1"
    alg = "WPA"
    verbose = True
    output = "output.png"
    expected = "WIFI:T:WPA;S:net1;P:pass1;H:;"
    expected_verbose_output = f"""QR Code created successfully.
             \n--------------------------------------
             \n  SSID:    \t{ssid}
             \n  Password:\t{password}
             \n--------------------------------------
             \nScan the QR Code with your camera to join {ssid}network.\n"""

    # WHEN
    generate_wifi_qrcode(
        ssid=ssid, password=password, alg=alg, output=output, verbose=verbose
    )
    result = _read_qrcode(output)
    verbose_output = capsys.readouterr().out

    # THEN
    assert expected == result
    assert expected_verbose_output == verbose_output


def test_generate_wifi_qrcode__with__random_password__and__without__verbose(capsys):
    """Tests generate_wifi_qrcode with random password and no verbose"""
    with patch("simple_wifi_qrcode.qrcode._random_hex") as random_hex_mock:
        # GIVEN
        ssid = "net1"
        alg = "WPA"
        verbose = False
        output = "output.png"
        random_hex_password = "0123456789ab"
        random_hex_mock.return_value = random_hex_password
        expected = f"WIFI:T:WPA;S:net1;P:{random_hex_password};H:;"
        expected_verbose_output = ""

        # WHEN
        generate_wifi_qrcode(
            ssid=ssid, alg=alg, output=output, verbose=verbose, random_password=True
        )
        result = _read_qrcode(output)
        verbose_output = capsys.readouterr().out

        # THEN
        assert result == expected
        assert verbose_output == expected_verbose_output


def _read_qrcode(filename: str):
    """Read an image and read the QR code.

    Args:
        filename (string): Path to file

    Returns:
        qr (string): Value from QR code
    """

    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value, _, _ = detect.detectAndDecode(img)
    return value
