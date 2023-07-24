# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional

import fire

from llama import Llama

dialogs = [
        [
            {
                "role": "system",
                "content": "provide detailled source code",
            },
            {"role": "user", "content": "Provide detailled code for a simple REST API application that perform CRUD"},
        ],
     ]


def return_results(user_input):
    for dialog, result in zip(dialogs, results):
        for msg in dialog:
            dialogs[0][1]["content"] = user_input

            return str(result['generation']['content'])

def return_res(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    results = generator.chat_completion(
        dialogs,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )



    dialogs[0][1]["content"] = input(" Are you in short of ideas ? please type your doubt in the text box and QGPT will provide you with a sample roadmap to develop your product rapidly and efficiently.")
    for dialog, result in zip(dialogs, results):
            for msg in dialog:
                print(f"{msg['role'].capitalize()}: {msg['content']}\n")
                print(
                f"> {result['generation']['role'].capitalize()}: {result['generation']['content']}")



if __name__ == "__main__":
    fire.Fire(return_res)
