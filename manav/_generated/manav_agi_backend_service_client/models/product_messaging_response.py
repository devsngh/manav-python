from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_messaging_response_approved_synonyms_type_0 import (
        ProductMessagingResponseApprovedSynonymsType0,
    )
    from ..models.product_messaging_response_differentiators_type_0_item import (
        ProductMessagingResponseDifferentiatorsType0Item,
    )
    from ..models.product_messaging_response_messaging_pillars_type_0_item import (
        ProductMessagingResponseMessagingPillarsType0Item,
    )
    from ..models.product_messaging_response_proof_points_type_0_item import (
        ProductMessagingResponseProofPointsType0Item,
    )
    from ..models.product_messaging_response_value_propositions_type_0_item import (
        ProductMessagingResponseValuePropositionsType0Item,
    )


T = TypeVar("T", bound="ProductMessagingResponse")


@_attrs_define
class ProductMessagingResponse:
    """
    Attributes:
        id (UUID):
        product_id (UUID):
        version (str):
        is_active (bool):
        positioning_statement (str):
        value_propositions (list[ProductMessagingResponseValuePropositionsType0Item] | None):
        differentiators (list[ProductMessagingResponseDifferentiatorsType0Item] | None):
        proof_points (list[ProductMessagingResponseProofPointsType0Item] | None):
        messaging_pillars (list[ProductMessagingResponseMessagingPillarsType0Item] | None):
        blocked_claims (list[str] | None):
        approved_synonyms (None | ProductMessagingResponseApprovedSynonymsType0):
        authored_by_bot_id (None | UUID):
        approved_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        effective_from (datetime.datetime | None):
        effective_until (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: UUID
    product_id: UUID
    version: str
    is_active: bool
    positioning_statement: str
    value_propositions: list[ProductMessagingResponseValuePropositionsType0Item] | None
    differentiators: list[ProductMessagingResponseDifferentiatorsType0Item] | None
    proof_points: list[ProductMessagingResponseProofPointsType0Item] | None
    messaging_pillars: list[ProductMessagingResponseMessagingPillarsType0Item] | None
    blocked_claims: list[str] | None
    approved_synonyms: None | ProductMessagingResponseApprovedSynonymsType0
    authored_by_bot_id: None | UUID
    approved_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    effective_from: datetime.datetime | None
    effective_until: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_messaging_response_approved_synonyms_type_0 import (
            ProductMessagingResponseApprovedSynonymsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        product_id = str(self.product_id)

        version = self.version

        is_active = self.is_active

        positioning_statement = self.positioning_statement

        value_propositions: list[dict[str, Any]] | None
        if isinstance(self.value_propositions, list):
            value_propositions = []
            for value_propositions_type_0_item_data in self.value_propositions:
                value_propositions_type_0_item = value_propositions_type_0_item_data.to_dict()
                value_propositions.append(value_propositions_type_0_item)

        else:
            value_propositions = self.value_propositions

        differentiators: list[dict[str, Any]] | None
        if isinstance(self.differentiators, list):
            differentiators = []
            for differentiators_type_0_item_data in self.differentiators:
                differentiators_type_0_item = differentiators_type_0_item_data.to_dict()
                differentiators.append(differentiators_type_0_item)

        else:
            differentiators = self.differentiators

        proof_points: list[dict[str, Any]] | None
        if isinstance(self.proof_points, list):
            proof_points = []
            for proof_points_type_0_item_data in self.proof_points:
                proof_points_type_0_item = proof_points_type_0_item_data.to_dict()
                proof_points.append(proof_points_type_0_item)

        else:
            proof_points = self.proof_points

        messaging_pillars: list[dict[str, Any]] | None
        if isinstance(self.messaging_pillars, list):
            messaging_pillars = []
            for messaging_pillars_type_0_item_data in self.messaging_pillars:
                messaging_pillars_type_0_item = messaging_pillars_type_0_item_data.to_dict()
                messaging_pillars.append(messaging_pillars_type_0_item)

        else:
            messaging_pillars = self.messaging_pillars

        blocked_claims: list[str] | None
        if isinstance(self.blocked_claims, list):
            blocked_claims = self.blocked_claims

        else:
            blocked_claims = self.blocked_claims

        approved_synonyms: dict[str, Any] | None
        if isinstance(self.approved_synonyms, ProductMessagingResponseApprovedSynonymsType0):
            approved_synonyms = self.approved_synonyms.to_dict()
        else:
            approved_synonyms = self.approved_synonyms

        authored_by_bot_id: None | str
        if isinstance(self.authored_by_bot_id, UUID):
            authored_by_bot_id = str(self.authored_by_bot_id)
        else:
            authored_by_bot_id = self.authored_by_bot_id

        approved_by_bot_id: None | str
        if isinstance(self.approved_by_bot_id, UUID):
            approved_by_bot_id = str(self.approved_by_bot_id)
        else:
            approved_by_bot_id = self.approved_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        effective_from: None | str
        if isinstance(self.effective_from, datetime.datetime):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str
        if isinstance(self.effective_until, datetime.datetime):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_id": product_id,
                "version": version,
                "is_active": is_active,
                "positioning_statement": positioning_statement,
                "value_propositions": value_propositions,
                "differentiators": differentiators,
                "proof_points": proof_points,
                "messaging_pillars": messaging_pillars,
                "blocked_claims": blocked_claims,
                "approved_synonyms": approved_synonyms,
                "authored_by_bot_id": authored_by_bot_id,
                "approved_by_bot_id": approved_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "effective_from": effective_from,
                "effective_until": effective_until,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_messaging_response_approved_synonyms_type_0 import (
            ProductMessagingResponseApprovedSynonymsType0,  # noqa: PLC0415
        )
        from ..models.product_messaging_response_differentiators_type_0_item import (
            ProductMessagingResponseDifferentiatorsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_response_messaging_pillars_type_0_item import (
            ProductMessagingResponseMessagingPillarsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_response_proof_points_type_0_item import (
            ProductMessagingResponseProofPointsType0Item,  # noqa: PLC0415
        )
        from ..models.product_messaging_response_value_propositions_type_0_item import (
            ProductMessagingResponseValuePropositionsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        product_id = UUID(d.pop("product_id"))

        version = d.pop("version")

        is_active = d.pop("is_active")

        positioning_statement = d.pop("positioning_statement")

        def _parse_value_propositions(data: object) -> list[ProductMessagingResponseValuePropositionsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_propositions_type_0 = []
                _value_propositions_type_0 = data
                for value_propositions_type_0_item_data in _value_propositions_type_0:
                    value_propositions_type_0_item = ProductMessagingResponseValuePropositionsType0Item.from_dict(
                        value_propositions_type_0_item_data
                    )

                    value_propositions_type_0.append(value_propositions_type_0_item)

                return value_propositions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingResponseValuePropositionsType0Item] | None, data)

        value_propositions = _parse_value_propositions(d.pop("value_propositions"))

        def _parse_differentiators(data: object) -> list[ProductMessagingResponseDifferentiatorsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                differentiators_type_0 = []
                _differentiators_type_0 = data
                for differentiators_type_0_item_data in _differentiators_type_0:
                    differentiators_type_0_item = ProductMessagingResponseDifferentiatorsType0Item.from_dict(
                        differentiators_type_0_item_data
                    )

                    differentiators_type_0.append(differentiators_type_0_item)

                return differentiators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingResponseDifferentiatorsType0Item] | None, data)

        differentiators = _parse_differentiators(d.pop("differentiators"))

        def _parse_proof_points(data: object) -> list[ProductMessagingResponseProofPointsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                proof_points_type_0 = []
                _proof_points_type_0 = data
                for proof_points_type_0_item_data in _proof_points_type_0:
                    proof_points_type_0_item = ProductMessagingResponseProofPointsType0Item.from_dict(
                        proof_points_type_0_item_data
                    )

                    proof_points_type_0.append(proof_points_type_0_item)

                return proof_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingResponseProofPointsType0Item] | None, data)

        proof_points = _parse_proof_points(d.pop("proof_points"))

        def _parse_messaging_pillars(data: object) -> list[ProductMessagingResponseMessagingPillarsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messaging_pillars_type_0 = []
                _messaging_pillars_type_0 = data
                for messaging_pillars_type_0_item_data in _messaging_pillars_type_0:
                    messaging_pillars_type_0_item = ProductMessagingResponseMessagingPillarsType0Item.from_dict(
                        messaging_pillars_type_0_item_data
                    )

                    messaging_pillars_type_0.append(messaging_pillars_type_0_item)

                return messaging_pillars_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProductMessagingResponseMessagingPillarsType0Item] | None, data)

        messaging_pillars = _parse_messaging_pillars(d.pop("messaging_pillars"))

        def _parse_blocked_claims(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocked_claims_type_0 = cast(list[str], data)

                return blocked_claims_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        blocked_claims = _parse_blocked_claims(d.pop("blocked_claims"))

        def _parse_approved_synonyms(data: object) -> None | ProductMessagingResponseApprovedSynonymsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                approved_synonyms_type_0 = ProductMessagingResponseApprovedSynonymsType0.from_dict(data)

                return approved_synonyms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductMessagingResponseApprovedSynonymsType0, data)

        approved_synonyms = _parse_approved_synonyms(d.pop("approved_synonyms"))

        def _parse_authored_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authored_by_bot_id_type_0 = UUID(data)

                return authored_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        authored_by_bot_id = _parse_authored_by_bot_id(d.pop("authored_by_bot_id"))

        def _parse_approved_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_bot_id_type_0 = UUID(data)

                return approved_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_bot_id = _parse_approved_by_bot_id(d.pop("approved_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_effective_from(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.datetime.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        effective_from = _parse_effective_from(d.pop("effective_from"))

        def _parse_effective_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.datetime.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        effective_until = _parse_effective_until(d.pop("effective_until"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        product_messaging_response = cls(
            id=id,
            product_id=product_id,
            version=version,
            is_active=is_active,
            positioning_statement=positioning_statement,
            value_propositions=value_propositions,
            differentiators=differentiators,
            proof_points=proof_points,
            messaging_pillars=messaging_pillars,
            blocked_claims=blocked_claims,
            approved_synonyms=approved_synonyms,
            authored_by_bot_id=authored_by_bot_id,
            approved_by_bot_id=approved_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            effective_from=effective_from,
            effective_until=effective_until,
            created_at=created_at,
        )

        product_messaging_response.additional_properties = d
        return product_messaging_response

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
