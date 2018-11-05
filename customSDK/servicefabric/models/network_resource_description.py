# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NetworkResourceDescription(Model):
    """This type describes a network resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the Network resource.
    :type name: str
    :param properties: Required. Describes properties of a network resource.
    :type properties: ~azure.servicefabric.models.NetworkResourceProperties
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'NetworkResourceProperties'},
    }

    def __init__(self, **kwargs):
        super(NetworkResourceDescription, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
