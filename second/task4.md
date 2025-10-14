Task 4: Batch Processing
In the previous task, we discussed the first step of text processing—extracting words and counting their frequencies from a single text. However, in many real-world scenarios, you’ll often need to process multiple files at once. In such cases, you’ll need to manage and analyze a collection of text files efficiently.

You may notice there is an os package is imported.
Consider doing a bit of research on how to use it to retrieve the paths of files in the data directory.
Try wrapping your logic in a function so that you can reuse it when necessary.

Task 4A:

Before starting batch file processing, you may notice  that certain very common words appear in your vocabulary list. These are known as stop words, for example words like "the", "is", "at", "on", or "and".  Such words usually carry little meaning on their own and can add unnecessary noise to your analysis. It is therefore useful to filter them out.

In this task, you need to:

Load the stop words provided in the file stop_words_english.txt.

Revise the function get_vocabs to exclude stop words while generating the vocabulary list.

Additionally, your function should also:

Filter out numbers and words composed entirely of digits

Filter out words contain any digit, e.g., app1e

Discard words with a length less than 2, as they are considered invalid and should not be kept in the vocabulary list.

Task 4B:

Now that you have an improved vocabulary generation function, you may want to use it to process a real-world dataset. In the folder named data, we have provided a collection of news headlines from four categories: Business, Sci_Tech, Sport, and World, with each category represented as a sub-folder.

Your task is to complete the function process_mini_dataset provided in the scaffold. This function should process all .txt files in the data folder.

To access the file paths of these .txt files, you may need to implement a function to do so, for completing process_mini_dataset. (check the blue block information above) 

Your tutor, Jueqing is also curious about specific categories. For example, he may want to see the vocabulary generated for a single category such as Sci_Tech. Therefore, your function process_mini_dataset should support both:

Generating a vocabulary from all .txt files across categories, and

Generating a vocabulary from files in a specific category only.

same outputs as function get_vocabs








---

任务4：批量处理
在上一任务中，我们讨论了文本处理的第一步——从单个文本中提取单词并统计其频率。然而，在许多实际场景中，你通常需要一次处理多个文件。在这种情况下，你需要高效地管理和分析一组文本文件。

你可能注意到导入了 os 包。建议你查阅一下如何使用它来获取 data 目录下文件的路径。
尝试将你的逻辑封装在函数中，以便在需要时复用。

任务4A：
在开始批量文件处理之前，你可能会注意到某些非常常见的单词出现在你的词汇表中。这些被称为停用词，例如 "the"、"is"、"at"、"on" 或 "and"。这些词本身通常没有太多意义，可能会为你的分析带来不必要的噪音。因此，过滤掉它们是有用的。

本任务你需要：
- 加载 stop_words_english.txt 文件中提供的停用词。


## 重点:
- 修改 get_vocabs 函数，在生成词汇表时排除停用词。

此外，你的函数还应：
- 过滤掉数字和完全由数字组成的单词
- 过滤掉包含任何数字的单词，例如 app1e
- 丢弃长度小于2的单词，这些被视为无效词，不应保留在词汇表中。

任务4B：
现在你已经有了改进的词汇生成函数，可能希望用它来处理真实数据集。在名为 data 的文件夹中，我们提供了四个类别的新闻标题集合：Business、Sci_Tech、Sport 和 World，每个类别对应一个子文件夹。

你的任务是完成脚手架中提供的 process_mini_dataset 函数。该函数应处理 data 文件夹下所有 .txt 文件。

为了访问这些 .txt 文件的路径，你可能需要实现一个函数来完成此操作，以便完成 process_mini_dataset。（参考上方蓝色块信息）

你的导师 Jueqing 也对特定类别感兴趣。例如，他可能希望查看仅针对 Sci_Tech 类别生成的词汇表。因此，你的 process_mini_dataset 函数应支持：
- 从所有类别的 .txt 文件生成词汇表
- 仅从某一特定类别的文件生成词汇表

输出格式与 get_vocabs 函数相同。

        