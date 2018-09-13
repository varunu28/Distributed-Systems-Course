from concurrent import futures

import calculator_pb2
import calculator_pb2_grpc
import time
import grpc

class Calculator(calculator_pb2_grpc.calculatorServicer):

    def sum(self, request, context):
        print(f'Recieved add request for: {request.num1} and {request.num2}')
        return calculator_pb2.SumResponse(res=request.num1 + request.num2)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_calculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port("[::]:8000")
    print("Starting server on port: " + str(8000))
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()