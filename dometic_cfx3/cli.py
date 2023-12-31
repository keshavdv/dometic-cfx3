import asyncio
import logging

from dometic_cfx3.client import WifiClient
from dometic_cfx3.topics import DataAction, DataTopic

logging.basicConfig(level=logging.INFO)


async def test():
    async with WifiClient("localhost", 13142) as client:
        async def callback(topic: DataTopic, value: str):
            print(f"{topic}: {value}")

        await client.subscribe(callback)
        await client.send(DataAction.PING.value)
        # await client.subscribe(DataTopic.SUBSCRIBE_APP_DZ)
        print(f"Name: {await client.get_device_name()}")
        print(f"compartments: {await client.get_compartment_count()}")
        print(f"icemaker: {await client.get_icemaker_count()}")
        print(f"door: {await client.get_door_alert()}")
        print(f"get_device_name: {await client.get_device_name()}")
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
    asyncio.get_event_loop().run_forever()


def main():  # pragma: no cover
    print("This will do something")
    asyncio.run(test())

if __name__ == "__main__":
    main()