from task7 import TextProcessor

def test_init_and_save():
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    tp.save()
    print("初始化并保存词汇表成功！")

def test_load():
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    tp.load()
    print("加载词汇表成功！", tp.word_freq)

def test_add_file():
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    tp.add_file("data/ag_news_test.csv")
    print("添加文件后词汇表：", tp.word_freq)

def test_delete_file():
    tp = TextProcessor(
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json",
    )
    tp.delete_file("data/ag_news_test.csv")
    print("删除文件后词汇表：", tp.word_freq)

if __name__ == "__main__":
    # test_init_and_save()
    test_load()
    # test_add_file()
    # test_delete_file()