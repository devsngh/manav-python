from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bucket_stat import BucketStat


T = TypeVar("T", bound="CabinetStructureResponse")


@_attrs_define
class CabinetStructureResponse:
    """The Cabinet UI landing view — buckets + counts.

    Attributes:
        buckets (list[BucketStat]):
        total_templates (int):
    """

    buckets: list[BucketStat]
    total_templates: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets = []
        for buckets_item_data in self.buckets:
            buckets_item = buckets_item_data.to_dict()
            buckets.append(buckets_item)

        total_templates = self.total_templates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buckets": buckets,
                "total_templates": total_templates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bucket_stat import BucketStat  # noqa: PLC0415

        d = dict(src_dict)
        buckets = []
        _buckets = d.pop("buckets")
        for buckets_item_data in _buckets:
            buckets_item = BucketStat.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        total_templates = d.pop("total_templates")

        cabinet_structure_response = cls(
            buckets=buckets,
            total_templates=total_templates,
        )

        cabinet_structure_response.additional_properties = d
        return cabinet_structure_response

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
