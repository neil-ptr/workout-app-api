from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


from ..database import Base


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    height = Column(Integer)
    weight = Column(Integer)
    age = Column(Integer)

    user_id = Column(ForeignKey("users.id"))
    user = relationship("User", back_populates="account")