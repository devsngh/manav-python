from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_algorithm_name import GraphAlgorithmName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_algorithm_request_params import GraphAlgorithmRequestParams


T = TypeVar("T", bound="GraphAlgorithmRequest")


@_attrs_define
class GraphAlgorithmRequest:
    """
    Attributes:
        workspace_id (str):
        algorithm (GraphAlgorithmName):
        params (GraphAlgorithmRequestParams | Unset):
    """

    workspace_id: str
    algorithm: GraphAlgorithmName
    params: GraphAlgorithmRequestParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        algorithm = self.algorithm.value

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace_id": workspace_id,
                "algorithm": algorithm,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_algorithm_request_params import GraphAlgorithmRequestParams  # noqa: PLC0415

        d = dict(src_dict)
        workspace_id = d.pop("workspace_id")

        algorithm = GraphAlgorithmName(d.pop("algorithm"))

        _params = d.pop("params", UNSET)
        params: GraphAlgorithmRequestParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = GraphAlgorithmRequestParams.from_dict(_params)

        graph_algorithm_request = cls(
            workspace_id=workspace_id,
            algorithm=algorithm,
            params=params,
        )

        graph_algorithm_request.additional_properties = d
        return graph_algorithm_request

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
