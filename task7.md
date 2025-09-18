Task 7: Role-Based Vocabulary Management - Part A
As your vocabulary grows and is reused across various documents, it's important to manage how it is accessed and modified. Imagine you're working in a team where different members play different roles:

Readers can load and view the vocabulary but cannot make any changes.

Admins can do everything Editors can do, and are also allowed to update the vocabulary when new files are added or existing files are deleted.

In this task, you will implement the class TextProcessor, provided in the scaffold, to simulate such role-based vocabulary management. You are expected to build upon the functionality developed in previous tasks, and extend it into a well-structured, object-oriented system.

📌 Task Objective
You are required to complete the TextProcessor class by implementing methods that:

Load and clean a corpus of text based on a given stopword list and punctuation rules.

Generate the vocabulary and compute word frequencies.

Save the vocabulary to disk in three formats:

A word-frequency file (word_freq.txt)

A word-to-index lookup table (word2idx.txt)

An index-to-word reverse lookup table (idx2word.txt)

Load these saved vocabularies and lookup tables when needed.

Update the vocabulary by adding new documents or removing existing ones, and reflecting these updates all related files.

🧠 Implementation Requirements
Please follow these strict implementation rules:

You must not modify the parameters of any provided methods or the class attributes.

You are encouraged to reuse code from previous tasks, but you should adapt it to fit into the current class-based design.

You must not remove any code that is already present in the scaffold.

Place all your implementations after the line # YOUR CODES START HERE in each method.

If any internal data (e.g., self.words_freq) is updated, the corresponding output files must be updated immediately.

You are provided with some predefined attributes in the constructor, and all of them must be used in your implementation.

🛠️ Functional Highlights
Your completed TextProcessor class should support the following functionality:

Corpus Initialization

Load the input CSV corpus and map numerical labels to label names using idx2label.json. Concatenate all texts and generate a cleaned vocabulary list, excluding:

Stop words

Words with length < 2

Non-alphabetic tokens

Vocabulary Saving

Store the vocabulary in three separate files:

word_freq.txt: sorted by descending frequency

word2idx.txt: word → index, sorted alphabetically

idx2word.txt: index → word, reverse mapping of the above

Vocabulary Loading

Implement the load method to restore vocabulary from the saved files.

Adding New Documents

Implement the add_file to:

Read the new .csv file

Extract word frequencies from it

Add new words and update frequencies of existing ones

Regenerate and overwrite all three vocabulary files

Removing Documents

Implement the delete_file to:

Read the .csv file to be removed

Compute word frequencies

Subtract frequencies from the current vocabulary

Remove words whose frequency drops to 0

Regenerate and overwrite all three vocabulary files

---

任务7：基于角色的词汇管理 - Part A
随着你的词汇量不断增长并在不同文档中复用，如何管理其访问和修改变得尤为重要。想象你在一个团队中，不同成员有不同的角色：

读者可以加载和查看词汇表，但不能进行任何更改。

管理员拥有编辑者的所有权限，并且可以在添加新文件或删除现有文件时更新词汇表。

本任务要求你实现 scaffold 中提供的 TextProcessor 类，以模拟这种基于角色的词汇管理。你需要在前面任务的基础上扩展功能，构建一个结构良好的面向对象系统。

📌 任务目标
你需要通过实现以下方法完善 TextProcessor 类：

根据给定的停用词列表和标点规则加载并清洗语料。

生成词汇表并计算词频。

将词汇表以三种格式保存到磁盘：

词频文件（word_freq.txt）

词到索引查找表（word2idx.txt）

索引到词反查表（idx2word.txt）

在需要时加载这些已保存的词汇表和查找表。

通过添加新文档或删除现有文档来更新词汇表，并同步更新所有相关文件。

🧠 实现要求
请严格遵循以下实现规则：

不得修改任何已提供方法的参数或类属性。

鼓励复用前面任务的代码，但需适应当前的类设计。

不得移除 scaffold 中已存在的任何代码。

所有实现均需写在每个方法的 # YOUR CODES START HERE 之后。

如果任何内部数据（如 self.words_freq）被更新，必须立即同步更新对应输出文件。

构造函数中已提供的属性必须全部使用。

🛠️ 功能亮点
你完成的 TextProcessor 类应支持以下功能：

语料初始化

加载输入的 CSV 语料，并使用 idx2label.json 将数字标签映射为标签名。拼接所有文本并生成清洗后的词汇表，排除：

停用词

长度小于2的词

非字母词

词汇保存

将词汇表分别存储到三个文件：

word_freq.txt：按词频降序排序

word2idx.txt：词→索引，按字母排序

idx2word.txt：索引→词，上述的反向映射

词汇加载

实现 load 方法，从保存的文件中恢复词汇表。

添加新文档

实现 add_file 方法：

读取新的 .csv 文件

提取其中的词频

新增词汇并更新已有词的频率

重新生成并覆盖所有三个词汇文件

删除文档

实现 delete_file 方法：

读取待删除的 .csv 文件

计算词频

从当前词汇表中减去对应频率

移除频率降为0的词

重新生成并覆盖所有三个词汇文件