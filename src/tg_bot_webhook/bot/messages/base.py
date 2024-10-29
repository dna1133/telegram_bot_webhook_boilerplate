from typing import Any


class BaseMessage:
    _text: str
    _reply: Any

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text) -> None:
        self._text = text

    @property
    def reply(self):
        return self._reply

    @reply.setter
    def reply(self, reply) -> None:
        self._reply = reply

    def message(self):
        content = {"text": self.text}

        if self.reply:
            content["reply"] = self.reply

        return content
