# -*- coding: utf-8 -*-
# Copyright (c) 2023-2025, AgiBot Inc. All Rights Reserved.
# Author: Genie Sim Team
# License: Mozilla Public License Version 2.0

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aimdk/protocol/hal/hand/agi_claw.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'aimdk/protocol/hal/hand/agi_claw.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&aimdk/protocol/hal/hand/agi_claw.proto\x12\x0e\x61imdk.protocol\"g\n\x12\x41giClawHandCommand\x12\x0b\n\x03\x63md\x18\x01 \x01(\r\x12\x0b\n\x03pos\x18\x02 \x01(\r\x12\r\n\x05\x66orce\x18\x03 \x01(\r\x12\x14\n\x0c\x63lamp_method\x18\x04 \x01(\r\x12\x12\n\nfinger_pos\x18\x05 \x01(\r\"W\n\x10\x41giClawHandState\x12\r\n\x05state\x18\x01 \x01(\r\x12\x0b\n\x03pos\x18\x02 \x01(\r\x12\x13\n\x0btemperature\x18\x03 \x01(\r\x12\x12\n\nfinger_pos\x18\x04 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aimdk.protocol.hal.hand.agi_claw_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_AGICLAWHANDCOMMAND']._serialized_start=58
  _globals['_AGICLAWHANDCOMMAND']._serialized_end=161
  _globals['_AGICLAWHANDSTATE']._serialized_start=163
  _globals['_AGICLAWHANDSTATE']._serialized_end=250
# @@protoc_insertion_point(module_scope)
