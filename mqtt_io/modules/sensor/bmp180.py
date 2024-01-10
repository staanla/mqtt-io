"""
BMP180 temperature and pressure sensor
"""
# This script implements the sensorclass for a BMP180 sensor.
# The BMP180 is a predecessor of the BME280 and has no humidity sensor.
# The code uses the Adafruit-BMP library


from typing import cast

from ...types import CerberusSchemaType, ConfigType, SensorValueType
from . import GenericSensor

REQUIREMENTS = ("smbus2", "Adafruit-BMP")
CONFIG_SCHEMA: CerberusSchemaType = {
    "i2c_bus_num": dict(type="integer", required=True, empty=False),
    "chip_addr": dict(type="integer", required=True, empty=False),
}


class Sensor(GenericSensor):
    """
    Implementation of Sensor class for the BMP180 sensor.
    """

    SENSOR_SCHEMA: CerberusSchemaType = {
        "type": dict(
            type="string",
            required=False,
            empty=False,
            default="temperature",
            allowed=["temperature", "pressure"],
        )
    }

    def setup_module(self) -> None:
        # pylint: disable=import-outside-toplevel,attribute-defined-outside-init
        # pylint: disable=import-error,no-member
        from smbus2 import SMBus  # type: ignore
        import Adafruit-BMP.BMP085 as BMP085  # type: ignore

        self.bus = SMBus(self.config["i2c_bus_num"])
        self.address: int = self.config["chip_addr"]
        self.sensor = BMP085.BMP085(busnum=self.bus, address=self.address)

    def get_value(self, sens_conf: ConfigType) -> SensorValueType:
        """
        Get the temperature, humidity or pressure value from the sensor
        """
        sens_type = sens_conf["type"]



        # this is the original code from the BME280 sensor
        # data = self.bme.sample(self.bus, self.address, self.calib)
        # return cast(
        #     float,
        #     dict(
        #         temperature=data.temperature,
        #         humidity=data.humidity,
        #         pressure=data.pressure,
        #     )[sens_type],
        # )
        # adapt this to use the BMP180 sensor
        data.temperature = self.sensor.read_temperature()
        data.pressure = self.sensor.read_pressure()
        return cast(
            float,
            dict(
                temperature=data.temperature,
                pressure=data.pressure,
            )[sens_type],
        )