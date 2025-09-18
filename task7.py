import pandas as pd
import json
from typing import Dict


class TextProcessor:

    def __init__(
            self,
            stopwords_filepath: str,
            corpus_filepath: str,
            idx2label_filepath: str
    ) -> None:
        # YOUR CODES START HERE
        """
        this is the initial instance building function,
        it ensures all the objects created within the TextProcessor class has the
        following attributes
        """
        self.stopwords_filepath = stopwords_filepath
        self.corpus_filepath = corpus_filepath
        self.idx2label_filepath = idx2label_filepath

        self.idx2label = {}
        self.word_freq = {}
        self.word2idx = {}
        self.idx2word = {}

        self.stopwords = []

        self.word_freq_path = "word_freq.txt"
        self.word2idx_path = "word2idx.txt"
        self.idx2word_path = "idx2word.txt"

    def add_file(self, add_file_path: str) -> None:
        # YOUR CODES START HERE
        """
        this function will read the new CSV file and extract word frequencies
        add new words and update frequencies of existing ones
        regenerate and overstite all three vocabulary files
        """
        standardised_stop_list = []
        if len(self.stopwords) > 0:
            for stopword in self.stopwords:
                cleaned_stopword = stopword.strip().lower()
                if cleaned_stopword not in standardised_stop_list:
                    standardised_stop_list.append(cleaned_stopword)
        else:
            with open(self.stopwords_filepath, "r") as stop_file:
                for line in stop_file:
                    word = line.strip().lower()
                    if word and word not in standardised_stop_list:
                        standardised_stop_list.append(word)
        self.stopwords = standardised_stop_list

        df = pd.read_csv(add_file_path)
        df = df.rename(columns={df.columns[0]: "text", df.columns[1]: "label"})
        text_to_be_processed = df["text"].astype(str).str.lower()

        new_word_freq = {}
        words_list = []
        for section in text_to_be_processed:
            cleaned_chars = []
            for ch in section:
                if ch.isalpha():
                    cleaned_chars.append(ch.lower())
                else:
                    cleaned_chars.append(" ")
            cleaned_text = "".join(cleaned_chars)
            tokens = cleaned_text.split()
            for token in tokens:
                if len(token) >= 2 and token not in self.stopwords:
                    words_list.append(token)
        #         temp_word = []
        #         for char in word:
        #             if char.isalpha():
        #                 temp_word.append(char)
        #             else:
        #                 if len(temp_word) > 0:
        #                     token = "".join(temp_word).lower()
        #                     if len(token) >= 2 and token not in self.stopwords:
        #                         words_list.append(token)
        #                     temp_word = []
        #         if len(temp_word) > 0:
        #             token = "".join(temp_word).lower()
        #             if len(token) >= 2 and token not in self.stopwords:
        #                 words_list.append(token)
        #             temp_word = []

        for word in words_list:
            if word in new_word_freq:
                new_word_freq[word] += 1
            else:
                new_word_freq[word] = 1

        for word, count in new_word_freq.items():
            if word in self.word_freq:
                self.word_freq[word] += count
            else:
                self.word_freq[word] = count

        self.save()

    def delete_file(self, delete_file_path) -> None:
        """
        this function will read the CSV file to be deleted and extract word frequencies
        add subtract the word and the word frequencies from the current vocabulary
        remove words with frequency == 0
        regenerate and overstite all three vocabulary files

        parameters:
            delete_file_path: the file to be deleted
        """

        standardised_stop_list = []
        if len(self.stopwords) > 0:
            for stopword in self.stopwords:
                cleaned_stopword = stopword.strip().lower()
                if cleaned_stopword not in standardised_stop_list:
                    standardised_stop_list.append(cleaned_stopword)
        else:
            with open(self.stopwords_filepath, "r") as stop_file:
                for line in stop_file:
                    word = line.strip().lower()
                    if word and word not in standardised_stop_list:
                        standardised_stop_list.append(word)
        self.stopwords = standardised_stop_list

        df = pd.read_csv(delete_file_path)
        df = df.rename(columns={df.columns[0]: "text", df.columns[1]: "label"})
