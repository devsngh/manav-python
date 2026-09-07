from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TerminalExecResponse")


@_attrs_define
class TerminalExecResponse:
    """
    Attributes:
        command (str):
        exit_code (int):
        stdout (str):
        stderr (str):
        cwd (str):
        duration_ms (int):
    """

    command: str
    exit_code: int
    stdout: str
    stderr: str
    cwd: str
    duration_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        exit_code = self.exit_code

        stdout = self.stdout

        stderr = self.stderr

        cwd = self.cwd

        duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "exit_code": exit_code,
                "stdout": stdout,
                "stderr": stderr,
                "cwd": cwd,
                "duration_ms": duration_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        exit_code = d.pop("exit_code")

        stdout = d.pop("stdout")

        stderr = d.pop("stderr")

        cwd = d.pop("cwd")

        duration_ms = d.pop("duration_ms")

        terminal_exec_response = cls(
            command=command,
            exit_code=exit_code,
            stdout=stdout,
            stderr=stderr,
            cwd=cwd,
            duration_ms=duration_ms,
        )

        terminal_exec_response.additional_properties = d
        return terminal_exec_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
