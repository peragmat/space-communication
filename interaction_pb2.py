# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interaction.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11interaction.proto\"\x88\x03\n\tSpaceship\x12\'\n\talignment\x18\x01 \x01(\x0e\x32\x14.Spaceship.Alignment\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n\nship_class\x18\x03 \x01(\x0e\x32\x14.Spaceship.ShipClass\x12\x0e\n\x06length\x18\x04 \x01(\x02\x12\x11\n\tcrew_size\x18\x05 \x01(\x05\x12\r\n\x05\x61rmed\x18\x06 \x01(\x08\x12$\n\x08officers\x18\x07 \x03(\x0b\x32\x12.Spaceship.Officer\x1a>\n\x07Officer\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x0c\n\x04rank\x18\x03 \x01(\t\" \n\tAlignment\x12\x08\n\x04\x41LLY\x10\x00\x12\t\n\x05\x45NEMY\x10\x01\"`\n\tShipClass\x12\x0c\n\x08\x43ORVETTE\x10\x00\x12\x0b\n\x07\x46RIGATE\x10\x01\x12\x0b\n\x07\x43RUISER\x10\x02\x12\r\n\tDESTROYER\x10\x03\x12\x0b\n\x07\x43\x41RRIER\x10\x04\x12\x0f\n\x0b\x44READNOUGHT\x10\x05\";\n\x0b\x43oordinates\x12\x17\n\x0fright_ascension\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65\x63lination\x18\x02 \x01(\t2E\n\x10ReportingService\x12\x31\n\x13GetSpaceshipEntries\x12\x0c.Coordinates\x1a\n.Spaceship0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'interaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SPACESHIP']._serialized_start=22
  _globals['_SPACESHIP']._serialized_end=414
  _globals['_SPACESHIP_OFFICER']._serialized_start=220
  _globals['_SPACESHIP_OFFICER']._serialized_end=282
  _globals['_SPACESHIP_ALIGNMENT']._serialized_start=284
  _globals['_SPACESHIP_ALIGNMENT']._serialized_end=316
  _globals['_SPACESHIP_SHIPCLASS']._serialized_start=318
  _globals['_SPACESHIP_SHIPCLASS']._serialized_end=414
  _globals['_COORDINATES']._serialized_start=416
  _globals['_COORDINATES']._serialized_end=475
  _globals['_REPORTINGSERVICE']._serialized_start=477
  _globals['_REPORTINGSERVICE']._serialized_end=546
# @@protoc_insertion_point(module_scope)
