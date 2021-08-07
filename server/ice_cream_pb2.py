# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ice_cream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/ice_cream.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15proto/ice_cream.proto\"1\n\x0fIceCreamRequest\x12\x0e\n\x06scoops\x18\x01 \x01(\x05\x12\x0e\n\x06\x66lavor\x18\x02 \x01(\t\"#\n\x10IceCreamResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2@\n\x08IceCream\x12\x34\n\rOrderIceCream\x12\x10.IceCreamRequest\x1a\x11.IceCreamResponseb\x06proto3'
)




_ICECREAMREQUEST = _descriptor.Descriptor(
  name='IceCreamRequest',
  full_name='IceCreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scoops', full_name='IceCreamRequest.scoops', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flavor', full_name='IceCreamRequest.flavor', index=1,
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
  serialized_start=25,
  serialized_end=74,
)


_ICECREAMRESPONSE = _descriptor.Descriptor(
  name='IceCreamResponse',
  full_name='IceCreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='IceCreamResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['IceCreamRequest'] = _ICECREAMREQUEST
DESCRIPTOR.message_types_by_name['IceCreamResponse'] = _ICECREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IceCreamRequest = _reflection.GeneratedProtocolMessageType('IceCreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _ICECREAMREQUEST,
  '__module__' : 'proto.ice_cream_pb2'
  # @@protoc_insertion_point(class_scope:IceCreamRequest)
  })
_sym_db.RegisterMessage(IceCreamRequest)

IceCreamResponse = _reflection.GeneratedProtocolMessageType('IceCreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _ICECREAMRESPONSE,
  '__module__' : 'proto.ice_cream_pb2'
  # @@protoc_insertion_point(class_scope:IceCreamResponse)
  })
_sym_db.RegisterMessage(IceCreamResponse)



_ICECREAM = _descriptor.ServiceDescriptor(
  name='IceCream',
  full_name='IceCream',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=113,
  serialized_end=177,
  methods=[
  _descriptor.MethodDescriptor(
    name='OrderIceCream',
    full_name='IceCream.OrderIceCream',
    index=0,
    containing_service=None,
    input_type=_ICECREAMREQUEST,
    output_type=_ICECREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ICECREAM)

DESCRIPTOR.services_by_name['IceCream'] = _ICECREAM

# @@protoc_insertion_point(module_scope)
