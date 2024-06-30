"""
Territory indicators data table is defined here
"""

from sqlalchemy import Column, Date, Enum, Float, ForeignKey, String, Table

from urban_api.db import metadata
from urban_api.db.entities.enums import DateFieldType, IndicatorValueType

DateFieldTypeEnum = Enum(DateFieldType, name="date_field_type")
IndicatorValueTypeEnum = Enum(IndicatorValueType, name="indicator_value_type")

territory_indicators_data = Table(
    "territory_indicators_data",
    metadata,
    Column("indicator_id", ForeignKey("indicators_dict.indicator_id"), primary_key=True, nullable=False),
    Column("territory_id", ForeignKey("territories_data.territory_id"), primary_key=True, nullable=False),
    Column("date_type", DateFieldTypeEnum, primary_key=True, nullable=False),
    Column("date_value", Date, primary_key=True, nullable=False),
    Column("value", Float(53), nullable=False),
    Column("value_type", IndicatorValueTypeEnum, nullable=False),
    Column("information_source", String(300)),
)

"""
Territory indicators:
- indicator_id foreign key int 
- territory_id foreign key int
- date_type enum
- date_value date
- value float(53)
- value_type enum
- information_source string(300)
"""
