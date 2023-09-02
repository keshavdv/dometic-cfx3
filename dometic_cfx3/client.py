import asyncio
import json
import logging
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Any, Optional, List
import socket

from dometic_cfx3.topics import (
    DataAction,
    DataTopic,
    DataType,
    decode,
    encode,
    PowerSourceType, 
    TemperatureUnit,
    get_topic,
    get_topic_definition,
)

logger = logging.getLogger(__name__)


class Client(ABC):
    def __init__(self):
        self.callbacks = defaultdict(list)

    async def get_device_name(self) -> Optional[str]:
        return await self.get(DataTopic.DEVICE_NAME)

    async def get_compartment_count(self) -> Optional[int]:
        return await self.get(DataTopic.COMPARTMENT_COUNT)

    async def get_icemaker_count(self) -> Optional[int]:
        return await self.get(DataTopic.ICEMAKER_COUNT)

    async def get_door_alert(self) -> Optional[bool]:
        return await self.get(DataTopic.DOOR_ALERT)

    async def get_communication_alarm(self) -> Optional[bool]:
        return await self.get(DataTopic.COMMUNICATION_ALARM)

    async def get_temperature_alert_dcm(self) -> Optional[bool]:
        return await self.get(DataTopic.TEMPERATURE_ALERT_DCM)

    async def get_station_ssid_0(self) -> Optional[str]:
        # starlight
        return await self.get(DataTopic.STATION_SSID_0)

    async def get_compartment_0_temperature_history_hour(
        self,
    ) -> Optional[list[int]]:
        # [19.0, 19.0, 19.0, 19.0, 19.4, 20.0, 20.0, 25]
        return await self.get(DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_HOUR)

    async def get_compartment_1_temperature_history_hour(
        self,
    ) -> Optional[list[int]]:
        # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 25]
        return await self.get(DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_HOUR)

    async def get_compartment_0_temperature_history_day(
        self,
    ) -> Optional[list[int]]:
        # [17.9, 16.1, 16.4, 17.9, 20.0, 20.7, 18.7, 203]
        return await self.get(DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_DAY)

    async def get_compartment_1_temperature_history_day(
        self,
    ) -> Optional[list[int]]:
        # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 203]
        return await self.get(DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_DAY)

    async def get_compartment_0_temperature_history_week(
        self,
    ) -> Optional[list[int]]:
        # [17.1, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, 247]
        return await self.get(DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_WEEK)

    async def get_compartment_1_temperature_history_week(
        self,
    ) -> Optional[list[int]]:
        # [0.0, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, 247]
        return await self.get(DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_WEEK)

    async def get_dc_current_history_hour(self) -> Optional[list[int]]:
        # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 25]
        return await self.get(DataTopic.DC_CURRENT_HISTORY_HOUR)

    async def get_dc_current_history_day(self) -> Optional[list[int]]:
        # [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 203]
        return await self.get(DataTopic.DC_CURRENT_HISTORY_DAY)

    async def get_dc_current_history_week(self) -> Optional[list[int]]:
        # [0.0, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, -3276.8, 247]
        return await self.get(DataTopic.DC_CURRENT_HISTORY_WEEK)

    async def get_wifi_ap_connected(self) -> Optional[bool]:
        return await self.get(DataTopic.WIFI_AP_CONNECTED)

    async def get_presented_temperature_unit(self) -> Optional[TemperatureUnit]:
        # 1
        data = await self.get(DataTopic.PRESENTED_TEMPERATURE_UNIT)
        if data:
            return TemperatureUnit(data)

    async def get_compartment_0_measured_temperature(self) -> Optional[int]:
        # 19.0
        return await self.get(DataTopic.COMPARTMENT_0_MEASURED_TEMPERATURE)

    async def get_compartment_1_measured_temperature(self) -> Optional[int]:
        # 0.0
        return await self.get(DataTopic.COMPARTMENT_1_MEASURED_TEMPERATURE)

    async def get_compartment_0_door_open(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPARTMENT_0_DOOR_OPEN)

    async def get_compartment_1_door_open(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPARTMENT_1_DOOR_OPEN)

    async def get_power_source(self) -> Optional[PowerSourceType]:
        # 1
        data = await self.get(DataTopic.POWER_SOURCE)
        if data:
            return PowerSourceType(data)

    async def get_battery_voltage_level(self) -> Optional[int]:
        # 13.1
        return await self.get(DataTopic.BATTERY_VOLTAGE_LEVEL)

    async def get_cooler_power(self) -> Optional[bool]:
        return await self.get(DataTopic.COOLER_POWER)

    async def get_compartment_0_power(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPARTMENT_0_POWER)

    async def get_compartment_1_power(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPARTMENT_1_POWER)

    async def get_compartment_0_temperature_range(self) -> Optional[list[int]]:
        # [-22.0, 10.0]
        return await self.get(DataTopic.COMPARTMENT_0_TEMPERATURE_RANGE)

    async def get_compartment_1_temperature_range(self) -> Optional[list[int]]:
        # [-22.0, 10.0]
        return await self.get(DataTopic.COMPARTMENT_1_TEMPERATURE_RANGE)

    async def get_compartment_0_set_temperature(self) -> Optional[int]:
        # 0.0
        return await self.get(DataTopic.COMPARTMENT_0_SET_TEMPERATURE)

    async def get_compartment_1_set_temperature(self) -> Optional[int]:
        # -15.0
        return await self.get(DataTopic.COMPARTMENT_1_SET_TEMPERATURE)

    async def get_compartment_0_recommended_range(self) -> Optional[list[int]]:
        # [-15.0, 4.0]
        return await self.get(DataTopic.COMPARTMENT_0_RECOMMENDED_RANGE)

    async def get_compartment_1_recommended_range(self) -> Optional[list[int]]:
        # [-15.0, 4.0]
        return await self.get(DataTopic.COMPARTMENT_1_RECOMMENDED_RANGE)

    async def get_ntc_open_large_error(self) -> Optional[bool]:
        return await self.get(DataTopic.NTC_OPEN_LARGE_ERROR)

    async def get_ntc_short_large_error(self) -> Optional[bool]:
        return await self.get(DataTopic.NTC_SHORT_LARGE_ERROR)

    async def get_solenoid_valve_error(self) -> Optional[bool]:
        return await self.get(DataTopic.SOLENOID_VALVE_ERROR)

    async def get_ntc_open_small_error(self) -> Optional[bool]:
        return await self.get(DataTopic.NTC_OPEN_SMALL_ERROR)

    async def get_ntc_short_small_error(self) -> Optional[bool]:
        return await self.get(DataTopic.NTC_SHORT_SMALL_ERROR)

    async def get_fan_overvoltage_error(self) -> Optional[bool]:
        return await self.get(DataTopic.FAN_OVERVOLTAGE_ERROR)

    async def get_compressor_start_fail_error(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPRESSOR_START_FAIL_ERROR)

    async def get_compressor_speed_error(self) -> Optional[bool]:
        return await self.get(DataTopic.COMPRESSOR_SPEED_ERROR)

    async def get_controller_over_temperature(self) -> Optional[bool]:
        return await self.get(DataTopic.CONTROLLER_OVER_TEMPERATURE)

    async def get_voltage_alert(self) -> Optional[bool]:
        return await self.get(DataTopic.VOLTAGE_ALERT)

    async def get_battery_protection_level(self) -> Optional[int]:
        return await self.get(DataTopic.BATTERY_PROTECTION_LEVEL)

    async def get_product_serial_number(self) -> Optional[int]:
        return await self.get(DataTopic.PRODUCT_SERIAL_NUMBER)

    @abstractmethod
    async def get(self, topic: DataTopic):
        pass


class WifiClient(Client):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.running = True
        self.events = defaultdict(asyncio.Event)
        self.device_data = {}
        self.send_ack = asyncio.Event()
        super().__init__()

    async def __aenter__(self):

        # client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # client.sendto("DDMD".encode(), (self.host, self.port))
        # data = json.loads(client.recv(1024))
        # self.product_type = data["pid"]
        # print(data)
        self.product_type = 1

        self.reader, self.writer = await asyncio.open_connection(
            self.host, self.port
        )
        asyncio.ensure_future(self.run())
        await self.send(DataAction.PING.value)
        return self
        
    async def subscribe(self, callback, topic: Optional[DataTopic] = None):
        if not topic:
            self.callbacks[DataTopic.ALL].append(callback)
            if self.product_type == 1:
                topic = DataTopic.SUBSCRIBE_APP_SZ
            elif self.product_type == 2:
                topic = DataTopic.SUBSCRIBE_APP_SZI
            elif self.product_type == 3:
                topic = DataTopic.SUBSCRIBE_APP_DZ
        else:
            self.callbacks[topic].append(callback)
            
        logger.debug(f"Subscribe to {topic}")
        await self._subscribe(topic)

    async def run(self):
        while self.running:
            try:
                data = await self.reader.readuntil("\r".encode())
                if not data:
                    break
            except asyncio.exceptions.IncompleteReadError:
                break
            await self.process(data)

    async def publish(self, topic: DataTopic, value):
        print("IN HEREEEEEE")
        dfn = get_topic_definition(topic)
        data = [DataAction.PUBLISH.value] + dfn.param + encode(dfn, value)
        await self.send_with_ack(data)

    async def _subscribe(self, topic: DataTopic):
        data = [DataAction.SUBSCRIBE.value] + get_topic_definition(topic).param
        await self.send_with_ack(data)

    async def send(self, data):
        x = json.dumps({"ddmp": data})
        logger.debug(f"Writing {x}")
        self.writer.write(f"{x}\r".encode())
        await self.writer.drain()

    async def send_with_ack(self, data):
        await self.send(data)
        self.send_ack.clear()
        await self.send_ack.wait()

    async def get(
        self, topic: DataTopic
    ): 
        self.events[topic].clear()
        await self._subscribe(topic)
        try:
            await asyncio.wait_for(self.events[topic].wait(), 1)
        except asyncio.TimeoutError:
            return
        return self.device_data.get(topic)

    async def process(self, data):
        msg = json.loads(data)["ddmp"]
        logger.debug(f"Received: {msg}")
        action = DataAction(msg[0])
        if action == DataAction.PING:
            logger.debug("Received PING")
            await self.send([DataAction.ACK.value])
        elif action == DataAction.ACK:
            logger.debug("Received ACK")
            self.send_ack.set()
        elif action == DataAction.NAK:
            logger.debug("Received NAK")
        elif action == DataAction.PUBLISH:
            dfn = get_topic(msg[1:5])
            await self.send([DataAction.ACK.value])
            logger.debug(f"Received PUBLISH")
            if dfn:
                value = None
                if len(msg) > 5:
                    value = msg[5:]
                if value:
                    pdata = decode(dfn, value)
                    logger.debug(f"Received PUBLISH: {dfn.topic} {pdata}")
                    self.device_data[dfn.topic] = pdata
                    self.events[dfn.topic].set()

                    await asyncio.gather(*[fn(dfn.topic, pdata) for fn in (self.callbacks[DataTopic.ALL] + self.callbacks[dfn.topic])])

        elif action == DataAction.SUBSCRIBE:
            logger.debug("Received SUBSCRIBE")
            await self.send([DataAction.ACK.value])

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.writer.close()
        await self.writer.wait_closed()
