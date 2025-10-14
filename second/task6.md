Task 6: Managing your Vocabulary - PartB
Great! Now that we have the ability to save and load the vocabulary, we can take it a step further and make our vocabulary management more flexible and generalizable.

Imagine this: you’ve added or updated some text files in your dataset. You can reuse the functions developed in previous tasks to process these new files. However, any newly discovered words or updated word frequencies will not be reflected in your current vocabulary unless explicitly updated.

To address this, your task is to design and implement functions that support incremental vocabulary updates—whether you are adding new files or removing existing ones.

Task 6A: Adding Files and Updating the Vocabulary

In this task, you will:

Accept one or more new .txt files as input.

Use the existing get_vocabs function to extract the vocabulary from these new files.

Update the saved vocabulary file word_freq.txt:

Add new words that are not currently in the vocabulary, with their corresponding frequency.

Increase the frequency of existing words if they appear in the new files.

You should also update the word2idx.txt and idx2word.txt lookup tables accordingly:

Assign new indices to newly added words.

Ensure existing mappings remain unchanged. This task simulates a live update scenario, where your vocabulary evolves as new data becomes available.

Task 6B: Deleting Files and Updating the Vocabulary

In this task, you will:

Accept one or more existing .txt files that are to be removed from your dataset.

Reuse your vocabulary extraction logic to compute the word frequencies in these files.

Update the current vocabulary file word_freq.txt:

Decrease the frequencies of words that appeared in the removed files.

Remove any words whose frequency drops to zero.

Update the word2idx.txt and idx2word.txt tables:

If a word is deleted from the vocabulary, its corresponding index should also be removed.

You may choose to reassign indices to maintain compactness or leave gaps for simplicity—justify your design choice in comments.


We provide a useful function format_file_path in util.py to help you get the path of files you may need. try to play with the function to understand it.

You can use any functions defined in previous tasks, e.g., task 4.
 os  is allowed in this task, you can use it again to format file paths if you want.


For  the three files, word_freq.txt, word2idx.txt, idx2word.txt, please do not change the files' name in the given function.

If you want to directly override the exiting files, you just need set in_path and out_path with same value

For testing purpose, we may store old files (in_path) and new files (out_path) under different directories to avoid overriding existing one. 
please note that:
in the case that out_path="result"
then you will have the three files in a folder named "result"
the directory structure will be:
result/
          word_freq.txt
          word2idx.txt
          idx2word.txt

*same thing for in_path 

=============================================

You can safely assume everything will be in same root folder, i.e.,
[task6_folder]/
                         result/
                                    word_freq.txt
                                    word2idx.txt
                                    idx2word.txt
                         data/
                         task6.py



Examples
Example of adding:

original word_freq.txt

dog 10
apple 3
master 1
once we extract words from one or more files, and we have:

word = ('dog', 'master', 'programming')
freq = (5, 49, 20)
so, we expect to see the updated word_freq.txt

master 50
programming 20
dog 15
apple 3
Example of deleting:

original word_freq.txt

dog 10
apple 3
master 1
once we want to remove/delete some files, and the words we have in these files are:

word = ('apple, 'dog')
freq = (3, 1)
so, we expect to see the updated word2idx.txt

dog 0
master 1




// ... existing code ...
任务6：管理你的词汇表 - PartB
太棒了！现在我们已经能够保存和加载词汇表，可以进一步让词汇管理更加灵活和通用。

想象一下：你在数据集中添加或更新了一些文本文件。你可以复用前面任务开发的函数来处理这些新文件。然而，任何新发现的单词或更新后的词频，除非显式更新，否则不会反映在当前词汇表中。

为了解决这个问题，你需要设计并实现支持词汇表增量更新的函数——无论是添加新文件还是移除已有文件。

任务6A：添加文件并更新词汇表
本任务中，你需要：
- 接收一个或多个新的 .txt 文件作为输入。
- 使用已有的 get_vocabs 函数从这些新文件中提取词汇。
- 更新已保存的词汇表文件 word_freq.txt：
  - 添加当前词汇表中没有的新单词及其对应词频。
  - 如果新文件中出现了已有单词，则增加其词频。
- 同时更新 word2idx.txt 和 idx2word.txt 查找表：
  - 为新添加的单词分配新索引。
  - 保证已有映射不变。本任务模拟了词汇表随新数据实时更新的场景。

任务6B：删除文件并更新词汇表
本任务中，你需要：
- 接收一个或多个需要从数据集中移除的 .txt 文件。
- 复用词汇提取逻辑，计算这些文件中的词频。
- 更新当前词汇表文件 word_freq.txt：
  - 对出现在被移除文件中的单词，减少其词频。
  - 移除词频降为零的单词。
- 更新 word2idx.txt 和 idx2word.txt 查找表：
  - 如果某个单词从词汇表中删除，其对应索引也应被移除。
  - 你可以选择重新分配索引以保持紧凑，或为简便保留空缺——请在注释中说明你的设计选择。

我们在 util.py 中提供了一个实用函数 format_file_path，帮助你获取所需文件的路径。建议尝试使用该函数以便理解其用法。

你可以使用前面任务定义的任何函数，例如 task 4。
本任务允许使用 os，你可以再次用它来格式化文件路径。

对于三个文件 word_freq.txt、word2idx.txt、idx2word.txt，请勿更改函数中给定的文件名。

如果你想直接覆盖已有文件，只需将 in_path 和 out_path 设置为相同值。

为测试目的，我们可能会将旧文件（in_path）和新文件（out_path）存储在不同目录下，以避免覆盖现有文件。
请注意：
如果 out_path="result"，那么你将在名为 "result" 的文件夹中拥有三个文件：
result/
          word_freq.txt
          word2idx.txt
          idx2word.txt
*in_path 同理

=============================================

你可以放心假设所有内容都在同一个根文件夹下，即：
[task6_folder]/
                         result/
                                    word_freq.txt
                                    word2idx.txt
                                    idx2word.txt
                         data/
                         task6.py


示例
添加示例：
原始 word_freq.txt

dog 10
apple 3
master 1
从一个或多个文件中提取单词后，得到：
word = ('dog', 'master', 'programming')
freq = (5, 49, 20)
则更新后的 word_freq.txt 应为：
master 50
programming 20
dog 15
apple 3
删除示例：
原始 word_freq.txt

dog 10
apple 3
master 1
如果要移除/删除一些文件，这些文件中的单词为：
word = ('apple', 'dog')
freq = (3, 1)
则更新后的 word2idx.txt 应为：
dog 0
master 1