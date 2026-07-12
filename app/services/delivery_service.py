from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.delivery import Delivery
from app.models.user import User


def accept_delivery(
    db: Session,
    delivery_id: int,
    volunteer: User,
) -> type[Delivery]:

    # Find delivery
    delivery = db.get(Delivery, delivery_id)

    if delivery is None:
        raise HTTPException(
            status_code=404,
            detail="Delivery not found",
        )

    # check if the delivery is already assigned or not
    if delivery.volunteer_id is not None:
        raise HTTPException(
            status_code=400,
            detail="Delivery already assigned",
        )

    # Assign volunteer
    delivery.volunteer_id = volunteer.id

    db.commit()
    db.refresh(delivery)

    return delivery