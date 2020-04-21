from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from huey_task.db_sync import Base


class Device(Base):
    # 表的名字:
    __tablename__ = 'device'

    # 表的结构:
    id = Column(BigInteger, primary_key=True)
    esn = Column(String(255))
    device_name = Column(String(255))
    device_type = Column(SmallInteger)
    status = Column(SmallInteger)
    deleted = Column(SmallInteger)
    interfaces = relationship('Interface')


class Interface(Base):
    # 表的名字:
    __tablename__ = 'interface'

    # 表的结构:
    id = Column(BigInteger, primary_key=True)
    device_id = Column(BigInteger, ForeignKey('device.id'))
    interface_type = Column(SmallInteger)
    ip = Column(String(32))
    deleted = Column(SmallInteger)
