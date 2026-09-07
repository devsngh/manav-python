from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plan_tier import PlanTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_plan_update_metadata_type_0 import BillingPlanUpdateMetadataType0


T = TypeVar("T", bound="BillingPlanUpdate")


@_attrs_define
class BillingPlanUpdate:
    """
    Attributes:
        name (None | str | Unset):
        slug (None | str | Unset):
        description (None | str | Unset):
        tier (None | PlanTier | Unset):
        price_monthly_cents (int | None | Unset):
        price_yearly_cents (int | None | Unset):
        credits_included (int | None | Unset):
        max_members (int | None | Unset):
        stripe_price_id_monthly (None | str | Unset):
        stripe_price_id_yearly (None | str | Unset):
        is_public (bool | None | Unset):
        is_custom (bool | None | Unset):
        sort_order (int | None | Unset):
        metadata (BillingPlanUpdateMetadataType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    slug: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tier: None | PlanTier | Unset = UNSET
    price_monthly_cents: int | None | Unset = UNSET
    price_yearly_cents: int | None | Unset = UNSET
    credits_included: int | None | Unset = UNSET
    max_members: int | None | Unset = UNSET
    stripe_price_id_monthly: None | str | Unset = UNSET
    stripe_price_id_yearly: None | str | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    is_custom: bool | None | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    metadata: BillingPlanUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_plan_update_metadata_type_0 import BillingPlanUpdateMetadataType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        elif isinstance(self.tier, PlanTier):
            tier = self.tier.value
        else:
            tier = self.tier

        price_monthly_cents: int | None | Unset
        if isinstance(self.price_monthly_cents, Unset):
            price_monthly_cents = UNSET
        else:
            price_monthly_cents = self.price_monthly_cents

        price_yearly_cents: int | None | Unset
        if isinstance(self.price_yearly_cents, Unset):
            price_yearly_cents = UNSET
        else:
            price_yearly_cents = self.price_yearly_cents

        credits_included: int | None | Unset
        if isinstance(self.credits_included, Unset):
            credits_included = UNSET
        else:
            credits_included = self.credits_included

        max_members: int | None | Unset
        if isinstance(self.max_members, Unset):
            max_members = UNSET
        else:
            max_members = self.max_members

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

        is_public: bool | None | Unset
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        is_custom: bool | None | Unset
        if isinstance(self.is_custom, Unset):
            is_custom = UNSET
        else:
            is_custom = self.is_custom

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BillingPlanUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if tier is not UNSET:
            field_dict["tier"] = tier
        if price_monthly_cents is not UNSET:
            field_dict["price_monthly_cents"] = price_monthly_cents
        if price_yearly_cents is not UNSET:
            field_dict["price_yearly_cents"] = price_yearly_cents
        if credits_included is not UNSET:
            field_dict["credits_included"] = credits_included
        if max_members is not UNSET:
            field_dict["max_members"] = max_members
        if stripe_price_id_monthly is not UNSET:
            field_dict["stripe_price_id_monthly"] = stripe_price_id_monthly
        if stripe_price_id_yearly is not UNSET:
            field_dict["stripe_price_id_yearly"] = stripe_price_id_yearly
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_custom is not UNSET:
            field_dict["is_custom"] = is_custom
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_plan_update_metadata_type_0 import BillingPlanUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tier(data: object) -> None | PlanTier | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tier_type_0 = PlanTier(data)

                return tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlanTier | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_price_monthly_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_monthly_cents = _parse_price_monthly_cents(d.pop("price_monthly_cents", UNSET))

        def _parse_price_yearly_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_yearly_cents = _parse_price_yearly_cents(d.pop("price_yearly_cents", UNSET))

        def _parse_credits_included(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        credits_included = _parse_credits_included(d.pop("credits_included", UNSET))

        def _parse_max_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_members = _parse_max_members(d.pop("max_members", UNSET))

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

        def _parse_is_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public = _parse_is_public(d.pop("is_public", UNSET))

        def _parse_is_custom(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_custom = _parse_is_custom(d.pop("is_custom", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        def _parse_metadata(data: object) -> BillingPlanUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BillingPlanUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingPlanUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        billing_plan_update = cls(
            name=name,
            slug=slug,
            description=description,
            tier=tier,
            price_monthly_cents=price_monthly_cents,
            price_yearly_cents=price_yearly_cents,
            credits_included=credits_included,
            max_members=max_members,
            stripe_price_id_monthly=stripe_price_id_monthly,
            stripe_price_id_yearly=stripe_price_id_yearly,
            is_public=is_public,
            is_custom=is_custom,
            sort_order=sort_order,
            metadata=metadata,
        )

        billing_plan_update.additional_properties = d
        return billing_plan_update

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
