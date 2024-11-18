from __future__ import annotations

from typing import (List, Optional)

from sqlalchemy.orm import (Mapped, mapped_column, relationship)

from base import Base

from sqlalchemy import String





class Pizzas(Base):
    __tablename__ = "Pizzas"


    def __repr__(self):
        return      (f"Pizza name = {self.name} \n"
                     f"Pizza cost = {self.cost} \n"
                     f"Pizza id = {self.id} \n")

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cost: Mapped[int] = mapped_column()
    description: Mapped[str] =mapped_column(String(250))

