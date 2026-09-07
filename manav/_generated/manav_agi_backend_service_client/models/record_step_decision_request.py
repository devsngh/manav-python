from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecordStepDecisionRequest")


@_attrs_define
class RecordStepDecisionRequest:
    """
    Attributes:
        decision (str): approved / rejected / delegated / pending
        approver_user_id (None | Unset | UUID):
        approver_bot_id (None | Unset | UUID):
        note (None | str | Unset):
    """

    decision: str
    approver_user_id: None | Unset | UUID = UNSET
    approver_bot_id: None | Unset | UUID = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision = self.decision

        approver_user_id: None | str | Unset
        if isinstance(self.approver_user_id, Unset):
            approver_user_id = UNSET
        elif isinstance(self.approver_user_id, UUID):
            approver_user_id = str(self.approver_user_id)
        else:
            approver_user_id = self.approver_user_id

        approver_bot_id: None | str | Unset
        if isinstance(self.approver_bot_id, Unset):
            approver_bot_id = UNSET
        elif isinstance(self.approver_bot_id, UUID):
            approver_bot_id = str(self.approver_bot_id)
        else:
            approver_bot_id = self.approver_bot_id

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "decision": decision,
            }
        )
        if approver_user_id is not UNSET:
            field_dict["approver_user_id"] = approver_user_id
        if approver_bot_id is not UNSET:
            field_dict["approver_bot_id"] = approver_bot_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decision = d.pop("decision")

        def _parse_approver_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_user_id_type_0 = UUID(data)

                return approver_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approver_user_id = _parse_approver_user_id(d.pop("approver_user_id", UNSET))

        def _parse_approver_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_bot_id_type_0 = UUID(data)

                return approver_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        approver_bot_id = _parse_approver_bot_id(d.pop("approver_bot_id", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        record_step_decision_request = cls(
            decision=decision,
            approver_user_id=approver_user_id,
            approver_bot_id=approver_bot_id,
            note=note,
        )

        record_step_decision_request.additional_properties = d
        return record_step_decision_request

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
