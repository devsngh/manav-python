from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hil_event_resolve_decision_args_type_0 import HILEventResolveDecisionArgsType0


T = TypeVar("T", bound="HILEventResolve")


@_attrs_define
class HILEventResolve:
    """
    Attributes:
        decision (str): approve, edit, or reject
        decision_args (HILEventResolveDecisionArgsType0 | None | Unset):
        decision_note (None | str | Unset):
    """

    decision: str
    decision_args: HILEventResolveDecisionArgsType0 | None | Unset = UNSET
    decision_note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hil_event_resolve_decision_args_type_0 import HILEventResolveDecisionArgsType0  # noqa: PLC0415

        decision = self.decision

        decision_args: dict[str, Any] | None | Unset
        if isinstance(self.decision_args, Unset):
            decision_args = UNSET
        elif isinstance(self.decision_args, HILEventResolveDecisionArgsType0):
            decision_args = self.decision_args.to_dict()
        else:
            decision_args = self.decision_args

        decision_note: None | str | Unset
        if isinstance(self.decision_note, Unset):
            decision_note = UNSET
        else:
            decision_note = self.decision_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decision": decision,
            }
        )
        if decision_args is not UNSET:
            field_dict["decision_args"] = decision_args
        if decision_note is not UNSET:
            field_dict["decision_note"] = decision_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hil_event_resolve_decision_args_type_0 import HILEventResolveDecisionArgsType0  # noqa: PLC0415

        d = dict(src_dict)
        decision = d.pop("decision")

        def _parse_decision_args(data: object) -> HILEventResolveDecisionArgsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                decision_args_type_0 = HILEventResolveDecisionArgsType0.from_dict(data)

                return decision_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HILEventResolveDecisionArgsType0 | None | Unset, data)

        decision_args = _parse_decision_args(d.pop("decision_args", UNSET))

        def _parse_decision_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_note = _parse_decision_note(d.pop("decision_note", UNSET))

        hil_event_resolve = cls(
            decision=decision,
            decision_args=decision_args,
            decision_note=decision_note,
        )

        hil_event_resolve.additional_properties = d
        return hil_event_resolve

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
