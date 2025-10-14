from typing import Tuple, List, Optional
import os


# Task 4A: get_stopwords function
def get_stopwords(stopwords_file: str) -> List[str]:
    """
    this function will read the stopwords_file and extract
    all the words in this file, turn all the words into lower-case to avoid confusion
    and return a list of strings for later calling

    parameters:
        stopwords_file[str]
    return:
        list[str]
    """
    stopwords = []
    with open(stopwords_file, "r") as stop_file:
        for line in stop_file:
            stopwords.append(line.strip().lower())
    return stopwords


# Task 4A: revised get_vocabs function
def get_vocabs(text: str, stopwords: list) -> Tuple[Tuple[str], Tuple[int]] | Tuple[()]:
    """
    this function will firstly filter words and then count each word frequency
    and return a tuple with matching word with its corresponding word count

    filterings:
        no digits
        no words less than 2 characters
        no words that are in the stopwords list

    parameter:
        text[str]
        stopwords[list]

    return:
        Tuple[Tuple[str], Tuple[int]]: a tuple with the word (string) matched to its counts(int)
        or an empty tuple
    """
    # this is to make sure the text is not empty
    if text.strip() == "":
        return ()

    # filtering words process
    text = text.lower()

    # for later adding words in the list
    words_list = []
    # for storing temporary words created during the filtering process
    temp_word = []

    for char in text:
        # store only alphabatic characters in the temporary word list
        if char.isalpha():
            temp_word.append(char)
        else:
            # filtering only alphabets and store in a temporary list for further filtering
            if len(temp_word) > 0:
                word = "".join(temp_word)
                if len(word) >= 2 and word not in stopwords:
                    words_list.append(word)
                temp_word = []
    # filter the last word
    if len(temp_word) > 0:
        word = "".join(temp_word)
        if len(word) >= 2 and word not in stopwords:
            words_list.append(word)

    # if the processed words_list is empty, then return ()
    if len(words_list) == 0:
        return ()

    # this is to create a dictionary using "word" as keys and the "words' counts" as the values
    # same as Task 3
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    the_word_list = tuple(sorted(word_count.keys()))
    # this is to use the dictionary keys to create a tuple "the_word_list"
    the_count_list = []
    for word in the_word_list:
        the_count_list.append(word_count[word])
    the_count_list = tuple(the_count_list)
    # this is to convert to a tuple for the return

    return the_word_list, the_count_list


# Task 4B access file paths function
def get_file_paths(data_path: str, category: Optional[str] = None) -> List[str]:
    """
    this function will explore the provided data path
    and return a list of all the file paths for the files in the data path folder

    Parameter:
        data_path: the data folder
        category: if specified which category (optional) within the data folder
    Return:
        list[str]: a list of file paths for the files in the data_path
    """
    # this is to decide whether a category is specified or not
    if category:
        data_path = os.path.join(data_path, category)

    txt_file_paths = []
    # this is to extract all the eligible file path from the folder
    for root, dirnames, files in os.walk(data_path):
        for filename in files:
            # extract txt files only
            if not filename.lower().endswith(".txt"):
                continue
            # not extract the stopwords file
            if filename.lower() == "stop_words_english.txt":
                continue
            filepath = os.path.join(root, filename)
            txt_file_paths.append(filepath)

    return txt_file_paths


# Task 4B process_mini_dataset function
def process_mini_dataset(
        stop_words: List[str],
        data_path: str = 'data',
        category: Optional[str] = None,
) -> Tuple[Tuple[str], Tuple[int]] | Tuple[()]:
    """
    this function will process all files in the data folder or
    a specific category inside the folder
    it will first find the file path and process the words in
    selected file and return a tuple by calling the get_vocabs function


    Parameters:
        the stopwords list
        the data folder paths
        if specified the category when calling the function
    Return:
        Tuple[Tuple[str], Tuple[int]]: a tuple with the word (string) matched to its counts(int)
        or an empty tuple

    """
    file_names = get_file_paths(data_path, category)

    # this is to ensure the file exists
    if not file_names:
        return ()

    total_vocabulary_dictionary = {}

    # extracting words and word counts from each file
    for each_file in file_names:
        with open(each_file, "r") as f:
            text = f.read()
            file_word, file_word_count = get_vocabs(text, stop_words)

            # combining all words and word counts
            for total_words, total_counts in zip(file_word, file_word_count):
                if total_words in total_vocabulary_dictionary:
                    total_vocabulary_dictionary[total_words] += total_counts
                else:
                    total_vocabulary_dictionary[total_words] = total_counts

    # this is to make sure the final vocabulary dictionary is not empty
    if not total_vocabulary_dictionary:
        return ()

    # converting to tuple for final return
    total_word_list = tuple(sorted(total_vocabulary_dictionary.keys()))

    total_count_list = []
    for total_words in total_word_list:
        total_count_list.append(total_vocabulary_dictionary[total_words])
    total_count_list = tuple(total_count_list)

    return total_word_list, total_count_list


# WARNING!!! *DO NOT* REMOVE THIS LINE
# THIS ENSURES THAT THE CODE BELOW ONLY RUNS WHEN YOU HIT THE GREEN `Run` BUTTON, AND NOT THE BLUE `Test` BUTTON
if __name__ == "__main__":
    # your testing code goes here
    stopwords = get_stopwords("data/stop_words_english.txt")
    print(process_mini_dataset(stopwords, "data/Business"))