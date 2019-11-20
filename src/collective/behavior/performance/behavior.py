#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent
from zope.interface import alsoProvides
from zope.interface import implements
from zope.lifecycleevent import modified
from five import grok
from zope.interface import implementer
from zope.component import adapter
from zope.interface import Interface
from zope.interface import provider
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import implementer
from zope.component import adapter
from plone.supermodel import model
from zope import schema
from collective.behavior.performance import _
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.app.z3cform.widget import AjaxSelectFieldWidget
#
# DataGridFields dependencies
#
#from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow, IDataGridField
#from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridFieldFactory


def safe_value(value):
    try:
        term = None
        if isinstance(value, unicode):
            # no need to use portal encoding for transitional encoding from
            # unicode to ascii. utf-8 should be fine.
            term = value.encode('utf-8')
            return term
        else:
            return value
    except:
        return None

class IProductArrangement(Interface):
    """Marker interface for Product."""

@provider(IFormFieldProvider)
class IProductBehavior(model.Schema):
    model.fieldset(
        'product_arrangement',
        label=_(u'API fields', default=u'API fields'),
        fields=['product_id'],
    )

    product_id = schema.TextLine(
        title=_(u'Product ID', default=u'Product ID'),
        required=False
    )


@provider(IFormFieldProvider)
class IPerformance(model.Schema):
    """Interface for Performance behavior."""

    # performance fieldset
    model.fieldset(
        'performance',
        label=_(u'Sync fields', default=u'Sync fields'),
        fields=['performance_id', 'season', 'event', 'eventType', 'performance_title', 'subtitle', 'tags',
                'performanceStatus', 'onsale', 'startOnlineSalesDate', 'endOnlineSalesDate', 'statusMessage', 'percentageTaken', 'price',
                'performance_availability', 'arrangements'],
    )

    waiting_list = schema.Bool(
        title=_(
            u'Show waiting list button when this performance is sold out',
            default=u'Show waiting list button when this performance is sold out'
        ),
        required=False,
        default=True
    )

    performance_id = schema.TextLine(
        title=_(u'Performance ID', default=u'Performance ID'),
        required=False
    )

    season = schema.TextLine(
        title=_(u'Season', default=u'Season'),
        required=False,
    )
    directives.mode(season="display")

    event = schema.TextLine(
        title=_(u'Event', default=u'Event'),
        required=False,
    )
    directives.mode(event="display")

    eventType = schema.TextLine(
        title=_(u'Event type', default=u'Event type'),
        required=False,
    )
    directives.mode(eventType="display")

    performance_title = schema.TextLine(
        title=_(u'Title', default=u'Title'),
        required=False,
    )
    directives.mode(performance_title="display")

    subtitle = schema.TextLine(
        title=_(u'Subtitle', default=u'Subtitle'),
        required=False,
    )
    directives.mode(subtitle="display")

    tags = schema.Tuple(
        title=_(u'Tags', default=u'Tags'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'tags',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )
    directives.mode(tags="display")

    performanceStatus = schema.TextLine(
        title=_(u'Performance status', default=u'Performance status'),
        required=False,
    )
    directives.mode(performanceStatus="display")

    onsale = schema.Bool(
        title=_(
            u'Onsale',
            default=u'Onsale'
        ),
        required=False,
        default=False
    )
    directives.mode(onsale="display")

    startOnlineSalesDate = schema.TextLine(
        title=_(u'Start online sales date', default=u'Start online sales date'),
        required=False,
    )
    directives.mode(startOnlineSalesDate="display")

    endOnlineSalesDate = schema.TextLine(
        title=_(u'End online sales date', default=u'End online sales date'),
        required=False,
    )
    directives.mode(endOnlineSalesDate="display")

    statusMessage = schema.TextLine(
        title=_(u'Status message', default=u'Status message'),
        required=False
    )
    directives.mode(statusMessage="display")

    percentageTaken = schema.TextLine(
        title=_(u'Percentage taken', default=u'Percentage taken'),
        required=False
    )
    directives.mode(percentageTaken="display")

    price = RichTextField(
        title=_(u'Price'),
        description=u'',
        required=False
    )
    directives.widget('price', RichTextFieldWidget)
    directives.mode(price="display")

    performance_availability = RichTextField(
        title=_(u'Performance availability'),
        description=u'',
        required=False
    )
    directives.widget('performance_availability', RichTextFieldWidget)
    directives.mode(performance_availability="display")

    arrangements = RichTextField(
        title=_(u'Arragementen'),
        description=u'',
        required=False
    )
    directives.widget('arrangements', RichTextFieldWidget)
    directives.mode(arrangements="display")


@indexer(IPerformance)
def performance_id(object, **kw):
    try:
        if getattr(object, 'portal_type', None) == "Event":
            if hasattr(object, 'performance_id'):
                value = object.performance_id
                if value:
                    return value.lower()
                else:
                    return ""
            else:
                return ""
        else:
            return ""
    except:
        return ""

@indexer(IProductArrangement)
def product_id(object, **kw):
    try:
        if hasattr(object, 'product_id'):
            value = object.product_id
            if value:
                return value.lower()
            else:
                return ""
        else:
            return ""
    except:
        return ""


@indexer(IPerformance)
def onsale(object, **kw):
    try:
        if getattr(object, 'portal_type', None) == "Event":
            if hasattr(object, 'onsale'):
                value = object.onsale
                return value
            else:
                return False
        else:
            return False
    except:
        return False



        





