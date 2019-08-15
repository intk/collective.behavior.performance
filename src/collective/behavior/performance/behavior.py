#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form
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
from plone.directives import dexterity, form
from plone.indexer.decorator import indexer
from plone.app.textfield import RichText as RichTextField
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from collective import dexteritytextindexer
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

@provider(IFormFieldProvider)
class IPerformance(model.Schema):
    """Interface for Performance behavior."""

    # performance fieldset
    model.fieldset(
        'performance',
        label=_(u'Performance fields', default=u'Performance fields'),
        fields=['performance_id', 'season', 'eventType', 'performance_title', 'subtitle', 'tags', 'facilityCode',
        'performanceStatus', 'onsale', 'startOnlineSalesDate', 'endOnlineSalesDate', 'statusMessage', 'percentageTaken', 'price'],
    )

    performance_id = schema.TextLine(
        title=_(u'Performance ID', default=u'Performance ID'),
        required=False
    )

    season = schema.TextLine(
        title=_(u'Season', default=u'Season'),
        required=False
    )

    eventType = schema.TextLine(
        title=_(u'Event type', default=u'Event type'),
        required=False
    )

    performance_title = schema.TextLine(
        title=_(u'Title', default=u'Title'),
        required=False
    )

    subtitle = schema.TextLine(
        title=_(u'Subtitle', default=u'Subtitle'),
        required=False
    )

    tags = schema.Tuple(
        title=_(u'Tags', default=u'Tags'),
        description=_(
            u'Tags',
            default=u'Tags'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'tags',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    facilityCode = schema.TextLine(
        title=_(u'Facility', default=u'Facility'),
        required=False
    )

    performanceStatus = schema.TextLine(
        title=_(u'Performance status', default=u'Performance status'),
        required=False
    )

    onsale = schema.Bool(
        title=_(
            u'Onsale',
            default=u'Onsale'
        ),
        description=_(
            u'Onsale',
            default=u'Onsale'
        ),
        required=False,
        default=False
    )

    startOnlineSalesDate = schema.TextLine(
        title=_(u'Start online sales date', default=u'Start online sales date'),
        required=False
    )

    endOnlineSalesDate = schema.TextLine(
        title=_(u'End online sales date', default=u'End online sales date'),
        required=False
    )

    statusMessage = schema.TextLine(
        title=_(u'Status message', default=u'Status message'),
        required=False
    )

    percentageTaken = schema.TextLine(
        title=_(u'Percentage taken', default=u'Percentage taken'),
        required=False
    )

    price = RichTextField(
        title=_(u'Text'),
        description=u'',
        required=False,
    )
    form.widget('price', RichTextFieldWidget)



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



        





