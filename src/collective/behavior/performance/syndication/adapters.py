# -*- coding: utf-8 -*-
from zope.interface import implementer
from OFS.interfaces import IItem

from zope.component import adapts
from Products.CMFPlone.browser.syndication.adapters import FolderFeed
from Products.CMFPlone.browser.syndication.adapters import BaseItem
from collective.behavior.performance.behavior import IPerformance
from Products.CMFPlone.interfaces.syndication import IFeed
from plone.event.interfaces import IEventAccessor
from plone.app.event.base import dates_for_display

from DateTime import DateTime

class PerformanceItem(BaseItem):
    adapts(IPerformance, IFeed)

    def __init__(self, context, feed):
        self.context = context
        self.feed = feed
        self.startdate = None
        self.enddate = None

        self.performance = IPerformance.providedBy(context)
        self.event_accessor = IEventAccessor(self.context)

        if self.event_accessor:
            self.startdate = self.event_accessor.start
            self.enddate = self.event_accessor.end

    @property
    def start(self):
        date = self.startdate
        if date and date != 'None':
            return DateTime(date)

    @property
    def end(self):
        date = self.enddate
        if date and date != 'None':
            return DateTime(date)

