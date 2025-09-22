import pandas as pd
import json
from typing import Dict


class TextProcessor:
    def __init__(self,
        stopwords_filepath: str,
        corpus_filepath: str,
        idx2label_filepath: str
        ) -> None:
        """
        """
        
        self.word2idx = {}
        self.idx2word = {}
        self.word_freq = {}

        with open(stopwords_filepath, "r") as f:
            #process stopwords 
            self.stopwords = set([line.strip().lower() for line in f if line.strip()])
       
        with open(idx2label_filepath, "r") as f:
            self.idx2label = json.load(f)
        
        self.corpus = pd.read_csv(corpus_filepath)
        #process corpus file
        for _, row in self.corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = str(row["text"])
            
            words = []
            temp_word = []
            for char in text.lower():
                if char.isalpha():
                    temp_word.append(char)
                else:
                    if len(temp_word) > 0:
                        word = "".join(temp_word)
                        # eliminate words that are in stopwords and words have less than 2 chars
                        if len(word) >= 2 and word not in self.stopwords:
                            words.append(word)
                        temp_word = []
            #process last word
            if len(temp_word) > 0:
                word = "".join(temp_word)
                if len(word) >= 2 and word not in self.stopwords:
                    words.append(word)
            
        #update word frequency 
            for word in words:
                if word in self.word_freq:
                    self.word_freq[word] += 1
                else:
                    self.word_freq[word] = 1
        
        self.save()

    def add_file(self, add_file_path: str) -> None:
        
        new_corpus = pd.read_csv(add_file_path)
        new_word_freq = {}
        
        for _, row in new_corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = str(row["text"])
            words = []
            temp_word = []
            for char in text.lower():
                if char.isalpha():
                    temp_word.append(char)
                else:
                    if len(temp_word) > 0:
                        word = "".join(temp_word)
                        if len(word) >= 2 and word not in self.stopwords:
                            words.append(word)
                        temp_word = []
            
            #process last word
            if len(temp_word) > 0:
                word = "".join(temp_word)
                if len(word) >= 2 and word not in self.stopwords:
                    words.append(word)
        
            #update word frequency
        for word in words:
            if word in self.word_freq:
                self.word_freq[word] += 1
            else:
                self.word_freq[word] = 1
        
            #combine all words 
        for word, freq in new_word_freq.items():
            self.word_freq[word] = self.word_freq.get(word, 0) + freq
        
        self.save()

    def delete_file(self, delete_file_path: str) -> None:
        del_corpus = pd.read_csv(delete_file_path)
        del_word_freq = {}
        
        for _, row in del_corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = str(row["text"])
            
            words = []
            temp_word = []
            for char in text.lower():
                if char.isalpha():
                    temp_word.append(char)
                else:
                    if len(temp_word) > 0:
                        word = "".join(temp_word)
                        if len(word) >= 2 and word not in self.stopwords:
                            words.append(word)
                        temp_word = []
            if len(temp_word) > 0:
                word = "".join(temp_word)
                if len(word) >= 2 and word not in self.stopwords:
                    words.append(word)
           
            for word in words:
                del_word_freq[word] = del_word_freq.get(word, 0) + 1
            
            # delete words and delete word count = 0
        for word, freq in del_word_freq.items():
            if word in self.word_freq:
                self.word_freq[word] -= freq
                if self.word_freq[word] <= 0:
                    del self.word_freq[word]
        self.save()

    def load(self) -> None:
        
        #load word frequncy 
        self.word_freq = {}
        with open("word_freq.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    word, freq = line.split()
                    self.word_freq[word] = int(freq)
        
        #load word2idx
        self.word2idx = {}
        with open("word2idx.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    word, idx = line.split()
                    self.word2idx[word] = int(idx)
        
        #load idx2word
        self.idx2word = {}
        with open("idx2word.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line: 
                    idx, word = line.split()
                    self.idx2word[int(idx)] = word

    def save(self) -> None:
        #create the text file as per requirement
        with open("word_freq.txt", "w") as f:
            for word, freq in sorted(self.word_freq.items(), key=lambda x: -x[1]):
                f.write(f"{word} {freq}\n")
        
        #create the text file as per requirement
        #save the word to index 
        word_list = sorted(self.word_freq.keys())
        
        with open("word2idx.txt", "w") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{word} {idx}\n")
        
        #create the idx to word file as per requirement
        with open("idx2word.txt", "w") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{idx} {word}\n")
        
        #update the two files
        self.word2idx = {word: idx for idx, word in enumerate(word_list)}
        self.idx2word = {idx: word for idx, word in enumerate(word_list)}


if __name__ == "__main__":
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )