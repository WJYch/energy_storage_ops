
"""
number.py
"""
from homeassistant.components.number import NumberEntity
from homeassistant.const import UnitOfPower
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
        EssMaxChargePowerNumber(),
        EssDischargeCutoffNumber(),
    ])

class EssMaxChargePowerNumber(NumberEntity):
    _attr_name = "ESS Max Charge Power"
    _attr_unique_id = "ess_max_charge_power"
    _attr_native_unit_of_measurement = UnitOfPower.WATT
    _attr_native_min_value = 0
    _attr_native_max_value = 5000
    _attr_native_step = 100
    _attr_icon = "mdi:flash"

    @property
    def native_value(self):
        return 3000

    async def async_set_native_value(self, value: float) -> None:
        # Update config
        pass

class EssDischargeCutoffNumber(NumberEntity):
    _attr_name = "ESS Discharge Cutoff SoC"
    _attr_unique_id = "ess_discharge_cutoff_soc"
    _attr_native_unit_of_measurement = "%"
    _attr_native_min_value = 10
    _attr_native_max_value = 100
    _attr_native_step = 5
    _attr_icon = "mdi:battery-alert"

    @property
    def native_value(self):
        return 20

    async def async_set_native_value(self, value: float) -> None:
        pass
