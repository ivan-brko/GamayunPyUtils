# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GamayunResult.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='GamayunResult.proto',
  package='gamayun',
  syntax='proto3',
  serialized_options=b'\n\021org.gamayun.protoB\025GamayunResultReporterP\001\242\002\003GMY',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13GamayunResult.proto\x12\x07gamayun\"*\n\tJobResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07results\x18\x02 \x03(\t\"\'\n\x08JobError\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\x0f\n\rEmptyResponse2\x82\x01\n\x06Result\x12<\n\x0cReportResult\x12\x12.gamayun.JobResult\x1a\x16.gamayun.EmptyResponse\"\x00\x12:\n\x0bReportError\x12\x11.gamayun.JobError\x1a\x16.gamayun.EmptyResponse\"\x00\x42\x32\n\x11org.gamayun.protoB\x15GamayunResultReporterP\x01\xa2\x02\x03GMYb\x06proto3'
)




_JOBRESULT = _descriptor.Descriptor(
  name='JobResult',
  full_name='gamayun.JobResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gamayun.JobResult.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='gamayun.JobResult.results', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=74,
)


_JOBERROR = _descriptor.Descriptor(
  name='JobError',
  full_name='gamayun.JobError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='gamayun.JobError.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='gamayun.JobError.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=115,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='gamayun.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['JobResult'] = _JOBRESULT
DESCRIPTOR.message_types_by_name['JobError'] = _JOBERROR
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobResult = _reflection.GeneratedProtocolMessageType('JobResult', (_message.Message,), {
  'DESCRIPTOR' : _JOBRESULT,
  '__module__' : 'GamayunResult_pb2'
  # @@protoc_insertion_point(class_scope:gamayun.JobResult)
  })
_sym_db.RegisterMessage(JobResult)

JobError = _reflection.GeneratedProtocolMessageType('JobError', (_message.Message,), {
  'DESCRIPTOR' : _JOBERROR,
  '__module__' : 'GamayunResult_pb2'
  # @@protoc_insertion_point(class_scope:gamayun.JobError)
  })
_sym_db.RegisterMessage(JobError)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'GamayunResult_pb2'
  # @@protoc_insertion_point(class_scope:gamayun.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)


DESCRIPTOR._options = None

_RESULT = _descriptor.ServiceDescriptor(
  name='Result',
  full_name='gamayun.Result',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=135,
  serialized_end=265,
  methods=[
  _descriptor.MethodDescriptor(
    name='ReportResult',
    full_name='gamayun.Result.ReportResult',
    index=0,
    containing_service=None,
    input_type=_JOBRESULT,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportError',
    full_name='gamayun.Result.ReportError',
    index=1,
    containing_service=None,
    input_type=_JOBERROR,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESULT)

DESCRIPTOR.services_by_name['Result'] = _RESULT

# @@protoc_insertion_point(module_scope)
