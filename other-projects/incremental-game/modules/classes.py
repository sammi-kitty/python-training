#!/usr/bin/python3
from enum import Enum
from dataclasses import dataclass
import datetime as dt

@dataclass
class Machine:
    name: str
    description: str
    production: float
    price: float

class FactorType(Enum):
    ADDITIVE = 1
    MULTIPLICATIVE = 2

@dataclass
class Upgrade:
    name: str
    description: str
    factor: float
    price: float
    factor_type: FactorType

@dataclass
class Statistics:
    money: float
    production: float
    factor: float
    last_check: dt.datetime
    owned_machines: list[Machine]
    owned_upgrades: list[Upgrade]