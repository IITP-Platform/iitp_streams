from typing import TypedDict, List

import faust


class Axis(faust.Record):
    x: int
    y: int
    z: int


# Chest Accelerometer
class ChestACC(faust.Record):
    hz: int
    value: List[Axis]


# Chest Electrocardiogram
class ChestEGC(faust.Record):
    hz: int
    value: List[int]


# Chest Electrodemal
class ChestEDA(faust.Record):
    hz: int
    value: List[int]


# Chest Electromyogram
class ChestEMG(TypedDict):
    hz: int
    value: List[int]


# Chest Temperature
class ChestTemp(faust.Record):
    hz: int
    value: List[int]


# Chest Respiration
class ChestResp(faust.Record):
    hz: int
    value: List[int]


class ChestDeviceSensorValue(faust.Record):
    user_id: str
    connection_id: str
    timestamp: int
    chest_acc: ChestACC
    chest_ecg: ChestEGC
    chest_eda: ChestEDA
    chest_emg: ChestEMG
    chest_temp: ChestTemp
    chest_resp: ChestResp
