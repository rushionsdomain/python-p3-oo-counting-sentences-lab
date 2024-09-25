class MyString:
    def __init__(self, value=""):
        """Initializes MyString with the provided value, default is an empty string."""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if value ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if value ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        if not self.value:
            return 0
        # Split the string by '.', '?', and '!', then filter out empty strings
        sentences = [s for s in self.value.replace('?', '.').replace('!', '.').split('.') if s.strip()]
        return len(sentences)