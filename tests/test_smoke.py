from inference_engine.api.server import InferenceServer
from inference_engine.batching.continuous_batcher import BatchItem, ContinuousBatcher
from inference_engine.cache.kv_cache import KVCache
from inference_engine.decoding.speculative import SpeculativeDecoder, SpeculativeDecoderConfig
from inference_engine.quantization.quantize import QuantizationMode, QuantizedModel


def test_server_and_components_bootstrap():
    server = InferenceServer(model_name="demo")
    assert server.run() == "Inference server initialized for demo"

    batcher = ContinuousBatcher(max_batch_size=2)
    batcher.add_request(BatchItem(request_id="1", prompt="hello"))
    assert len(batcher.next_batch()) == 1

    cache = KVCache()
    cache.update("layer_0", [0.1, 0.2])
    assert cache.get("layer_0") == [0.1, 0.2]

    decoder = SpeculativeDecoder(SpeculativeDecoderConfig(draft_tokens=3))
    assert decoder.plan(10) == 3

    quantized = QuantizedModel(QuantizationMode.INT4)
    assert quantized.describe() == "Quantized model using int4"
