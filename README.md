# Sentence Splitter
A Python program to split input sentences by either specified word counts or letter counts.

## General Information
This is a simple Python program that requests an input sentence that consists of words separated with spaces. Then, it is required to select the splitting mode whether it will be by word count per line or letter count per line. Finally, the word count or the letter count is asked from the user according to the previously selected mode and the input sentence is printed as splitted lines where each line has the specified amount of words or letters.

* **Example**:

For Input Sentence: **the quick brown fox jumps over the lazy dog**

Mode: **Word Limit**\
Word Number per Line: **3**\
Output:
```
the quick brown
fox jumps over
the lazy dog
```

Mode: **Letter Limit**\
Word Number per Line: **18**\
Output:
```
the quick brown
fox jumps over the
lazy dog
```

## Technologies
This project is created with:
* Python
* Jupyter Notebook

## Setup & Run
There are 2 different files to run the program in different ways:
1. **Sentence_Splitter.ipynb** can be run with Jupyter Notebook:
```
pip install jupyter
```
```
jupyter notebook
```
2. **Sentence_Splitter.py** can be run directly with Python:
```
python Sentence_Splitter.py
```
