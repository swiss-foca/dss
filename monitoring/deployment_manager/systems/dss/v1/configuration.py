from monitoring.monitorlib.typing import ImplicitDict


class V1DSS(ImplicitDict):
    """Definition of a version 1 DSS instance.

    A v1 DSS system is a DSS instance consisting of CRDB nodes, core-service
    workers, and http-gateway translators, initially defined with Jsonnet in
    build/deploy to be applied to a Kubernetes cluster with Tanka.
    """

    namespace: str = 'default'
    """Namespace in which all DSS components are located"""
