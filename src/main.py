from collections import deque
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InverseInput(BaseModel):
    N: int
    Input: list[int]


def inverse(inputs: list[int], n: int) -> list[int]:
    res = deque()
    multiples = []
    for index, value in enumerate(inputs):
        if not value % n:
            multiples.append((index, value))
        else:
            res.appendleft(value)
    for index, value in multiples:
        res.insert(index, value)
    return list(res)


@app.post("/inverse")
async def inverser(inverse_input: InverseInput) -> list[int]:
    return inverse(inverse_input.Input, inverse_input.N)
