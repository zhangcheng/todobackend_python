from sqlalchemy import Boolean, Column, Integer, String, Table, MetaData

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", String(32), primary_key=True),
    Column("title", String(255), nullable=False),
    Column("order", Integer, nullable=False),
    Column("completed", Boolean, nullable=False),
)
