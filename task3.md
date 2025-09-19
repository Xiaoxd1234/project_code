Task 3: Preliminary Step of Text Processing
Now, you might be wondering where the marks for Tasks 1 and 2 come from. Your tutor, Jueqing, is asking for your help in providing a standard solution for the assignment on which these marks are based. To begin, here’s a simple example that has been extracted from a more complex task. You are given a string, and your job is to extract all the words from it and count how many times each word appears. For example:

the_example_str = "you are good at python , and you will be master of programming ."
As a result，you should have:

the_word_list = ('and', 'are', 'at', 'be', 'good', 'master', 'of', 'programming', 'python', 'will', 'you')
the_count_list = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)
you may notice that:

The given string already separates each word by a space;

Only words are preserved; for example, there are no punctuation marks;

Only unique words will be stored in the word list;

The words list is sorted, and the count list follows the order of each word.

Task 3A

You are provided with a empty function get_vocabs_simple in the scaffold, which should be used to process simple strings like the example above. You may assume that "simple strings" are strings in which words and punctuation marks are concatenated using a single space.

You don't need to further process the strings. 
The only task here is to extract words.
Task 3B's rules are not applicable to this one.


Task 3B

Now, you've already touched on the core step of text processing: generating the vocabulary list. To make it more flexible for general use, we should extend the above function—called get_vocabs—to handle more general types of text. For example:

the_real_str = "You are good at Python, and you will be master of programming."
As a result，you should have:

the_word_list = ('and', 'are', 'at', 'be', 'good', 'master', 'of', 'programming', 'python', 'will', 'you')
the_count_list = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)
One more example will be:

the_real_str = "Hello, apple?! 'You you', yOU, heLLo, I've, At, apPle"
the_word_list = ('apple', 'at', 'hello', 'i', 've', 'you')
the_count_list = (2, 1, 2, 1, 1, 3)
Besides what has been mentioned above, you may also notice and assume that:

All words have been converted to lowercase.

Even when punctuation marks directly follow a word, they are cleaned and not stored as separate words in the vocabulary list.

Contractions will always follow the correct English syntax

Additionally, as mentioned earlier:

The given string already separates each word with a space.

Only words are preserved; for example, no punctuation marks are included.

Only unique words will be stored in the vocabulary list.

The words list is sorted, and the count list follows the order of each word.

You are allowed to modify the import statements in the scaffold; but you are not allowed to import any modules which weren't originally imported in the scaffold.








          
任务3：文本处理的初步步骤

现在，你可能会好奇任务1和任务2的分数是从哪里来的。你的导师Jueqing希望你帮助提供一个标准的作业解决方案，这些分数就是基于这个作业。首先，这里有一个从更复杂任务中提取出来的简单例子。你会得到一个字符串，你的任务是从中提取所有单词，并统计每个单词出现的次数。例如：

the_example_str = "you are good at python , and you will be master of programming ."

结果你应该得到：
the_word_list = ('and', 'are', 'at', 'be', 'good', 'master', 'of', 'programming', 'python', 'will', 'you')
the_count_list = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)
你可能会注意到：
- 给定的字符串已经用空格分隔每个单词；
- 只保留单词，例如没有标点符号；
- 单词列表只存储唯一单词；
- 单词列表已排序，计数列表与单词顺序一致。

任务3A
脚手架中已提供空函数get_vocabs_simple，用于处理如上例的简单字符串。你可以假设“简单字符串”是指单词和标点用单个空格连接的字符串。
你不需要进一步处理字符串，此处唯一任务是提取单词。任务3B的规则不适用于此处。

任务3B
现在，你已经接触到文本处理的核心步骤：生成词汇表。为了让它更灵活地通用，我们应扩展上述函数（get_vocabs），以处理更一般类型的文本。例如：

the_real_str = "You are good at Python, and you will be master of programming."

结果你应该得到：
the_word_list = ('and', 'are', 'at', 'be', 'good', 'master', 'of', 'programming', 'python', 'will', 'you')
the_count_list = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2)

再举一个例子：
the_real_str = "Hello, apple?! 'You you', yOU, heLLo, I've, At, apPle"
the_word_list = ('apple', 'at', 'hello', 'i', 've', 'you')
the_count_list = (2, 1, 2, 1, 1, 3)

除了上述内容，你还可以注意并假设：
- 所有单词都已转换为小写；
- 即使标点直接跟在单词后面，也会被清理，不会作为单独单词存储在词汇表中；
- 缩写总是遵循正确的英语语法。

此外，如前所述：
- 给定字符串已经用空格分隔每个单词；
- 只保留单词，例如不包含标点符号；
- 词汇表只存储唯一单词；
- 单词列表已排序，计数列表与单词顺序一致。

你可以修改脚手架中的import语句，但不能导入脚手架未原本导入的模块。
        