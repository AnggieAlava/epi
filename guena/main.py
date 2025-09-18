from contextlib import contextmanager
from functools import lru_cache
from itertools import batched
from time import perf_counter

import typer
from typing import Iterable, Any
from typing_extensions import Annotated

app = typer.Typer()


@contextmanager
def span(name: str):
    start = perf_counter()
    yield
    end = perf_counter()
    print(f"Span {name} took {(end - start) * 1000:.2f} ms.")


# @lru_cache(2)
def fibo(n: int):
    print(f"Calculando {n}")
    if n in [0, 1]:
        return n
    return fibo(n - 2) + fibo(n - 1)


def sequence(n: int):
    return (fibo(i) for i in range(n + 1))


def write(values: Iterable[Any], filename: str, batch_size):
    with open(filename, "w") as f:
        for batch in batched(values, batch_size):
            for item in batch:
                f.write(f"{item}\n")


@app.command("seq")
def list_all(
    n: int,
    filename: Annotated[str | None, typer.Option("--output", "-o")] = None,
    batch_size: Annotated[int, typer.Option("--batch", "-b")] = 200,
):
    with span("total"):
        if filename:
            write(sequence(n), filename, batch_size)
        else:
            for item in sequence(n):
                print(f"{item}")


@app.command("val")
def single(n: int):
    with span("total"):
        _, last_fibo = max(enumerate(sequence(n)))
        print(f"{last_fibo}")


@app.callback(invoke_without_command=True)
def interactive(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        while True:
            n = input("n? ")
            try:
                n = int(n)
                break
            except ValueError:
                pass

        _, last_fibo = max(enumerate(sequence(n)))
        print(f"{last_fibo}")


if __name__ == "__main__":
    app()
