from inference_engine.api.server import InferenceRequest, InferenceServer


if __name__ == "__main__":
    server = InferenceServer(model_name="demo-model")
    server.add_request(InferenceRequest(prompt="Hello world"))
    print(server.run())
