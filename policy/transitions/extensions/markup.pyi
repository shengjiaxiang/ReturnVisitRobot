import numbers

from ..core import Machine, StateIdentifier, CallbacksArg, StateConfig, Event
from .nesting import HierarchicalMachine
from typing import  List, Dict, Union, Optional, Callable, Tuple, Any

# mypy does not support recursive definitions (yet), we need to use Any instead of 'MarkupConfig'
MarkupConfig = Dict[str, Union[List, str, Any]]

class MarkupMachine(Machine):
    state_attributes: List[str]
    transition_attributes: List[str]
    _markup: MarkupConfig
    _auto_transitions_markup: bool
    _needs_update: bool
    def __init__(self, *args: List, **kwargs: Dict[str, Any]) -> None: ...
    @property
    def auto_transitions_markup(self) -> bool: ...
    @auto_transitions_markup.setter
    def auto_transitions_markup(self, value: bool) -> None: ...
    @property
    def markup(self) -> MarkupConfig: ...
    def get_markup_config(self) -> MarkupConfig: ...
    def add_transition(self, trigger: str,
                       source: Union[StateIdentifier, List[StateIdentifier]],
                       dest: StateIdentifier, conditions: CallbacksArg = ..., unless: CallbacksArg = ...,
                       before: CallbacksArg = ..., after: CallbacksArg = ..., prepare: CallbacksArg = ...,
                       **kwargs: Dict[str, Any]) -> None: ...
    def add_states(self, states: Union[List[StateConfig], StateConfig],
                   on_enter: CallbacksArg = ..., on_exit: CallbacksArg = ...,
                   ignore_invalid_triggers: Optional[bool] = ..., **kwargs: Dict[str, Any]) -> None: ...
    @staticmethod
    def format_references(func: Callable) -> str: ...
    def _convert_states_and_transitions(self, root: MarkupConfig) -> None: ...
    def _convert_states(self, root: MarkupConfig) -> None: ...
    def _convert_transitions(self, root: MarkupConfig) -> None: ...
    def _add_markup_model(self, markup: MarkupConfig) -> None: ...
    def _convert_models(self) -> List[Dict[str, str]]: ...
    def _omit_auto_transitions(self, event: Event) -> bool: ...
    def _is_auto_transition(self, event: Event) -> bool: ...
    def _identify_callback(self, name: str) -> Tuple[Optional[str], Optional[str]]: ...


class HierarchicalMarkupMachine(MarkupMachine, HierarchicalMachine):  # type: ignore
    pass


def rep(func: Union[Callable, str, numbers.Number],
        format_references: Optional[Callable] = ...) -> str: ...
def _convert(obj: object, attributes: List[str], format_references: Optional[Callable]) -> MarkupConfig: ...
