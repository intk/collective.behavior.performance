from collective.behavior.performance import _
from zope.interface import Attribute
from zope.interface import Interface
from zope.schema import Int
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import implementer
from zope.component import adapter

from Products.CMFPlone.interfaces.syndication import IFeed, IFeedItem

class IPerformancesFeed(IFeed):
	pass

class IPerformanceFeedItem(IFeedItem):
	pass

    

