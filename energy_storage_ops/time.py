
"""
time.py
"""
from datetime import time
from homeassistant.components.time import TimeEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    async_add_entities([
        EssChargeStartTime(),
        EssDischargeStartTime(),
    ])

class EssChargeStartTime(TimeEntity):
    _attr_name = "ESS Charge Start Time"
    _attr_unique_id = "ess_charge_start_time"
    _attr_icon = "mdi:clock-start"

    @property
    def native_value(self) -> time | None:
        return time(22, 0)

    async def async_set_value(self, value: time) -> None:
        pass

class EssDischargeStartTime(TimeEntity):
    _attr_name = "ESS Discharge Start Time"
    _attr_unique_id = "ess_discharge_start_time"
    _attr_icon = "mdi:clock-end"

    @property
    def native_value(self) -> time | None:
        return time(8, 0)

    async def async_set_value(self, value: time) -> None:
        pass
