import calculator_pb2
import calculator_pb2_grpc
import grpc
import sys

def run():
    if len(sys.argv) < 2:
        num1 = 1
        num2 = 2
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

    with grpc.insecure_channel('localhost:8000') as channel:
        stub = calculator_pb2_grpc.calculatorStub(channel)
        resp = stub.sum(calculator_pb2.SumRequest(num1=num1, num2=num2))

    print("Sum: " + str(resp.res))

if __name__ == "__main__":
    run()