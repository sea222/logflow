from typing import Generic, List, TypeVar

from .emitter import Emitter, FunctionEmitter
from .sink import Sink
from .source import Source
from .stage import Stage

R = TypeVar("R")


class Pipeline(Generic[R]):
    """Source -> [Stage ...] -> Sink. Bu hafta ara stage yok."""

    def __init__(self, source: Source[R], sink: Sink[R]) -> None:
        self._source = source
        self._sink = sink
        self._stages: List[Stage[R, R]] = []

    def add_stage(self, stage: Stage[R, R]) -> "Pipeline[R]":
        self._stages.append(stage)
        return self

    def run(self) -> None:
        for s in self._stages:
            s.open()
        try:
            # Zinciri sondan basa kur: sink <- stage[n-1] <- ... <- stage[0]
            head: Emitter[R] = FunctionEmitter(self._sink.consume)
            for stage in reversed(self._stages):
                head = FunctionEmitter(self._make_link(stage, head))
            self._source.produce(head)
        finally:
            for s in reversed(self._stages):
                s.close()

    @staticmethod
    def _make_link(stage: Stage[R, R], nxt: Emitter[R]):
        return lambda item: stage.process(item, nxt)
