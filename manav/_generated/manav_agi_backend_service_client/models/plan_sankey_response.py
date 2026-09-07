from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sankey_link import SankeyLink
    from ..models.sankey_node import SankeyNode


T = TypeVar("T", bound="PlanSankeyResponse")


@_attrs_define
class PlanSankeyResponse:
    """GET /api/analytics/billing/plan-sankey — from→to tier transitions + churn.

    Attributes:
        nodes (list[SankeyNode]):
        links (list[SankeyLink]):
        window_months (int):
    """

    nodes: list[SankeyNode]
    links: list[SankeyLink]
    window_months: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        window_months = self.window_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
                "links": links,
                "window_months": window_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sankey_link import SankeyLink  # noqa: PLC0415
        from ..models.sankey_node import SankeyNode  # noqa: PLC0415

        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = SankeyNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = SankeyLink.from_dict(links_item_data)

            links.append(links_item)

        window_months = d.pop("window_months")

        plan_sankey_response = cls(
            nodes=nodes,
            links=links,
            window_months=window_months,
        )

        plan_sankey_response.additional_properties = d
        return plan_sankey_response

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
