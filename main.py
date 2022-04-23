from uuid import uuid4

from flox import Flox
from flox.clipboard import copy


class UUID(Flox):
    def __init__(self):
        self.generated_uuid = str(uuid4())
        super().__init__()

    def query(self, query):
        self.add_item(
            title=self.generated_uuid.upper(),
            subtitle="Click to copy.",
            method=self.copy_to_clipboard,
            parameters=[self.generated_uuid.upper()]
        )

    def context_menu(self, data):
        self.add_item(
            title=self.generated_uuid,
            subtitle="Click to copy lowercase.",
            method=self.copy_to_clipboard,
            parameters=[self.generated_uuid]
        )

    def copy_to_clipboard(self, data):
        copy(data)
        self.show_msg(
            title=self.name,
            sub_title=f"uuid copied to clipboard",
            ico_path=self.icon
        )


if __name__ == "__main__":
    UUID()
