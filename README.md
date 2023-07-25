# QGPT
We leverage the open-source llama2 to build QGPT
## Download pre-trained weights

We downloaded the pre-trained models via this form [request a new download link](https://ai.meta.com/resources/models-and-libraries/llama-downloads/). 


To download the model weights and tokenizer, please visit the [Meta AI website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).


### Access on Hugging Face

This is an alternative link to download the model weights [Hugging Face](https://huggingface.co/meta-llama).

## Setup

In a conda env with PyTorch / CUDA available, clone the repo and run in the top-level directory:

```
pip install -e .
```

## Inference

Different models require different model-parallel (MP) values:

|  Model | MP |
|--------|----|
| 7B     | 1  |


All models support sequence length up to 4096 tokens, but we pre-allocate the cache according to `max_seq_len` and `max_batch_size` values. So set those according to your hardware.

### Pretrained Models

The fine-tuned models are not super good at code, but we finetuned it to support code generation efficiently.


### Fine-tuned Chat Models

The fine-tuned models were trained for dialogue applications. To get the expected features and performance for them, specific formatting defined in [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212)
needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and break lines in between (we recommend calling `strip()` on inputs to avoid double-spaces).

Examples using llama-2-7b-chat:

```
torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir llama-2-7b-chat/ \
    --tokenizer_path tokenizer.model \
    --max_seq_len 512 --max_batch_size 4
```



## References

1. [Research Paper](https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/)
2. [Llama 2 technical overview](https://ai.meta.com/resources/models-and-libraries/llama)
3. [Open Innovation AI Research Community](https://ai.meta.com/llama/open-innovation-ai-research-community/)

## Original LLaMA
The repo for the original llama release is in the [`llama_v1`](https://github.com/facebookresearch/llama/tree/llama_v1) branch.
