
"""
sensor.py
"""
from homeassistant.components.sensor import (
    SensorEntity,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, UnitOfPower
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
    """Set up the sensor platform."""
    # In reality, pass the data coordinator here
    entities = [
        EssSocSensor(),
        EssPowerSensor(),
        EssModeSensor(),
    ]
    async_add_entities(entities)

class EssSocSensor(SensorEntity):
    _attr_name = "ESS Battery SoC"
    _attr_unique_id = "ess_battery_soc"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        # Return real value from API/Coordinator
        return 85.5 

class EssPowerSensor(SensorEntity):
    _attr_name = "ESS Current Power"
    _attr_unique_id = "ess_current_power"
    _attr_native_unit_of_measurement = UnitOfPower.KILO_WATT
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT

    @property
    def native_value(self):
        return 2.4

class EssModeSensor(SensorEntity):
    _attr_name = "ESS Operation Mode"
    _attr_unique_id = "ess_operation_mode"
    _attr_icon = "mdi:state-machine"

    @property
    def native_value(self):
        return "Charge"
