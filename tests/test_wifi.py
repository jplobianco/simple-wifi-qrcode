""" Tests for simple_wifi_qrcode.wifi """

from simple_wifi_qrcode.wifi import wifi_join_string


def test_wifi_join_string__with__ssid__password__alg():
    # GIVEN
    ssid = "net1"
    password = "pass1"
    alg = "WPA"
    expected = "WIFI:T:WPA;S:net1;P:pass1;H:;"

    # WHEN
    result = wifi_join_string(ssid, password, alg)

    # THEN
    assert result == expected


def test_wifi_join_string__with__ssid__password__and__without__alg():
    # GIVEN
    ssid = "net1"
    password = "pass1"
    expected = "WIFI:T:;S:net1;P:pass1;H:;"

    # WHEN
    result = wifi_join_string(ssid, password)

    # THEN
    assert result == expected
