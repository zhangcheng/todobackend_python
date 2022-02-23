from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, MetaData

metadata = MetaData()

todos = Table(
    "todos",
    metadata,
    Column("id", String(32), primary_key=True),
    Column("title", String(255), nullable=False),
)
