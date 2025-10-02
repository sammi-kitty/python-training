#!/usr/bin/python3
from dataclasses import dataclass

@dataclass
class Machine:
    name: str
    description: str
    production: float
    price: float

@dataclass
class Upgrade:
    name: str
    description: str
    factor: float
    price: float

@dataclass
class Statistics:
    money: float
    production: float
    factor: float
    owned_machines: list[Machine]
    owned_upgrades: list[Upgrade]