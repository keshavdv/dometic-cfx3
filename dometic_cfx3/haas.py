import asyncio
import logging

from dometic_cfx3.client import WifiClient
from dometic_cfx3.topics import DataAction, DataTopic
from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo, BinarySensor, BinarySensorInfo, Switch, SwitchInfo
from paho.mqtt.client import Client, MQTTMessage

logging.basicConfig(level=logging.DEBUG)

from queue import Queue
 


async def test():
    async with WifiClient("localhost", 13142) as client:
        # Configure the required parameters for the MQTT broker
        mqtt_settings = Settings.MQTT(host="192.168.103.138")
        sn = await client.get_product_serial_number()
        device_info = DeviceInfo(name=await client.get_device_name(), manufacturer="Dometic", hw_version=sn, identifiers=sn)

      
        dt = {}
        loop = asyncio.get_event_loop()
        command_queue = Queue()
        def toggle(_: Client, topic, message: MQTTMessage):
            payload = message.payload.decode()
            logging.info(f"Received {payload} from HA")
            asyncio.run_coroutine_threadsafe(client.publish(topic, True if payload == "ON" else False), loop)
            if payload == "ON":
                dt.get(topic).on()
            else:
                dt.get(topic).off()


        dt[DataTopic.DOOR_ALERT] = BinarySensor(Settings(mqtt=mqtt_settings, entity=BinarySensorInfo(name="door_alert", unique_id="door_alert", device=device_info)))
        dt[DataTopic.PRODUCT_SERIAL_NUMBER] = Sensor(Settings(mqtt=mqtt_settings, entity=SensorInfo(name="serial_number", unique_id="serial_number", device=device_info)))
        dt[DataTopic.COOLER_POWER] = Switch(Settings(mqtt=mqtt_settings, entity=SwitchInfo(name="cooler_power", unique_id="cooler_power", device=device_info)), toggle, DataTopic.COOLER_POWER)
        dt[DataTopic.COMPARTMENT_0_MEASURED_TEMPERATURE] = Sensor(Settings(mqtt=mqtt_settings, entity=SensorInfo(name="compartment_temperature", unique_id="compartment_temperature", unit_of_measurement="°C", device=device_info)))
        dt[DataTopic.COMPARTMENT_0_SET_TEMPERATURE] = Sensor(Settings(mqtt=mqtt_settings, entity=SensorInfo(name="compartment_setpoint", unique_id="compartment_setpoint", unit_of_measurement="°C", device=device_info)))
        dt[DataTopic.BATTERY_VOLTAGE_LEVEL] = Sensor(Settings(mqtt=mqtt_settings, entity=SensorInfo(name="battery_voltage", unique_id="battery_voltage", unit_of_measurement="V", device=device_info)))
        dt[DataTopic.POWER_SOURCE] = Sensor(Settings(mqtt=mqtt_settings, entity=SensorInfo(name="power_source", unique_id="power_source", device=device_info)))



        async def callback(topic: DataTopic, value):
            if topic in dt:
                sensor = dt.get(topic)
                print(sensor)
                if isinstance(sensor, BinarySensor):
                    if value:
                        sensor.on()
                    else:
                        sensor.off()
                elif isinstance(sensor, Sensor):
                    if topic == DataTopic.POWER_SOURCE:
                        value = "dc" if value == 1 else "ac"
                    sensor.set_state(value)
            print(f"{topic}: {value}")

        await client.subscribe(callback)
        # for topic, _ in dt.items():
        #     await client.subscribe(callback, topic=topic)

        # await client.send(DataAction.PING.value)
        # await client.publish(DataTopic.COOLER_POWER, True)
        # print(f"Name: {await client.get_device_name()}")
        print(f"compartments: {await client.get_compartment_count()}")
        # print(f"icemaker: {await client.get_icemaker_count()}")
        print(f"door: {await client.get_door_alert()}")
        # print(f"get_device_name: {await client.get_device_name()}")
        # print(
        #     f"get_communication_alarm: {await client.get_communication_alarm()}"
        # )
        # print(
        #     f"get_temperature_alert_dcm: {await client.get_temperature_alert_dcm()}"
        # )
        # print(f"get_station_ssid_0: {await client.get_station_ssid_0()}")
        # print(
        #     f"get_compartment_0_temperature_history_hour: {await client.get_compartment_0_temperature_history_hour()}"
        # )
        # print(
        #     f"get_compartment_1_temperature_history_hour: {await client.get_compartment_1_temperature_history_hour()}"
        # )
        # print(
        #     f"get_compartment_0_temperature_history_day: {await client.get_compartment_0_temperature_history_day()}"
        # )
        # print(
        #     f"get_compartment_1_temperature_history_day: {await client.get_compartment_1_temperature_history_day()}"
        # )
        # print(
        #     f"get_compartment_0_temperature_history_week: {await client.get_compartment_0_temperature_history_week()}"
        # )
        # print(
        #     f"get_compartment_1_temperature_history_week: {await client.get_compartment_1_temperature_history_week()}"
        # )
        # print(
        #     f"get_dc_current_history_hour: {await client.get_dc_current_history_hour()}"
        # )
        # print(
        #     f"get_dc_current_history_day: {await client.get_dc_current_history_day()}"
        # )
        # print(
        #     f"get_dc_current_history_week: {await client.get_dc_current_history_week()}"
        # )
        # print(f"get_wifi_ap_connected: {await client.get_wifi_ap_connected()}")
        # print(
        #     f"get_presented_temperature_unit: {await client.get_presented_temperature_unit()}"
        # )
        # print(
        #     f"get_compartment_0_measured_temperature: {await client.get_compartment_0_measured_temperature()}"
        # )
        # print(
        #     f"get_compartment_1_measured_temperature: {await client.get_compartment_1_measured_temperature()}"
        # )
        # print(
        #     f"get_compartment_0_door_open: {await client.get_compartment_0_door_open()}"
        # )
        # print(
        #     f"get_compartment_1_door_open: {await client.get_compartment_1_door_open()}"
        # )
        # print(f"get_power_source: {await client.get_power_source()}")
        # print(
        #     f"get_battery_voltage_level: {await client.get_battery_voltage_level()}"
        # )
        # print(f"get_cooler_power: {await client.get_cooler_power()}")
        # print(
        #     f"get_compartment_0_power: {await client.get_compartment_0_power()}"
        # )
        # print(
        #     f"get_compartment_1_power: {await client.get_compartment_1_power()}"
        # )
        # print(
        #     f"get_compartment_0_temperature_range: {await client.get_compartment_0_temperature_range()}"
        # )
        # print(
        #     f"get_compartment_1_temperature_range: {await client.get_compartment_1_temperature_range()}"
        # )
        # print(
        #     f"get_compartment_0_set_temperature: {await client.get_compartment_0_set_temperature()}"
        # )
        # print(
        #     f"get_compartment_1_set_temperature: {await client.get_compartment_1_set_temperature()}"
        # )
        # print(
        #     f"get_compartment_0_recommended_range: {await client.get_compartment_0_recommended_range()}"
        # )
        # print(
        #     f"get_compartment_1_recommended_range: {await client.get_compartment_1_recommended_range()}"
        # )
        # print(
        #     f"get_ntc_open_large_error: {await client.get_ntc_open_large_error()}"
        # )
        # print(
        #     f"get_ntc_short_large_error: {await client.get_ntc_short_large_error()}"
        # )
        # print(
        #     f"get_solenoid_valve_error: {await client.get_solenoid_valve_error()}"
        # )
        # print(
        #     f"get_ntc_open_small_error: {await client.get_ntc_open_small_error()}"
        # )
        # print(
        #     f"get_ntc_short_small_error: {await client.get_ntc_short_small_error()}"
        # )
        # print(
        #     f"get_fan_overvoltage_error: {await client.get_fan_overvoltage_error()}"
        # )
        # print(
        #     f"get_compressor_start_fail_error: {await client.get_compressor_start_fail_error()}"
        # )
        # print(
        #     f"get_compressor_speed_error: {await client.get_compressor_speed_error()}"
        # )
        # print(
        #     f"get_controller_over_temperature: {await client.get_controller_over_temperature()}"
        # )
        # print(f"get_door_alert: {await client.get_door_alert()}")
        # print(f"get_voltage_alert: {await client.get_voltage_alert()}")
        # print(
        #     f"get_battery_protection_level: {await client.get_battery_protection_level()}"
        # )
        # print(
        #     f"get_product_serial_number: {await client.get_product_serial_number()}"
        # )
        while True:
            await asyncio.sleep(1)
        #     topic, value = command_queue.get()
        #     await client.publish(topic, value)


def main():  # pragma: no cover
    print("This will do something")
    asyncio.run(test())

if __name__ == "__main__":
    main()