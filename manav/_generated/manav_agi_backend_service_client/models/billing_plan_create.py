from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plan_tier import PlanTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_plan_create_metadata_type_0 import BillingPlanCreateMetadataType0


T = TypeVar("T", bound="BillingPlanCreate")


@_attrs_define
class BillingPlanCreate:
    """
    Attributes:
        name (str):
        slug (str):
        tier (PlanTier):
        description (None | str | Unset):
        price_monthly_cents (int | Unset):  Default: 0.
        price_yearly_cents (int | Unset):  Default: 0.
        credits_included (int | Unset):  Default: 0.
        max_members (int | Unset):  Default: 1.
        stripe_price_id_monthly (None | str | Unset):
        stripe_price_id_yearly (None | str | Unset):
        is_public (bool | Unset):  Default: True.
        is_custom (bool | Unset):  Default: False.
        sort_order (int | Unset):  Default: 0.
        metadata (BillingPlanCreateMetadataType0 | None | Unset):
    """

    name: str
    slug: str
    tier: PlanTier
    description: None | str | Unset = UNSET
    price_monthly_cents: int | Unset = 0
    price_yearly_cents: int | Unset = 0
    credits_included: int | Unset = 0
    max_members: int | Unset = 1
    stripe_price_id_monthly: None | str | Unset = UNSET
    stripe_price_id_yearly: None | str | Unset = UNSET
    is_public: bool | Unset = True
    is_custom: bool | Unset = False
    sort_order: int | Unset = 0
    metadata: BillingPlanCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_plan_create_metadata_type_0 import BillingPlanCreateMetadataType0  # noqa: PLC0415

        name = self.name

        slug = self.slug

        tier = self.tier.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        price_monthly_cents = self.price_monthly_cents

        price_yearly_cents = self.price_yearly_cents

        credits_included = self.credits_included

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

        is_public = self.is_public

        is_custom = self.is_custom

        sort_order = self.sort_order

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BillingPlanCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "tier": tier,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.billing_plan_create_metadata_type_0 import BillingPlanCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        tier = PlanTier(d.pop("tier"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        price_monthly_cents = d.pop("price_monthly_cents", UNSET)

        price_yearly_cents = d.pop("price_yearly_cents", UNSET)

        credits_included = d.pop("credits_included", UNSET)

        max_members = d.pop("max_members", UNSET)

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

        is_public = d.pop("is_public", UNSET)

        is_custom = d.pop("is_custom", UNSET)

        sort_order = d.pop("sort_order", UNSET)

        def _parse_metadata(data: object) -> BillingPlanCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BillingPlanCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingPlanCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        billing_plan_create = cls(
            name=name,
            slug=slug,
            tier=tier,
            description=description,
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

        billing_plan_create.additional_properties = d
        return billing_plan_create

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
