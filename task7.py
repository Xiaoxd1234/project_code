import pandas as pd
import json
from typing import Dict


class TextProcessor:
    def __init__(self,
        stopwords_filepath: str,
        corpus_filepath: str,
        idx2label_filepath: str
        ) -> None:
        with open(stopwords_filepath, "r", encoding="utf-8") as f:
            self.stopwords = set([line.strip().lower() for line in f])
        with open(idx2label_filepath, "r", encoding="utf-8") as f:
            self.idx2label = json.load(f)
        self.corpus = pd.read_csv(corpus_filepath)
        self.word_freq = {}
        for _, row in self.corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = label_name + " " + str(row["text"])
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
                self.word_freq[word] = self.word_freq.get(word, 0) + 1
     

    def add_file(self, add_file_path: str) -> None:
        import pandas as pd
        # 读取新csv
        new_corpus = pd.read_csv(add_file_path)
        new_word_freq = {}
        for _, row in new_corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = label_name + " " + str(row["text"])
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
                new_word_freq[word] = new_word_freq.get(word, 0) + 1
        # 合并词频
        for word, freq in new_word_freq.items():
            self.word_freq[word] = self.word_freq.get(word, 0) + freq
        # 重新生成并覆盖词汇文件
        with open("word_freq.txt", "w", encoding="utf-8") as f:
            for word, freq in sorted(self.word_freq.items(), key=lambda x: -x[1]):
                f.write(f"{word} {freq}\n")
        word_list = sorted(self.word_freq.keys())
        with open("word2idx.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{word} {idx}\n")
        with open("idx2word.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{idx} {word}\n")

    def delete_file(self, delete_file_path: str) -> None:
        import pandas as pd
        # 读取待删除csv
        del_corpus = pd.read_csv(delete_file_path)
        del_word_freq = {}
        for _, row in del_corpus.iterrows():
            label_name = self.idx2label[str(row["label"])]
            text = label_name + " " + str(row["text"])
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
        # 从词表中减去对应词频
        for word, freq in del_word_freq.items():
            if word in self.word_freq:
                self.word_freq[word] -= freq
                if self.word_freq[word] <= 0:
                    del self.word_freq[word]
        # 重新生成并覆盖词汇文件
        with open("word_freq.txt", "w", encoding="utf-8") as f:
            for word, freq in sorted(self.word_freq.items(), key=lambda x: -x[1]):
                f.write(f"{word} {freq}\n")
        word_list = sorted(self.word_freq.keys())
        with open("word2idx.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{word} {idx}\n")
        with open("idx2word.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{idx} {word}\n")

    def load(self) -> None:
        # 恢复 word_freq
        self.word_freq = {}
        with open("word_freq.txt", "r", encoding="utf-8") as f:
            for line in f:
                word, freq = line.strip().split()
                self.word_freq[word] = int(freq)
        # 恢复 word2idx
        self.word2idx = {}
        with open("word2idx.txt", "r", encoding="utf-8") as f:
            for line in f:
                word, idx = line.strip().split()
                self.word2idx[word] = int(idx)
        # 恢复 idx2word
        self.idx2word = {}
        with open("idx2word.txt", "r", encoding="utf-8") as f:
            for line in f:
                idx, word = line.strip().split()
                self.idx2word[int(idx)] = word

    def save(self) -> None:
        # 保存 word_freq.txt，按词频降序
        with open("word_freq.txt", "w", encoding="utf-8") as f:
            for word, freq in sorted(self.word_freq.items(), key=lambda x: -x[1]):
                f.write(f"{word} {freq}\n")
        # 保存 word2idx.txt，词→索引，按字母排序
        word_list = sorted(self.word_freq.keys())
        with open("word2idx.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{word} {idx}\n")
        # 保存 idx2word.txt，索引→词
        with open("idx2word.txt", "w", encoding="utf-8") as f:
            for idx, word in enumerate(word_list):
                f.write(f"{idx} {word}\n")


if __name__ == "__main__":
    
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    tp.save()