# -*- coding: utf-8 -*-

from .behavior import IProductArrangement, IProductBehavior
from plone import api
from Products.Five.browser import BrowserView
from zope.container.interfaces import IContainer
from zope.interface import alsoProvides
from zope.interface import noLongerProvides

class EnableDisableFeature(BrowserView):
    feature_iface = None
    enable_message = None
    disable_message = None

    def enableProduct(self):
        alsoProvides(self.context, self.feature_iface)
        cat = api.portal.get_tool("portal_catalog")
        cat.reindexObject(self.context, idxs=["object_provides"], update_metadata=1)
        api.portal.show_message(message=self.enable_message, request=self.request)
        self.request.response.redirect(self.context.absolute_url())

    def disableProduct(self):
        noLongerProvides(self.context, self.feature_iface)
        cat = api.portal.get_tool("portal_catalog")
        cat.reindexObject(self.context, idxs=["object_provides"], update_metadata=1)
        api.portal.show_message(message=self.disable_message, request=self.request)
        self.request.response.redirect(self.context.absolute_url())

class ProductAction(EnableDisableFeature):
    feature_iface = IProductArrangement
    enable_message = "Product API fields are enabled."
    disable_message = "Product API fields are disabled."


