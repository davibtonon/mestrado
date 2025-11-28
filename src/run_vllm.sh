#!/bin/bash

MODEL_LIST=("microsoft/Phi-3-mini-4k-instruct" "meta-llama/Llama-3.2-1B" "Qwen/Qwen3-0.6B")

MODEL_INDEX=${1:-0}
MODEL=${MODEL_LIST[$MODEL_INDEX]}

echo "Execuntando o modelo: $MODEL"

docker run --rm \
  --security-opt seccomp=unconfined \
  --cap-add SYS_NICE \
  --shm-size=4g \
  -p 8000:8000 \
  -e VLLM_CPU_KVCACHE_SPACE=8 \
  -e VLLM_CPU_OMP_THREADS_BIND=4 \
  --env "HUGGING_FACE_HUB_TOKEN=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" \
  vllm-cpu-env \
  --model="$MODEL" \
  --dtype=auto \
  --trust-remote-code \
  --chat-template ./tool_chat_template_llama3.2_json.jinja
#--cpu-offload-gb 12
