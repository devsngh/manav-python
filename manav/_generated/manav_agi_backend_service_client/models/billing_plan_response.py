from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plan_tier import PlanTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_feature_response import PlanFeatureResponse
    from ..models.plan_quota_response import PlanQuotaResponse


T = TypeVar("T", bound="BillingPlanResponse")


@_attrs_define
class BillingPlanResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        slug (str):
        tier (PlanTier):
        price_monthly_cents (int):
        price_yearly_cents (int):
        credits_included (int):
        max_members (int):
        is_public (bool):
        is_custom (bool):
        sort_order (int):
        description (None | str | Unset):
        stripe_price_id_monthly (None | str | Unset):
        stripe_price_id_yearly (None | str | Unset):
        features (list[PlanFeatureResponse] | Unset):
        quotas (list[PlanQuotaResponse] | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    name: str
    slug: str
    tier: PlanTier
    price_monthly_cents: int
    price_yearly_cents: int
    credits_included: int
    max_members: int
    is_public: bool
    is_custom: bool
    sort_order: int
    description: None | str | Unset = UNSET
    stripe_price_id_monthly: None | str | Unset = UNSET
    stripe_price_id_yearly: None | str | Unset = UNSET
    features: list[PlanFeatureResponse] | Unset = UNSET
    quotas: list[PlanQuotaResponse] | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        slug = self.slug

        tier = self.tier.value

        price_monthly_cents = self.price_monthly_cents

        price_yearly_cents = self.price_yearly_cents

        credits_included = self.credits_included

        max_members = self.max_members

        is_public = self.is_public

        is_custom = self.is_custom

        sort_order = self.sort_order

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        stripe_price_id_monthly: None | str | Unset
        if isinstance(self.stripe_price_id_monthly, Unset):
            stripe_price_id_monthly = UNSET
        else:
            stripe_price_id_monthly = self.stripe_price_id_monthly

        stripe_price_id_yearly: None | str | Unset
        if isinstance(self.stripe_price_id_yearly, Unset):
            stripe_price_id_yearly = UNSET
        else:
            stripe_price_id_yearly = self.stripe_price_id_yearly

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        quotas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = []
            for quotas_item_data in self.quotas:
                quotas_item = quotas_item_data.to_dict()
                quotas.append(quotas_item)

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "tier": tier,
                "price_monthly_cents": price_monthly_cents,
                "price_yearly_cents": price_yearly_cents,
                "credits_included": credits_included,
                "max_members": max_members,
                "is_public": is_public,
                "is_custom": is_custom,
                "sort_order": sort_order,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if stripe_price_id_monthly is not UNSET:
            field_dict["stripe_price_id_monthly"] = stripe_price_id_monthly
        if stripe_price_id_yearly is not UNSET:
            field_dict["stripe_price_id_yearly"] = stripe_price_id_yearly
        if features is not UNSET:
            field_dict["features"] = features
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_feature_response import PlanFeatureResponse  # noqa: PLC0415
        from ..models.plan_quota_response import PlanQuotaResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        slug = d.pop("slug")

        tier = PlanTier(d.pop("tier"))

        price_monthly_cents = d.pop("price_monthly_cents")

        price_yearly_cents = d.pop("price_yearly_cents")

        credits_included = d.pop("credits_included")

        max_members = d.pop("max_members")

        is_public = d.pop("is_public")

        is_custom = d.pop("is_custom")

        sort_order = d.pop("sort_order")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_stripe_price_id_monthly(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_price_id_monthly = _parse_stripe_price_id_monthly(d.pop("stripe_price_id_monthly", UNSET))

        def _parse_stripe_price_id_yearly(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_price_id_yearly = _parse_stripe_price_id_yearly(d.pop("stripe_price_id_yearly", UNSET))

        _features = d.pop("features", UNSET)
        features: list[PlanFeatureResponse] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = PlanFeatureResponse.from_dict(features_item_data)

                features.append(features_item)

        _quotas = d.pop("quotas", UNSET)
        quotas: list[PlanQuotaResponse] | Unset = UNSET
        if _quotas is not UNSET:
            quotas = []
            for quotas_item_data in _quotas:
                quotas_item = PlanQuotaResponse.from_dict(quotas_item_data)

                quotas.append(quotas_item)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        billing_plan_response = cls(
            id=id,
            name=name,
            slug=slug,
            tier=tier,
            price_monthly_cents=price_monthly_cents,
            price_yearly_cents=price_yearly_cents,
            credits_included=credits_included,
            max_members=max_members,
            is_public=is_public,
            is_custom=is_custom,
            sort_order=sort_order,
            description=description,
            stripe_price_id_monthly=stripe_price_id_monthly,
            stripe_price_id_yearly=stripe_price_id_yearly,
            features=features,
            quotas=quotas,
            created_at=created_at,
            updated_at=updated_at,
        )

        billing_plan_response.additional_properties = d
        return billing_plan_response

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
