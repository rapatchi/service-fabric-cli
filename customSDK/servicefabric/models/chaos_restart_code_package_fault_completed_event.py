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

from .application_event import ApplicationEvent


class ChaosRestartCodePackageFaultCompletedEvent(ApplicationEvent):
    """Chaos Restart Code Package Fault Completed event.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param application_id: The identity of the application. This is an encoded
     representation of the application name. This is used in the REST APIs to
     identify the application resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the application name is "fabric:/myapp/app1",
     the application identity would be "myapp\\~app1" in 6.0+ and "myapp/app1"
     in previous versions.
    :type application_id: str
    :param fault_group_id: Id of fault group.
    :type fault_group_id: str
    :param fault_id: Id of fault.
    :type fault_id: str
    :param node_name: The name of a Service Fabric node.
    :type node_name: str
    :param service_manifest_name: Service manifest name.
    :type service_manifest_name: str
    :param code_package_name: Code package name.
    :type code_package_name: str
    :param service_package_activation_id: Id of Service package activation.
    :type service_package_activation_id: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'application_id': {'required': True},
        'fault_group_id': {'required': True},
        'fault_id': {'required': True},
        'node_name': {'required': True},
        'service_manifest_name': {'required': True},
        'code_package_name': {'required': True},
        'service_package_activation_id': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'application_id': {'key': 'ApplicationId', 'type': 'str'},
        'fault_group_id': {'key': 'FaultGroupId', 'type': 'str'},
        'fault_id': {'key': 'FaultId', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'service_manifest_name': {'key': 'ServiceManifestName', 'type': 'str'},
        'code_package_name': {'key': 'CodePackageName', 'type': 'str'},
        'service_package_activation_id': {'key': 'ServicePackageActivationId', 'type': 'str'},
    }

    def __init__(self, event_instance_id, time_stamp, application_id, fault_group_id, fault_id, node_name, service_manifest_name, code_package_name, service_package_activation_id, has_correlated_events=None):
        super(ChaosRestartCodePackageFaultCompletedEvent, self).__init__(event_instance_id=event_instance_id, time_stamp=time_stamp, has_correlated_events=has_correlated_events, application_id=application_id)
        self.fault_group_id = fault_group_id
        self.fault_id = fault_id
        self.node_name = node_name
        self.service_manifest_name = service_manifest_name
        self.code_package_name = code_package_name
        self.service_package_activation_id = service_package_activation_id
        self.kind = 'ChaosRestartCodePackageFaultCompleted'
