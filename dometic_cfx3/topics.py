from dataclasses import dataclass
from enum import Enum, auto
import math

class PowerSourceType(Enum):
    AC = 0
    DC = 1
    SOLAR = 2

class TemperatureUnit(Enum):
    CELCIUS = 0
    FAHRENHEIT = 1

class DataAction(Enum):
    PUBLISH = 0
    SUBSCRIBE = 1
    PING = 2
    HELLO = 3
    ACK = 4
    NAK = 5
    NOP = 6


class DataType(Enum):
    INT16_DECIDEGREE_CELSIUS = auto()
    INT8_BOOLEAN = auto()
    INT8_NUMBER = auto()
    INT16_DECICURRENT_VOLT = auto()
    UINT8_NUMBER = auto()
    UTF8_STRING = auto()
    HISTORY_DATA_ARRAY = auto()
    INT16_ARRAY = auto()
    EMPTY = auto()


class DataTopic(Enum):
    ALL = auto()
    SUBSCRIBE_APP_SZ = auto()
    SUBSCRIBE_APP_SZI = auto()
    SUBSCRIBE_APP_DZ = auto()
    PRODUCT_SERIAL_NUMBER = auto()
    COMPARTMENT_COUNT = auto()
    ICEMAKER_COUNT = auto()
    COMPARTMENT_0_POWER = auto()
    COMPARTMENT_1_POWER = auto()
    COMPARTMENT_0_MEASURED_TEMPERATURE = auto()
    COMPARTMENT_1_MEASURED_TEMPERATURE = auto()
    COMPARTMENT_0_DOOR_OPEN = auto()
    COMPARTMENT_1_DOOR_OPEN = auto()
    COMPARTMENT_0_SET_TEMPERATURE = auto()
    COMPARTMENT_1_SET_TEMPERATURE = auto()
    COMPARTMENT_0_RECOMMENDED_RANGE = auto()
    COMPARTMENT_1_RECOMMENDED_RANGE = auto()
    PRESENTED_TEMPERATURE_UNIT = auto()
    COMPARTMENT_0_TEMPERATURE_RANGE = auto()
    COMPARTMENT_1_TEMPERATURE_RANGE = auto()
    COOLER_POWER = auto()
    BATTERY_VOLTAGE_LEVEL = auto()
    BATTERY_PROTECTION_LEVEL = auto()
    POWER_SOURCE = auto()
    ICEMAKER_POWER = auto()
    COMMUNICATION_ALARM = auto()
    NTC_OPEN_LARGE_ERROR = auto()
    NTC_SHORT_LARGE_ERROR = auto()
    SOLENOID_VALVE_ERROR = auto()
    NTC_OPEN_SMALL_ERROR = auto()
    NTC_SHORT_SMALL_ERROR = auto()
    FAN_OVERVOLTAGE_ERROR = auto()
    COMPRESSOR_START_FAIL_ERROR = auto()
    COMPRESSOR_SPEED_ERROR = auto()
    CONTROLLER_OVER_TEMPERATURE = auto()
    TEMPERATURE_ALERT_DCM = auto()
    TEMPERATURE_ALERT_CC = auto()
    DOOR_ALERT = auto()
    VOLTAGE_ALERT = auto()
    DEVICE_NAME = auto()
    WIFI_MODE = auto()
    BLUETOOTH_MODE = auto()
    WIFI_AP_CONNECTED = auto()
    STATION_SSID_0 = auto()
    STATION_SSID_1 = auto()
    STATION_SSID_2 = auto()
    STATION_PASSWORD_0 = auto()
    STATION_PASSWORD_1 = auto()
    STATION_PASSWORD_2 = auto()
    STATION_PASSWORD_3 = auto()
    STATION_PASSWORD_4 = auto()
    CFX_DIRECT_PASSWORD_0 = auto()
    CFX_DIRECT_PASSWORD_1 = auto()
    CFX_DIRECT_PASSWORD_2 = auto()
    CFX_DIRECT_PASSWORD_3 = auto()
    CFX_DIRECT_PASSWORD_4 = auto()
    COMPARTMENT_0_TEMPERATURE_HISTORY_HOUR = auto()
    COMPARTMENT_1_TEMPERATURE_HISTORY_HOUR = auto()
    COMPARTMENT_0_TEMPERATURE_HISTORY_DAY = auto()
    COMPARTMENT_1_TEMPERATURE_HISTORY_DAY = auto()
    COMPARTMENT_0_TEMPERATURE_HISTORY_WEEK = auto()
    COMPARTMENT_1_TEMPERATURE_HISTORY_WEEK = auto()
    DC_CURRENT_HISTORY_HOUR = auto()
    DC_CURRENT_HISTORY_DAY = auto()
    DC_CURRENT_HISTORY_WEEK = auto()


@dataclass
class TopicDefinition:
    """Class for keeping track of an item in inventory."""

    topic: DataTopic
    param: list[int]
    data_type: DataType


TOPICS = {
    # Subscribe All SZ topics
    DataTopic.SUBSCRIBE_APP_SZ: TopicDefinition(
        topic=DataTopic.SUBSCRIBE_APP_SZ,
        param=[1, 0, 0, 129],
        data_type=DataType.EMPTY,
    ),
    # Subscribe All SZ with icemaker topics
    DataTopic.SUBSCRIBE_APP_SZI: TopicDefinition(
        topic=DataTopic.SUBSCRIBE_APP_SZI,
        param=[2, 0, 0, 129],
        data_type=DataType.EMPTY,
    ),
    # Subscribe All DZ
    DataTopic.SUBSCRIBE_APP_DZ: TopicDefinition(
        topic=DataTopic.SUBSCRIBE_APP_DZ,
        param=[3, 0, 0, 129],
        data_type=DataType.EMPTY,
    ),
    # Product Information
    DataTopic.PRODUCT_SERIAL_NUMBER: TopicDefinition(
        topic=DataTopic.PRODUCT_SERIAL_NUMBER,
        param=[0, 193, 0, 0],
        data_type=DataType.UTF8_STRING,
    ),
    # # Properties
    DataTopic.COMPARTMENT_COUNT: TopicDefinition(
        topic=DataTopic.COMPARTMENT_COUNT,
        param=[0, 128, 0, 1],
        data_type=DataType.INT8_NUMBER,
    ),
    DataTopic.ICEMAKER_COUNT: TopicDefinition(
        topic=DataTopic.ICEMAKER_COUNT,
        param=[0, 129, 0, 1],
        data_type=DataType.INT8_NUMBER,
    ),
    # # Compartment
    DataTopic.COMPARTMENT_0_POWER: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_POWER,
        param=[0, 0, 1, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPARTMENT_1_POWER: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_POWER,
        param=[16, 0, 1, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPARTMENT_0_MEASURED_TEMPERATURE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_MEASURED_TEMPERATURE,
        param=[0, 1, 1, 1],
        data_type=DataType.INT16_DECIDEGREE_CELSIUS,
    ),
    DataTopic.COMPARTMENT_1_MEASURED_TEMPERATURE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_MEASURED_TEMPERATURE,
        param=[16, 1, 1, 1],
        data_type=DataType.INT16_DECIDEGREE_CELSIUS,
    ),
    DataTopic.COMPARTMENT_0_DOOR_OPEN: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_DOOR_OPEN,
        param=[0, 8, 1, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPARTMENT_1_DOOR_OPEN: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_DOOR_OPEN,
        param=[16, 8, 1, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPARTMENT_0_SET_TEMPERATURE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_SET_TEMPERATURE,
        param=[0, 2, 1, 1],
        data_type=DataType.INT16_DECIDEGREE_CELSIUS,
    ),
    DataTopic.COMPARTMENT_1_SET_TEMPERATURE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_SET_TEMPERATURE,
        param=[16, 2, 1, 1],
        data_type=DataType.INT16_DECIDEGREE_CELSIUS,
    ),
    DataTopic.COMPARTMENT_0_RECOMMENDED_RANGE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_RECOMMENDED_RANGE,
        param=[0, 129, 1, 1],
        data_type=DataType.INT16_ARRAY,
    ),
    DataTopic.COMPARTMENT_1_RECOMMENDED_RANGE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_RECOMMENDED_RANGE,
        param=[16, 129, 1, 1],
        data_type=DataType.INT16_ARRAY,
    ),
    # Presented Temperature Unit
    DataTopic.PRESENTED_TEMPERATURE_UNIT: TopicDefinition(
        topic=DataTopic.PRESENTED_TEMPERATURE_UNIT,
        param=[0, 0, 2, 1],
        data_type=DataType.INT8_NUMBER,
    ),
    DataTopic.COMPARTMENT_0_TEMPERATURE_RANGE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_TEMPERATURE_RANGE,
        param=[0, 128, 1, 1],
        data_type=DataType.INT16_ARRAY,
    ),
    DataTopic.COMPARTMENT_1_TEMPERATURE_RANGE: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_TEMPERATURE_RANGE,
        param=[16, 128, 1, 1],
        data_type=DataType.INT16_ARRAY,
    ),
    # Power
    DataTopic.COOLER_POWER: TopicDefinition(
        topic=DataTopic.COOLER_POWER,
        param=[0, 0, 3, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.BATTERY_VOLTAGE_LEVEL: TopicDefinition(
        topic=DataTopic.BATTERY_VOLTAGE_LEVEL,
        param=[0, 1, 3, 1],
        data_type=DataType.INT16_DECICURRENT_VOLT,
    ),
    DataTopic.BATTERY_PROTECTION_LEVEL: TopicDefinition(
        topic=DataTopic.BATTERY_PROTECTION_LEVEL,
        param=[0, 2, 3, 1],
        data_type=DataType.UINT8_NUMBER,
    ),
    DataTopic.POWER_SOURCE: TopicDefinition(
        topic=DataTopic.POWER_SOURCE,
        param=[0, 5, 3, 1],
        data_type=DataType.INT8_NUMBER,
    ),
    DataTopic.ICEMAKER_POWER: TopicDefinition(
        topic=DataTopic.ICEMAKER_POWER,
        param=[0, 6, 3, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    # Errors
    DataTopic.COMMUNICATION_ALARM: TopicDefinition(
        topic=DataTopic.COMMUNICATION_ALARM,
        param=[0, 3, 4, 1],
        # data_type=not specified in documentation. Using INT8_BOOLEAN for now
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.NTC_OPEN_LARGE_ERROR: TopicDefinition(
        topic=DataTopic.NTC_OPEN_LARGE_ERROR,
        param=[0, 1, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.NTC_SHORT_LARGE_ERROR: TopicDefinition(
        topic=DataTopic.NTC_SHORT_LARGE_ERROR,
        param=[0, 2, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.SOLENOID_VALVE_ERROR: TopicDefinition(
        topic=DataTopic.SOLENOID_VALVE_ERROR,
        param=[0, 9, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.NTC_OPEN_SMALL_ERROR: TopicDefinition(
        topic=DataTopic.NTC_OPEN_SMALL_ERROR,
        #  Temporary params for mocked broker. Params should be 'param': [0, 11, 4, 1],
        param=[0, 17, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.NTC_SHORT_SMALL_ERROR: TopicDefinition(
        topic=DataTopic.NTC_SHORT_SMALL_ERROR,
        #  Temporary params for mocked broker. Params should be 'param': [0, 12, 4, 1],
        param=[0, 18, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.FAN_OVERVOLTAGE_ERROR: TopicDefinition(
        topic=DataTopic.FAN_OVERVOLTAGE_ERROR,
        #  Temporary params for mocked broker, Params should be 'param': [0, 32, 4, 1]
        param=[0, 50, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPRESSOR_START_FAIL_ERROR: TopicDefinition(
        topic=DataTopic.COMPRESSOR_START_FAIL_ERROR,
        #  Temporary params for mocked broker. Params should be 'param': [0, 33, 4, 1],
        param=[0, 51, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.COMPRESSOR_SPEED_ERROR: TopicDefinition(
        topic=DataTopic.COMPRESSOR_SPEED_ERROR,
        #  Temporary params for mocked broker. Params should be 'param': [0, 34, 4, 1],
        param=[0, 52, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.CONTROLLER_OVER_TEMPERATURE: TopicDefinition(
        topic=DataTopic.CONTROLLER_OVER_TEMPERATURE,
        #  Temporary params for mocked broker. Params should be 'param': [0, 35, 4, 1],
        param=[0, 53, 4, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    # Alerts
    DataTopic.TEMPERATURE_ALERT_DCM: TopicDefinition(
        topic=DataTopic.TEMPERATURE_ALERT_DCM,
        param=[0, 3, 5, 1],  # used for DCM as source
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.TEMPERATURE_ALERT_CC: TopicDefinition(
        topic=DataTopic.TEMPERATURE_ALERT_CC,
        param=[0, 0, 5, 1],  # used for CC as source
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.DOOR_ALERT: TopicDefinition(
        topic=DataTopic.DOOR_ALERT,
        param=[0, 1, 5, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.VOLTAGE_ALERT: TopicDefinition(
        topic=DataTopic.VOLTAGE_ALERT,
        param=[0, 2, 5, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    # Communication
    DataTopic.DEVICE_NAME: TopicDefinition(
        topic=DataTopic.DEVICE_NAME,
        param=[0, 0, 6, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.WIFI_MODE: TopicDefinition(
        topic=DataTopic.WIFI_MODE,
        param=[0, 1, 6, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.BLUETOOTH_MODE: TopicDefinition(
        topic=DataTopic.BLUETOOTH_MODE,
        param=[0, 3, 6, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    DataTopic.WIFI_AP_CONNECTED: TopicDefinition(
        topic=DataTopic.WIFI_AP_CONNECTED,
        param=[0, 8, 6, 1],
        data_type=DataType.INT8_BOOLEAN,
    ),
    # WiFi Settings
    DataTopic.STATION_SSID_0: TopicDefinition(
        topic=DataTopic.STATION_SSID_0,
        param=[0, 0, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_SSID_1: TopicDefinition(
        topic=DataTopic.STATION_SSID_1,
        param=[1, 0, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_SSID_2: TopicDefinition(
        topic=DataTopic.STATION_SSID_2,
        param=[2, 0, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_PASSWORD_0: TopicDefinition(
        topic=DataTopic.STATION_PASSWORD_0,
        param=[0, 1, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_PASSWORD_1: TopicDefinition(
        topic=DataTopic.STATION_PASSWORD_1,
        param=[1, 1, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_PASSWORD_2: TopicDefinition(
        topic=DataTopic.STATION_PASSWORD_2,
        param=[2, 1, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_PASSWORD_3: TopicDefinition(
        topic=DataTopic.STATION_PASSWORD_3,
        param=[3, 1, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.STATION_PASSWORD_4: TopicDefinition(
        topic=DataTopic.STATION_PASSWORD_4,
        param=[4, 1, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.CFX_DIRECT_PASSWORD_0: TopicDefinition(
        topic=DataTopic.CFX_DIRECT_PASSWORD_0,
        param=[0, 2, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.CFX_DIRECT_PASSWORD_1: TopicDefinition(
        topic=DataTopic.CFX_DIRECT_PASSWORD_1,
        param=[1, 2, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.CFX_DIRECT_PASSWORD_2: TopicDefinition(
        topic=DataTopic.CFX_DIRECT_PASSWORD_2,
        param=[2, 2, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.CFX_DIRECT_PASSWORD_3: TopicDefinition(
        topic=DataTopic.CFX_DIRECT_PASSWORD_3,
        param=[3, 2, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.CFX_DIRECT_PASSWORD_4: TopicDefinition(
        topic=DataTopic.CFX_DIRECT_PASSWORD_4,
        param=[4, 2, 7, 1],
        data_type=DataType.UTF8_STRING,
    ),
    DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_HOUR: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_HOUR,
        param=[0, 64, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_HOUR: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_HOUR,
        param=[16, 64, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_DAY: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_DAY,
        param=[0, 65, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_DAY: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_DAY,
        param=[16, 65, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_WEEK: TopicDefinition(
        topic=DataTopic.COMPARTMENT_0_TEMPERATURE_HISTORY_WEEK,
        param=[0, 66, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_WEEK: TopicDefinition(
        topic=DataTopic.COMPARTMENT_1_TEMPERATURE_HISTORY_WEEK,
        param=[16, 66, 1, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.DC_CURRENT_HISTORY_HOUR: TopicDefinition(
        topic=DataTopic.DC_CURRENT_HISTORY_HOUR,
        param=[0, 64, 3, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.DC_CURRENT_HISTORY_DAY: TopicDefinition(
        topic=DataTopic.DC_CURRENT_HISTORY_DAY,
        param=[0, 65, 3, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
    DataTopic.DC_CURRENT_HISTORY_WEEK: TopicDefinition(
        topic=DataTopic.DC_CURRENT_HISTORY_WEEK,
        param=[0, 66, 3, 1],
        data_type=DataType.HISTORY_DATA_ARRAY,
    ),
}


def get_topic_definition(topic: DataTopic):
    return TOPICS.get(topic)


def get_topic(param):
    for k, v in TOPICS.items():
        if param == v.param:
            return v


# export const fetchTopicType = (param) => {
#   let ddmDataType;
#   Object.keys(ddmTopics).forEach((key) => {
#     if (JSON.stringify(ddmTopics[key].PARAM) === JSON.stringify(param)) {
#       ddmDataType = ddmTopics[key].TYPE;
#     }
#   });
#   return ddmDataType;
# };


def bytes_to_celcius(data):
    deciDegree = 0
    if data[1] >= 128:
        # negative number
        deciDegree = ((data[1] * 256) + data[0]) - 65536
    else:
        # zero or positive number
        deciDegree = (data[1] << 8) | data[0]
    return deciDegree / 10


def decode(dfn, data):
    if dfn.data_type == DataType.INT16_DECIDEGREE_CELSIUS:
        return bytes_to_celcius(data)
    elif dfn.data_type == DataType.INT8_BOOLEAN:
        return bool(data[0])
    elif dfn.data_type in {DataType.INT8_NUMBER, DataType.UINT8_NUMBER}:
        return data[0]
    elif dfn.data_type == DataType.INT16_DECICURRENT_VOLT:
        current = (data[1] << 8) | data[0]
        current = round(current) / 10
        return current
    elif dfn.data_type == DataType.UTF8_STRING:
        if data:
            return bytearray(data).decode()
        return ""
    elif dfn.data_type == DataType.HISTORY_DATA_ARRAY:
        return [
            bytes_to_celcius(data[0:2]),
            bytes_to_celcius(data[2:4]),
            bytes_to_celcius(data[4:6]),
            bytes_to_celcius(data[6:8]),
            bytes_to_celcius(data[8:10]),
            bytes_to_celcius(data[10:12]),
            bytes_to_celcius(data[12:14]),
            data[14],
        ]
    elif dfn.data_type == DataType.INT16_ARRAY:
        return [bytes_to_celcius(data[0:2]), bytes_to_celcius(data[2:4])]
    elif dfn.data_type == DataType.EMPTY:
        return data
    return data


def encode(dfn, value):
    if dfn.data_type == DataType.INT16_DECIDEGREE_CELSIUS:
        deciDegree = math.ceil(value * 10)
        c1 = deciDegree & 0xff
        c2 = (deciDegree >> 8) & 0xff
        return [c1, c2]
    elif dfn.data_type == DataType.INT8_BOOLEAN:
        return [1] if value else [0]
    elif dfn.data_type in {DataType.INT8_NUMBER, DataType.UINT8_NUMBER}:
        return [value]
    elif dfn.data_type == DataType.UTF8_STRING:
        raise NotImplemented()
    raise NotImplemented()