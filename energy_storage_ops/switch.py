
"""
switch.py
"""
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    entities = [
        EssAutoStrategySwitch(),
        EssForceChargeSwitch(),
    ]
    async_add_entities(entities)

class EssAutoStrategySwitch(SwitchEntity):
    _attr_name = "ESS Auto Strategy"
    _attr_unique_id = "ess_auto_strategy"
    _attr_icon = "mdi:robot"

    @property
    def is_on(self):
        return True # Replace with real state

    async def async_turn_on(self, **kwargs):
        # Call API to enable
        pass

    async def async_turn_off(self, **kwargs):
        # Call API to disable
        pass

class EssForceChargeSwitch(SwitchEntity):
    _attr_name = "ESS Force Charge"
    _attr_unique_id = "ess_force_charge"
    _attr_icon = "mdi:lightning-bolt"

    @property
    def is_on(self):
        return False

    async def async_turn_on(self, **kwargs):
        pass

    async def async_turn_off(self, **kwargs):
        pass
