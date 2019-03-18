"""Tests for certbot_dns_powerdns.dns_powerdns"""

import os
import unittest

import mock
from requests.exceptions import HTTPError

from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.plugins.dns_test_common import DOMAIN

from certbot.tests import util as test_util

API_TOKEN = '00000000-0000-0000-0000-000000000000'
API_URL = 'https://127.0.0.1'


class AuthenticatorTest(test_util.TempDirTestCase,
                        dns_test_common_lexicon.BaseLexiconAuthenticatorTest):

    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        from certbot_dns_powerdns.dns_powerdns import Authenticator

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write(
            {"powerdns_api_url": API_URL,
             "powerdns_api_key": API_TOKEN},
            path
        )

        print("File content")
        print(open(path).read())

        self.config = mock.MagicMock(powerdns_credentials=path,
                                     powerdns_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "powerdns")

        self.mock_client = mock.MagicMock()
        # _get_powerdns_client | pylint: disable=protected-access
        self.auth._get_powerdns_client = mock.MagicMock(return_value=self.mock_client)


class PowerDnsLexiconClientTest(unittest.TestCase,
                                dns_test_common_lexicon.BaseLexiconClientTest):
    DOMAIN_NOT_FOUND = HTTPError('422 Client Error: Unprocessable Entity for url: {0}.'.format(DOMAIN))
    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized')

    def setUp(self):
        from certbot_dns_powerdns.dns_powerdns import _PowerDNSLexiconClient

        self.client = _PowerDNSLexiconClient(api_key=API_TOKEN, api_url=API_URL, ttl=0)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
