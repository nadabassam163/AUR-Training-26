from abc import ABC, abstractmethod
from enum import Enum


class ItemStatus(Enum):
    AVAILABLE = "AVAILABLE"
    CHECKED_OUT = "CHECKED_OUT"
    LOST = "LOST"


class LibraryItem(ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        LibraryItem._registry[cls.__name__] = cls

    def __init__(self, title, status=ItemStatus.AVAILABLE):
        self._title = title
        self._status = status

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @property
    @abstractmethod
    def loan_period(self):
        """Return the loan period in days."""
        pass

    def checkout(self):
        if self._status != ItemStatus.AVAILABLE:
            raise ValueError("Item is not available for checkout.")

        self._status = ItemStatus.CHECKED_OUT

    def return_item(self):
        if self._status != ItemStatus.CHECKED_OUT:
            raise ValueError("Item is not currently checked out.")

        self._status = ItemStatus.AVAILABLE

    def mark_lost(self):
        if self._status == ItemStatus.LOST:
            raise ValueError("Item is already marked as lost.")

        self._status = ItemStatus.LOST

    def __lt__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented

        return self.title.lower() < other.title.lower()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(title={self.title!r}, status={self.status.name!r})"
        )

    def __str__(self):
        return (
            f"{self.title} ({self.__class__.__name__}) - "
            f"{self.status.name.title().replace('_', ' ')}"
        )

    @classmethod
    def from_dict(cls, data):
        item_type = data.get("type")

        item_class = cls._registry.get(item_type)

        if item_class is None:
            raise ValueError(f"Unknown item type: {item_type}")

        return item_class.from_dict(data)

    @staticmethod
    def validate_isbn(isbn):
        """
        Validate an ISBN-13 checksum.

        Returns True if the ISBN-13 is valid, otherwise False.
        Hyphens and spaces are allowed.
        """
        digits = isbn.replace("-", "").replace(" ", "")

        if len(digits) != 13 or not digits.isdigit():
            return False

        total = 0

        for i, digit in enumerate(digits):
            value = int(digit)

            if i % 2 == 0:
                total += value
            else:
                total += value * 3

        return total % 10 == 0


class Book(LibraryItem):

    def __init__(self, title, author, isbn, status=ItemStatus.AVAILABLE):
        super().__init__(title, status)
        self.author = author
        self.isbn = isbn

    @property
    def loan_period(self):
        return 21

    @classmethod
    def from_dict(cls, data):
        status = ItemStatus[data.get("status", "AVAILABLE")]

        return cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            status=status
        )


class DVD(LibraryItem):

    def __init__(self, title, director, status=ItemStatus.AVAILABLE):
        super().__init__(title, status)
        self.director = director

    @property
    def loan_period(self):
        return 5

    @classmethod
    def from_dict(cls, data):
        status = ItemStatus[data.get("status", "AVAILABLE")]

        return cls(
            title=data["title"],
            director=data["director"],
            status=status
        )


class Magazine(LibraryItem):

    def __init__(self, title, issue, status=ItemStatus.AVAILABLE):
        super().__init__(title, status)
        self.issue = issue

    @property
    def loan_period(self):
        return 14

    @classmethod
    def from_dict(cls, data):
        status = ItemStatus[data.get("status", "AVAILABLE")]

        return cls(
            title=data["title"],
            issue=data["issue"],
            status=status
        )


class Library:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added.")

        self._items.append(item)

    def checkout_item(self, title):
        item = self.find_by_title(title)

        if item is None:
            raise ValueError(f"No item found with title: {title}")

        item.checkout()

    def return_item(self, title):
        item = self.find_by_title(title)

        if item is None:
            raise ValueError(f"No item found with title: {title}")

        item.return_item()

    def find_by_title(self, title):
        for item in self._items:
            if item.title.lower() == title.lower():
                return item

        return None

    def list_available(self):
        return [
            item
            for item in self._items
            if item.status == ItemStatus.AVAILABLE
        ]

    def get_items(self):
        return list(self._items)