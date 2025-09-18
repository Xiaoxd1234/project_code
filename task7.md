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