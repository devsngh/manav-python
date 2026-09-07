from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_status import SubscriptionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billing_plan_response import BillingPlanResponse


T = TypeVar("T", bound="SubscriptionResponse")


@_attrs_define
class SubscriptionResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        plan_id (UUID):
        status (SubscriptionStatus):
        cancel_at_period_end (bool):
        plan (BillingPlanResponse | None | Unset):
        stripe_subscription_id (None | str | Unset):
        stripe_customer_id (None | str | Unset):
        current_period_start (datetime.datetime | None | Unset):
        current_period_end (datetime.datetime | None | Unset):
        canceled_at (datetime.datetime | None | Unset):
        trial_end (datetime.datetime | None | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: UUID
    org_id: UUID
    plan_id: UUID
    status: SubscriptionStatus
    cancel_at_period_end: bool
    plan: BillingPlanResponse | None | Unset = UNSET
    stripe_subscription_id: None | str | Unset = UNSET
    stripe_customer_id: None | str | Unset = UNSET
    current_period_start: datetime.datetime | None | Unset = UNSET
    current_period_end: datetime.datetime | None | Unset = UNSET
    canceled_at: datetime.datetime | None | Unset = UNSET
    trial_end: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_plan_response import BillingPlanResponse  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        plan_id = str(self.plan_id)

        status = self.status.value

        cancel_at_period_end = self.cancel_at_period_end

        plan: dict[str, Any] | None | Unset
        if isinstance(self.plan, Unset):
            plan = UNSET
        elif isinstance(self.plan, BillingPlanResponse):
            plan = self.plan.to_dict()
        else:
            plan = self.plan

        stripe_subscription_id: None | str | Unset
        if isinstance(self.stripe_subscription_id, Unset):
            stripe_subscription_id = UNSET
        else:
            stripe_subscription_id = self.stripe_subscription_id

        stripe_customer_id: None | str | Unset
        if isinstance(self.stripe_customer_id, Unset):
            stripe_customer_id = UNSET
        else:
            stripe_customer_id = self.stripe_customer_id

        current_period_start: None | str | Unset
        if isinstance(self.current_period_start, Unset):
            current_period_start = UNSET
        elif isinstance(self.current_period_start, datetime.datetime):
            current_period_start = self.current_period_start.isoformat()
        else:
            current_period_start = self.current_period_start

        current_period_end: None | str | Unset
        if isinstance(self.current_period_end, Unset):
            current_period_end = UNSET
        elif isinstance(self.current_period_end, datetime.datetime):
            current_period_end = self.current_period_end.isoformat()
        else:
            current_period_end = self.current_period_end

        canceled_at: None | str | Unset
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        elif isinstance(self.canceled_at, datetime.datetime):
            canceled_at = self.canceled_at.isoformat()
        else:
            canceled_at = self.canceled_at

        trial_end: None | str | Unset
        if isinstance(self.trial_end, Unset):
            trial_end = UNSET
        elif isinstance(self.trial_end, datetime.datetime):
            trial_end = self.trial_end.isoformat()
        else:
            trial_end = self.trial_end

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
                "org_id": org_id,
                "plan_id": plan_id,
                "status": status,
                "cancel_at_period_end": cancel_at_period_end,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan
        if stripe_subscription_id is not UNSET:
            field_dict["stripe_subscription_id"] = stripe_subscription_id
        if stripe_customer_id is not UNSET:
            field_dict["stripe_customer_id"] = stripe_customer_id
        if current_period_start is not UNSET:
            field_dict["current_period_start"] = current_period_start
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at
        if trial_end is not UNSET:
            field_dict["trial_end"] = trial_end
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_plan_response import BillingPlanResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        plan_id = UUID(d.pop("plan_id"))

        status = SubscriptionStatus(d.pop("status"))

        cancel_at_period_end = d.pop("cancel_at_period_end")

        def _parse_plan(data: object) -> BillingPlanResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plan_type_0 = BillingPlanResponse.from_dict(data)

                return plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BillingPlanResponse | None | Unset, data)

        plan = _parse_plan(d.pop("plan", UNSET))

        def _parse_stripe_subscription_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_subscription_id = _parse_stripe_subscription_id(d.pop("stripe_subscription_id", UNSET))

        def _parse_stripe_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stripe_customer_id = _parse_stripe_customer_id(d.pop("stripe_customer_id", UNSET))

        def _parse_current_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_period_start_type_0 = datetime.datetime.fromisoformat(data)

                return current_period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        current_period_start = _parse_current_period_start(d.pop("current_period_start", UNSET))

        def _parse_current_period_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_period_end_type_0 = datetime.datetime.fromisoformat(data)

                return current_period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        current_period_end = _parse_current_period_end(d.pop("current_period_end", UNSET))

        def _parse_canceled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                canceled_at_type_0 = datetime.datetime.fromisoformat(data)

                return canceled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

        def _parse_trial_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trial_end_type_0 = datetime.datetime.fromisoformat(data)

                return trial_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        trial_end = _parse_trial_end(d.pop("trial_end", UNSET))

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

        subscription_response = cls(
            id=id,
            org_id=org_id,
            plan_id=plan_id,
            status=status,
            cancel_at_period_end=cancel_at_period_end,
            plan=plan,
            stripe_subscription_id=stripe_subscription_id,
            stripe_customer_id=stripe_customer_id,
            current_period_start=current_period_start,
            current_period_end=current_period_end,
            canceled_at=canceled_at,
            trial_end=trial_end,
            created_at=created_at,
            updated_at=updated_at,
        )

        subscription_response.additional_properties = d
        return subscription_response

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
