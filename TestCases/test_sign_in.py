import pytest

from Features.PageObjects.Homepage import Homepage
from Features.PageObjects.HotDeals import HotDeals
from TestCases.BaseTest import BaseTest


class TestSignIn(BaseTest):


    def test_signin(self):
        hp=Homepage(self.driver)
        hd=hp.navigation_check()
        hd.accept_cookies()
