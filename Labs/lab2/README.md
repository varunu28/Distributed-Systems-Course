# Lab2
Lab2 for Cmpe273 Distributed Systems course

## Client build to take 2 optional parameters for which the sum is calculated. In absence of parameters default values(1 & 2) will be used. Refer ```output.txt``` for more information. Complete logging present on the server side

## Installation
```
pip install grpcio
pip install grpcio-tools googleapis-common-protos
```

## Command used to generate pb2 files
```
python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. calculator.proto
```
