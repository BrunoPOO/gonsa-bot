from src.config import trigram_repository, tokenizer


class DataLearner:
    def __init__(self):
        self.trigram_repository = trigram_repository
        self.tokenizer = tokenizer

    def learn(self, message):
        """
        Split message to trigrams and write to DB
        :param message: Message
        """
        print(f"> Learn: message {message}")
        words = self.tokenizer.extract_words(message)
        print(f"> Learn: words {words}")
        trigrams = self.tokenizer.split_to_trigrams(words)
        self.trigram_repository.store(message.chat_id, trigrams)
