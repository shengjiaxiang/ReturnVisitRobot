from transitions.core import Event, Machine
from typing import Any, Dict, ContextManager, Literal, Optional, Type, List, DefaultDict, Union, Callable
from types import TracebackType
from logging import Logger
from threading import Lock

from ..core import StateIdentifier, State

_LOGGER: Logger


class PicklableLock(ContextManager):
    lock: Lock
    def __init__(self) -> None: ...
    def __getstate__(self) -> Dict[str, Any]: ...
    def __setstate__(self, value: Dict[str, Any]) -> PicklableLock: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None: ...

class IdentManager(ContextManager):
    current: int
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]) -> None: ...

class LockedEvent(Event):
    machine: LockedMachine
    def trigger(self, model: object, *args: List, **kwargs: Dict[str, Any]) -> bool: ...


class LockedMachine(Machine):
    event_cls: Type[LockedEvent]
    _ident: IdentManager
    machine_context: List[ContextManager]
    model_context_map: DefaultDict[int, List[ContextManager]]
    def __init__(self, *args: List, **kwargs: Dict[str, Any]) -> None: ...
    def __getstate__(self) -> Dict[str, Any]: ...
    def __setstate__(self, state: Dict[str, Any]) -> None: ...
    def add_model(self, model:  Union[Union[Literal['self'], object], List[Union[Literal['self'], object]]],
                  initial: Optional[StateIdentifier] = ...,
                  model_context: Optional[Union[ContextManager, List[ContextManager]]] = ...) -> None: ...
    def remove_model(self, model: Union[Union[Literal['self'], object],
                                        List[Union[Literal['self'], object]]]) -> None: ...
    def __getattribute__(self, item: str) -> Any: ...
    def __getattr__(self, item: str) -> Any: ...
    def _add_model_to_state(self, state: State, model: object) -> None: ...
    def _get_qualified_state_name(self, state: State) -> str: ...
    def _locked_method(self, func: Callable, *args: List, **kwargs: Dict[str, Any]) -> Any: ...