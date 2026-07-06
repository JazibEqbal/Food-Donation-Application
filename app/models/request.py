from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, Float, String, DateTime, Enum
from sqlalchemy.orm import relationship

from app.database import Base
from app.enums.request import RequestStatus


class DonationRequest(Base):
    __tablename__ = "donation_requests"

    id = Column(Integer, primary_key=True, index=True)

    # id of requested donation
    donation_id = Column(
        Integer,
        ForeignKey("donations.id"),
        nullable=False,
    )

    # id of user requesting the donation
    requester_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    status = Column(
        Enum(RequestStatus),
        nullable=False,
        default=RequestStatus.PENDING
    )

    requested_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    # relationship to donation model
    donation = relationship(
        "Donation",
        back_populates="requests",
    )

    requester = relationship(
        "User",
        back_populates="requests"
    )
