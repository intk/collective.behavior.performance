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
        fields=['performance_id'],
    )

    performance_id = schema.TextLine(
        title=_(u'Performance ID', default=u'Performance ID'),
        required=False
    )


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



        





