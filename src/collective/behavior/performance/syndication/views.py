# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces.syndication import IFeed
from Products.CMFPlone.interfaces.syndication import IFeedSettings
from Products.Five import BrowserView
from zope.component import getMultiAdapter
from zope.component import queryAdapter
from zExceptions import NotFound

class PerformancesFeedView(BrowserView):

    content_type = 'application/atom+xml'

    def feed(self):
        f = queryAdapter(self.context, IFeed)
        if f is None:
            raise NotFound
        return f

    def __call__(self):
        util = getMultiAdapter((self.context, self.request),
                               name='syndication-util')
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        if context_state.is_portal_root() or util.context_enabled(raise404=True):
            settings = IFeedSettings(self.context)
            if self.__name__ not in settings.feed_types:
                raise NotFound
            self.request.response.setHeader('Content-Type', self.content_type)
            return self.index()