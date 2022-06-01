"""
    test of transport tools
"""
import pytest

from modules.transport.transport import TransportLayer
from modules.exceptions import NoProxiesError


def test_transport():
    transport = TransportLayer(headers_list=[])
    transport.set_proxies(['username:pass@109.248.201.166:3128'])

    transport.set_headers([
        {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/123.45 (KHTML, like Gecko) Chrome/0.0.0.0 Safari/123.45"},
    ])


    res = transport.get('http://ifconfig.io/ip', need_proxy=True, need_change_header=True)
    assert res.status_code == 407

    with pytest.raises(NoProxiesError) as e_info:
        transport.set_proxies([])
        res = transport.get('http://ifconfig.io/ip', need_proxy=True, need_change_header=True)
        assert res.status_code == 407

    transport.set_headers([])
    res = transport.get('http://ifconfig.io/ip', need_proxy=False, need_change_header=True)
    assert res.status_code == 200
