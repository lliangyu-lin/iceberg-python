from pathlib import Path

from pydantic import BaseModel, Field
from typing import List, Literal, Union

from pyiceberg.catalog import load_catalog

class ExecutionContext:
    def __init__(self, warehouse: Path):
        self.warehouse = warehouse
        self.catalog = load_catalog("rest", **{
            "type": "rest",
            "uri": "http://localhost:8181"
        })

class TestSpec(BaseModel):
    testName: str
    actions: List[Union[CreateTableAction, DropTableAction]] = Field(..., discriminator="type")

