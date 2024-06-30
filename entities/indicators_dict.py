"""
Table which represent indicators dict is defined here.

Current list is:
- measurement_units_dict
- indicators_dict
"""

from sqlalchemy import Column, ForeignKey, Integer, Sequence, String, Table

from urban_api.db import metadata

measurement_units_dict_id_seq = Sequence("measurement_units_dict_id_seq")

measurement_units_dict = Table(
    "measurement_units_dict",
    metadata,
    Column("measurement_unit_id", Integer, primary_key=True, server_default=measurement_units_dict_id_seq.next_value()),
    Column("name", String(200), nullable=False, unique=True),
)

"""
Measurement units dict:
- measurement_unit_id int 
- name string(200)
"""

indicators_dict_id_seq = Sequence("indicators_dict_id_seq")

indicators_dict = Table(
    "indicators_dict",
    metadata,
    Column("indicator_id", Integer, primary_key=True, server_default=indicators_dict_id_seq.next_value()),
    Column("name_full", String(200), nullable=False, unique=True),
    Column("name_short", String(200), nullable=False),
    Column("measurement_unit_id", ForeignKey("measurement_units_dict.measurement_unit_id")),
    Column("level", Integer),
    Column("list_label", String(20), nullable=False),
    Column("parent_id", ForeignKey("indicators_dict.indicator_id")),
)

"""
Indicators dict:
- indicator_id int
- name_full string(200)
- name_short string(200)
- measurement_unit_id foreign key int
- level int
- list_label string(20)
- parent_id foreign key int
"""
