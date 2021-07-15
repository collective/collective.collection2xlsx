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
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_xlsx_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='xlsx'
        )
        self.assertTrue(view.__name__ == 'xlsx')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in xlsx'
        # )

    def test_xlsx_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='xlsx'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = COLLECTIVE_COLLECTION2XLSX_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
