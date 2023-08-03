from dataclasses import dataclass

@dataclass
class AccountingRecord:
    """A class to represent a business accounting record."""

    date: str
    description: str
    income: float
    expenses: float
    balance: float

    def to_dict(self):
        """Convert the AccountingRecord to a dictionary."""
        return self.__dict__
