from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    first_name:Mapped[str] = mapped_column(String(255))
    last_name:Mapped[str] = mapped_column(String(255))
    password:Mapped[str] = mapped_column(String(255))

    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="user")


