from .base import Base


class Start(Base):
    name = "start"

    def execute(self, command):
        self.reply(command, "Oie :3")
