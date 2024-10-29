class BaseMessage[T]:
    _text: str
    _reply_markup: T

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text) -> None:
        self._text = text

    @property
    def reply_markup(self) -> T:
        return self._reply_markup

    @reply_markup.setter
    def reply_markup(self, reply_markup) -> None:
        self._reply_markup = reply_markup

    def message(self):
        content = {"text": self.text}

        if self.reply_markup:
            content["reply_markup"] = self.reply_markup

        return content
