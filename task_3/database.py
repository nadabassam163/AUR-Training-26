from library import LibraryItem


class Database:

    def __init__(self, filename="database.txt"):
        self.filename = filename

    def save(self, items):
        with open(self.filename, "w", encoding="utf-8") as file:
            for item in items:
                data = self._item_to_dict(item)

                line = "|".join(
                    f"{key}={value}"
                    for key, value in data.items()
                )

                file.write(line + "\n")

    def load(self):
        items = []

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if not line:
                        continue

                    data = self._parse_line(line)
                    item = LibraryItem.from_dict(data)
                    items.append(item)

        except FileNotFoundError:
            return []

        return items

    @staticmethod
    def _parse_line(line):
        data = {}

        for field in line.split("|"):
            key, value = field.split("=", 1)
            data[key] = value

        return data

    @staticmethod
    def _item_to_dict(item):
        data = {
            "type": item.__class__.__name__,
            "title": item.title,
            "status": item.status.name
        }

        # Use the object's attributes dynamically.
        excluded = {"_title", "_status"}

        for key, value in vars(item).items():
            if key not in excluded:
                data[key.lstrip("_")] = value

        return data