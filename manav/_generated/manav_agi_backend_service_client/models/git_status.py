from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitStatus")


@_attrs_define
class GitStatus:
    """
    Attributes:
        branch (str):
        ahead (int | Unset):  Default: 0.
        behind (int | Unset):  Default: 0.
        staged (list[str] | Unset):
        unstaged (list[str] | Unset):
        untracked (list[str] | Unset):
        has_conflicts (bool | Unset):  Default: False.
    """

    branch: str
    ahead: int | Unset = 0
    behind: int | Unset = 0
    staged: list[str] | Unset = UNSET
    unstaged: list[str] | Unset = UNSET
    untracked: list[str] | Unset = UNSET
    has_conflicts: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        ahead = self.ahead

        behind = self.behind

        staged: list[str] | Unset = UNSET
        if not isinstance(self.staged, Unset):
            staged = self.staged

        unstaged: list[str] | Unset = UNSET
        if not isinstance(self.unstaged, Unset):
            unstaged = self.unstaged

        untracked: list[str] | Unset = UNSET
        if not isinstance(self.untracked, Unset):
            untracked = self.untracked

        has_conflicts = self.has_conflicts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
            }
        )
        if ahead is not UNSET:
            field_dict["ahead"] = ahead
        if behind is not UNSET:
            field_dict["behind"] = behind
        if staged is not UNSET:
            field_dict["staged"] = staged
        if unstaged is not UNSET:
            field_dict["unstaged"] = unstaged
        if untracked is not UNSET:
            field_dict["untracked"] = untracked
        if has_conflicts is not UNSET:
            field_dict["has_conflicts"] = has_conflicts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch")

        ahead = d.pop("ahead", UNSET)

        behind = d.pop("behind", UNSET)

        staged = cast(list[str], d.pop("staged", UNSET))

        unstaged = cast(list[str], d.pop("unstaged", UNSET))

        untracked = cast(list[str], d.pop("untracked", UNSET))

        has_conflicts = d.pop("has_conflicts", UNSET)

        git_status = cls(
            branch=branch,
            ahead=ahead,
            behind=behind,
            staged=staged,
            unstaged=unstaged,
            untracked=untracked,
            has_conflicts=has_conflicts,
        )

        git_status.additional_properties = d
        return git_status

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
