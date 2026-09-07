from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrySyncResponse")


@_attrs_define
class RegistrySyncResponse:
    """
    Attributes:
        skills (int):
        guardrails (int):
        policies (int):
        formulas (int):
        agents (int):
        message (str):
        errors (int | Unset):  Default: 0.
    """

    skills: int
    guardrails: int
    policies: int
    formulas: int
    agents: int
    message: str
    errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skills = self.skills

        guardrails = self.guardrails

        policies = self.policies

        formulas = self.formulas

        agents = self.agents

        message = self.message

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "skills": skills,
                "guardrails": guardrails,
                "policies": policies,
                "formulas": formulas,
                "agents": agents,
                "message": message,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        skills = d.pop("skills")

        guardrails = d.pop("guardrails")

        policies = d.pop("policies")

        formulas = d.pop("formulas")

        agents = d.pop("agents")

        message = d.pop("message")

        errors = d.pop("errors", UNSET)

        registry_sync_response = cls(
            skills=skills,
            guardrails=guardrails,
            policies=policies,
            formulas=formulas,
            agents=agents,
            message=message,
            errors=errors,
        )

        registry_sync_response.additional_properties = d
        return registry_sync_response

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
