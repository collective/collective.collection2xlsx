# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from collective.collection2xlsx.testing import (  # noqa: E501
    COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING,
)

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.collection2xlsx is properly installed."""

    layer = COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.collection2xlsx is installed."""
        self.assertTrue(self.installer.isProductInstalled("collective.collection2xlsx"))

    def test_browserlayer(self):
        """Test that ICollectiveCollection2XlsxLayer is registered."""
        from plone.browserlayer import utils

        from collective.collection2xlsx.interfaces import (
            ICollectiveCollection2XlsxLayer,
        )

        self.assertIn(ICollectiveCollection2XlsxLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["collective.collection2xlsx"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.collection2xlsx is cleanly uninstalled."""
        self.assertFalse(
            self.installer.isProductInstalled("collective.collection2xlsx")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveCollection2XlsxLayer is removed."""
        from plone.browserlayer import utils

        from collective.collection2xlsx.interfaces import (
            ICollectiveCollection2XlsxLayer,
        )

        self.assertNotIn(ICollectiveCollection2XlsxLayer, utils.registered_layers())
