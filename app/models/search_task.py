"""
Задача поиска — одно ключевое слово/название вакансии.

Пользователь заводит несколько задач (по одной на искомую должность), каждая
ищет строго по своему названию. Движок прогоняет автоотклик по всем активным
задачам. Прочие фильтры (регион, формат, письма, лимит, умный отбор) — общие
на пользователя (UserSettings).
"""
from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class SearchTask(Base, TimestampMixin):
    __tablename__ = "search_tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    keyword: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
