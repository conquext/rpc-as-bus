#!/bin/bash

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\proto\ice_cream.proto
# protoc-gen-grpc --js_out=import_style=commonjs,binary:./client/ --grpc_out=./client --proto_path ./proto ./proto/ice_cream.proto
protoc-gen-grpc --js_out=import_style=commonjs,binary:./client/ --grpc_out=./client --proto_path .\proto\ .\proto\ice_cream.proto

# yarn proto-loader-gen-types --grpcLib=@grpc/grpc-js --outDir=proto/ proto/*.proto