# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

from collective.collection2xlsx.testing import (
    COLLECTIVE_COLLECTION2XLSX_FUNCTIONAL_TESTING,
    COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING,
)


class ViewsIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Collection", "collection1")

    def test_xlsx_is_registered(self):
        view = getMultiAdapter(
            (self.portal["collection1"], self.portal.REQUEST), name="xlsx"
        )
        self.assertTrue(view.__name__ == "xlsx")


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_COLLECTION2XLSX_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
