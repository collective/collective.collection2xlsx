# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import collective.collection2xlsx


class CollectiveCollection2XlsxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.collection2xlsx)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.collection2xlsx:default')


COLLECTIVE_COLLECTION2XLSX_FIXTURE = CollectiveCollection2XlsxLayer()


COLLECTIVE_COLLECTION2XLSX_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_COLLECTION2XLSX_FIXTURE,),
    name='CollectiveCollection2XlsxLayer:IntegrationTesting',
)


COLLECTIVE_COLLECTION2XLSX_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_COLLECTION2XLSX_FIXTURE,),
    name='CollectiveCollection2XlsxLayer:FunctionalTesting',
)


COLLECTIVE_COLLECTION2XLSX_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_COLLECTION2XLSX_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveCollection2XlsxLayer:AcceptanceTesting',
)
