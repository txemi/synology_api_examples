from typing import Any, Dict, Optional

import yaml
from typeguard import typechecked


@typechecked
def print_api_call_result(msg: str) -> None:
    print(f"\n--- {msg} ---")


@typechecked
def print_api_call_result_yaml(msg: str, result_object: Optional[Dict[str, Any]]) -> None:
    print(f"\n--- {msg} ---")
    print(yaml.dump(result_object, default_flow_style=False, sort_keys=False, allow_unicode=True))


@typechecked
def print_separator(msg: str) -> None:
    print("\n" + "-" * 50)
    print(msg)
