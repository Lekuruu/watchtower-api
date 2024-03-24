
from sqlalchemy.orm import declarative_base
from sqlalchemy import func
from sqlalchemy import (
    BigInteger,
    DateTime,
    Boolean,
    Integer,
    Column,
    String,
    Float
)

Base = declarative_base()

class DBScore(Base):
    __tablename__ = 'scores'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    user_name = Column(String)
    user_country = Column(String(2), default='XX')
    server = Column(String, default='ppy.sh')
    beatmap_id = Column(Integer)
    beatmap_text = Column(String)
    beatmap_checksum = Column(String(32))
    checksum = Column(String(32))
    mode = Column(Integer)
    submitted_at = Column(DateTime, server_default=func.now())
    pp = Column(Float, nullable=True)
    acc = Column(Float)
    total_score = Column(Integer)
    max_combo = Column(Integer)
    mods = Column(Integer)
    perfect = Column(Boolean)
    passed = Column(Boolean)
    length = Column(Integer)
    grade = Column(String(2), default='F')
    c300 = Column(Integer)
    c100 = Column(Integer)
    c50 = Column(Integer)
    cgeki = Column(Integer)
    ckatu = Column(Integer)
    cmiss = Column(Integer)
    replay_filename = Column(String)
    replay_available = Column(Boolean, default=True)

class DBMessage(Base):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    sender_id = Column(Integer)
    sender_name = Column(String)
    target_name = Column(String)
    server = Column(String, default='ppy.sh')
    message = Column(String)
    created_at = Column(DateTime, server_default=func.now())
