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

from .health_evaluation_py3 import HealthEvaluation


class EventHealthEvaluation(HealthEvaluation):
    """Represents health evaluation of a HealthEvent that was reported on the
    entity.
    The health evaluation is returned when evaluating health of an entity
    results in Error or Warning.

    All required parameters must be populated in order to send to Azure.

    :param aggregated_health_state: The health state of a Service Fabric
     entity such as Cluster, Node, Application, Service, Partition, Replica
     etc. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error',
     'Unknown'
    :type aggregated_health_state: str or
     ~azure.servicefabric.models.HealthState
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param consider_warning_as_error: Indicates whether warnings are treated
     with the same severity as errors. The field is specified in the health
     policy used to evaluate the entity.
    :type consider_warning_as_error: bool
    :param unhealthy_event: Represents health information reported on a health
     entity, such as cluster, application or node, with additional metadata
     added by the Health Manager.
    :type unhealthy_event: ~azure.servicefabric.models.HealthEvent
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'consider_warning_as_error': {'key': 'ConsiderWarningAsError', 'type': 'bool'},
        'unhealthy_event': {'key': 'UnhealthyEvent', 'type': 'HealthEvent'},
    }

    def __init__(self, *, aggregated_health_state=None, description: str=None, consider_warning_as_error: bool=None, unhealthy_event=None, **kwargs) -> None:
        super(EventHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description, **kwargs)
        self.consider_warning_as_error = consider_warning_as_error
        self.unhealthy_event = unhealthy_event
        self.kind = 'Event'
