from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from datetime import  date


    

class Task(Base):
        __tablename__ = "tasks"
        id: Mapped[int] = mapped_column(primary_key=True)
        title: Mapped[str] = mapped_column(String(255))
        status: Mapped[str] = mapped_column(String(255))
        type: Mapped[str] = mapped_column(String(255))
        priority: Mapped[str] = mapped_column(String(255))
        description: Mapped[str] = mapped_column(String(255))
        due_date: Mapped[date] = mapped_column(Date, nullable=True)
        user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False) 
        assignee: Mapped[str] = mapped_column(String(255), nullable=True)
        screen_shot: Mapped[str] = mapped_column(String(255), nullable=True)

        user: Mapped["User"] = relationship("User", back_populates="tasks")