from task7 import TextProcessor

if __name__ == "__main__":
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    print("初始化词汇表：", tp.word_freq)
    tp.save()
    print("已保存词汇表。")
    tp.load()
    print("加载后的词汇表：", tp.word_freq)
    tp.add_file("data/add.csv")
    print("添加文件后的词汇表：", tp.word_freq)
    tp.delete_file("data/delete.csv")
    print("删除文件后的词汇表：", tp.word_freq)