from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_messaging_create_approved_synonyms_type_0 import ProductMessagingCreateApprovedSynonymsType0
    from ..models.product_messaging_create_differentiators_type_0_item import (
        ProductMessagingCreateDifferentiatorsType0Item,
    )
    from ..models.product_messaging_create_messaging_pillars_type_0_item import (
        ProductMessagingCreateMessagingPillarsType0Item,
    )
    from ..models.product_messaging_create_proof_points_type_0_item import ProductMessagingCreateProofPointsType0Item
    from ..models.product_messaging_create_value_propositions_type_0_item import (
        ProductMessagingCreateValuePropositionsType0Item,
    )


T = TypeVar("T", bound="ProductMessagingCreate")


@_attrs_define
class ProductMessagingCreate:
    """
    Attributes:
        version (str):
        positioning_statement (str):
        value_propositions (list[ProductMessagingCreateValuePropositionsType0Item] | None | Unset):
        differentiators (list[ProductMessagingCreateDifferentiatorsType0Item] | None | Unset):
        proof_points (list[ProductMessagingCreateProofPointsType0Item] | None | Unset):
        messaging_pillars (list[ProductMessagingCreateMessagingPillarsType0Item] | None | Unset):
        blocked_claims (list[str] | None | Unset):
        approved_synonyms (None | ProductMessagingCreateApprovedSynonymsType0 | Unset):
        effective_from (datetime.datetime | None | Unset):
        effective_until (datetime.datetime | None | Unset):
    """

    version: str
    positioning_statement: str
    value_propositions: list[ProductMessagingCreateValuePropositionsType0Item] | None | Unset = UNSET
    differentiators: list[ProductMessagingCreateDifferentiatorsType0Item] | None | Unset = UNSET
    proof_points: list[ProductMessagingCreateProofPointsType0Item] | None | Unset = UNSET
    messaging_pillars: list[ProductMessagingCreateMessagingPillarsType0Item] | None | Unset = UNSET
    blocked_claims: list[str] | None | Unset = UNSET
    approved_synonyms: None | ProductMessagingCreateApprovedSynonymsType0 | Unset = UNSET
    effective_from: datetime.datetime | None | Unset = UNSET
    effective_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_messaging_create_approved_synonyms_type_0 import (
            ProductMessagingCreateApprovedSynonymsType0,  # noqa: PLC0415
        )

        version = self.version

        positioning_statement = self.positioning_statement

        value_propositions: list[dict[str, Any]] | None | Unset
        if isinstance(self.value_propositions, Unset):
            value_propositions = UNSET
        elif isinstance(self.value_propositions, list):
            value_propositions = []
            for value_propositions_type_0_item_data in self.value_propositions:
                value_propositions_type_0_item = value_propositions_type_0_item_data.to_dict()
                value_propositions.append(value_propositions_type_0_item)

        else:
            value_propositions = self.value_propositions

        differentiators: list[dict[str, Any]] | None | Unset
        if isinstance(self.differentiators, Unset):
            differentiators = UNSET
        elif isinstance(self.differentiators, list):
            differentiators = []
            for differentiators_type_0_item_data in self.differentiators:
                differentiators_type_0_item = differentiators_type_0_item_data.to_dict()
                differentiators.append(differentiators_type_0_item)

        else:
            differentiators = self.differentiators

        proof_points: list[dict[str, Any]] | None | Unset
        if isinstance(self.proof_points, Unset):
            proof_points = UNSET
        elif isinstance(self.proof_points, list):
            proof_points = []
            for proof_points_type_0_item_data in self.proof_points:
                proof_points_type_0_item = proof_points_type_0_item_data.to_dict()
                proof_points.append(proof_points_type_0_item)

        else:
            proof_points = self.proof_points

        messaging_pillars: list[dict[str, Any]] | None | Unset
        if isinstance(self.messaging_pillars, Unset):
            messaging_pillars = UNSET
        elif isinstance(self.messaging_pillars, list):
            messaging_pillars = []
            for messaging_pillars_type_0_item_data in self.messaging_pillars:
                messaging_pillars_type_0_item = messaging_pillars_type_0_item_data.to_dict()
                messaging_pillars.append(messaging_pillars_type_0_item)

        else:
            messaging_pillars = self.messaging_pillars

        blocked_claims: list[str] | None | Unset
        if isinstance(self.blocked_claims, Unset):
            blocked_claims = UNSET
        elif isinstance(self.blocked_claims, list):
            blocked_claims = self.blocked_claims

        else:
            blocked_claims = self.blocked_claims

        approved_synonyms: dict[str, Any] | None | Unset
        if isinstance(self.approved_synonyms, Unset):
            approved_synonyms = UNSET
        elif isinstance(self.approved_synonyms, ProductMessagingCreateApprovedSynonymsType0):
            approved_synonyms = self.approved_synonyms.to_dict()
        else:
            approved_synonyms = self.approved_synonyms

        effective_from: None | str | Unset
        if isinstance(self.effective_from, Unset):
            effective_from = UNSET
        elif isinstance(self.effective_from, datetime.datetime):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str | Unset
        if isinstance(self.effective_until, Unset):
            effective_until = UNSET
        elif isinstance(self.effective_until, datetime.datetime):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "positioning_statement": positioning_statement,
            }
        )
        if value_propositions is not UNSET:
            field_dict["value_propositions"] = value_propositions
        if differentiators is not UNSET:
            field_dict["differentiators"] = differentiators
        if proof_points is not UNSET:
            field_dict["proof_points"] = proof_points
        if messaging_pillars is not UNSET:
            field_dict["messaging_pillars"] = messaging_pillars
        if blocked_claims is not UNSET:
            field_dict["blocked_claims"] = blocked_claims
        if approved_synonyms is not UNSET:
            field_dict["approved_synonyms"] = approved_synonyms
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from
        if effective_until is not UNSET:
            field_dict["effective_until"] = effective_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_messaging_create_approved_synonyms_type_0 import (
            ProductMessagingCreateApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.product_messaging_create_differentiators_type_0_item import (
            ProductMessagingCreateDifferentiatorsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_create_messaging_pillars_type_0_item import (
            ProductMessagingCreateMessagingPillarsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_create_proof_points_type_0_item import (
            ProductMessagingCreateProofPointsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_create_value_propositions_type_0_item import (
            ProductMessagingCreateValuePropositionsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        positioning_statement = d.pop("positioning_statement")

        def _parse_value_propositions(
            data: object,
        ) -> list[ProductMessagingCreateValuePropositionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_propositions_type_0 = []
                _value_propositions_type_0 = data
                for value_propositions_type_0_item_data in _value_propositions_type_0:
                    value_propositions_type_0_item = ProductMessagingCreateValuePropositionsType0Item.from_dict(
                        value_propositions_type_0_item_data
                    )

                    value_propositions_type_0.append(value_propositions_type_0_item)

                return value_propositions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingCreateValuePropositionsType0Item] | None | Unset, data)

        value_propositions = _parse_value_propositions(d.pop("value_propositions", UNSET))

        def _parse_differentiators(data: object) -> list[ProductMessagingCreateDifferentiatorsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                differentiators_type_0 = []
                _differentiators_type_0 = data
                for differentiators_type_0_item_data in _differentiators_type_0:
                    differentiators_type_0_item = ProductMessagingCreateDifferentiatorsType0Item.from_dict(
                        differentiators_type_0_item_data
                    )

                    differentiators_type_0.append(differentiators_type_0_item)

                return differentiators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingCreateDifferentiatorsType0Item] | None | Unset, data)

        differentiators = _parse_differentiators(d.pop("differentiators", UNSET))

        def _parse_proof_points(data: object) -> list[ProductMessagingCreateProofPointsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                proof_points_type_0 = []
                _proof_points_type_0 = data
                for proof_points_type_0_item_data in _proof_points_type_0:
                    proof_points_type_0_item = ProductMessagingCreateProofPointsType0Item.from_dict(
                        proof_points_type_0_item_data
                    )

                    proof_points_type_0.append(proof_points_type_0_item)

                return proof_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingCreateProofPointsType0Item] | None | Unset, data)

        proof_points = _parse_proof_points(d.pop("proof_points", UNSET))

        def _parse_messaging_pillars(
            data: object,
        ) -> list[ProductMessagingCreateMessagingPillarsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messaging_pillars_type_0 = []
                _messaging_pillars_type_0 = data
                for messaging_pillars_type_0_item_data in _messaging_pillars_type_0:
                    messaging_pillars_type_0_item = ProductMessagingCreateMessagingPillarsType0Item.from_dict(
                        messaging_pillars_type_0_item_data
                    )

                    messaging_pillars_type_0.append(messaging_pillars_type_0_item)

                return messaging_pillars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingCreateMessagingPillarsType0Item] | None | Unset, data)

        messaging_pillars = _parse_messaging_pillars(d.pop("messaging_pillars", UNSET))

        def _parse_blocked_claims(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_claims_type_0 = cast(list[str], data)

                return blocked_claims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocked_claims = _parse_blocked_claims(d.pop("blocked_claims", UNSET))

        def _parse_approved_synonyms(data: object) -> None | ProductMessagingCreateApprovedSynonymsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approved_synonyms_type_0 = ProductMessagingCreateApprovedSynonymsType0.from_dict(data)

                return approved_synonyms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductMessagingCreateApprovedSynonymsType0 | Unset, data)

        approved_synonyms = _parse_approved_synonyms(d.pop("approved_synonyms", UNSET))

        def _parse_effective_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.datetime.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        effective_from = _parse_effective_from(d.pop("effective_from", UNSET))

        def _parse_effective_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.datetime.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        effective_until = _parse_effective_until(d.pop("effective_until", UNSET))

        product_messaging_create = cls(
            version=version,
            positioning_statement=positioning_statement,
            value_propositions=value_propositions,
            differentiators=differentiators,
            proof_points=proof_points,
            messaging_pillars=messaging_pillars,
            blocked_claims=blocked_claims,
            approved_synonyms=approved_synonyms,
            effective_from=effective_from,
            effective_until=effective_until,
        )

        product_messaging_create.additional_properties = d
        return product_messaging_create

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
