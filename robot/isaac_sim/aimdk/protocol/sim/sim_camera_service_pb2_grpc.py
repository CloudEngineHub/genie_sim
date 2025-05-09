# Copyright (c) 2023-2025, AgiBot Inc. All Rights Reserved.
# Author: Genie Sim Team
# License: Mozilla Public License Version 2.0

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from aimdk.protocol.sim import sim_camera_service_pb2 as aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in aimdk/protocol/sim/sim_camera_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SimCameraServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSemanticData = channel.unary_unary(
                '/aimdk.protocol.SimCameraService/GetSemanticData',
                request_serializer=aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticRequest.SerializeToString,
                response_deserializer=aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticResponse.FromString,
                _registered_method=True)


class SimCameraServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSemanticData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimCameraServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSemanticData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSemanticData,
                    request_deserializer=aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticRequest.FromString,
                    response_serializer=aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aimdk.protocol.SimCameraService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('aimdk.protocol.SimCameraService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SimCameraService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSemanticData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/aimdk.protocol.SimCameraService/GetSemanticData',
            aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticRequest.SerializeToString,
            aimdk_dot_protocol_dot_sim_dot_sim__camera__service__pb2.GetSemanticResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
