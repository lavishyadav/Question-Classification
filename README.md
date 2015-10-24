# VQA Question-Classification
Using CNN to clasify questions into two categories i.e questions on common objects and questions on uncommon objects.

Runs on Python 2.7 and Theano 0.6

Modified from https://github.com/yoonkim/CNN_sentence

Instructions:

First

run python extract_ques.py MultipleChoice_mscoco_train2014_questions.json

It extracts questions from JSON filegiven as argument to txt file for further processing.

Then,

run python process_data.py GoogleNews-vectors-negative300.bin

This file processes the datasets files. It uses the word2vec model to convert word to word vectors. Argument must point to GoogleNews-vectors-negative300.bin file. Downloadable from https://code.google.com/p/word2vec/.

Then,

run python conv_net_question.py -nonstatic -rand num

run python conv_net_question.py -static -word2vec num

run python conv_net_question.py -nonstatic -word2vec num

It trains a CNN model to classify questions on common objects. The output of this run is two files named commonquestions.txt and uncommonquestions.txt.

This will run the CNN-rand, CNN-static, and CNN-nonstatic models respectively from the paper http://arxiv.org/abs/1408.5882.

Note : num is number of example from VQA dataset that you want to classify and use -nonstatic and -word2vec for best results.

About the datasets:-

1)MultipleChoice_mscoco_train2014_questions.json is question set from VQA dataset.

2)commonobject file contains examples of common object questions. It contains persons, entity and location classes from Question classification dataset(http://cogcomp.cs.illinois.edu/Data/QA/QC/).

3)uncommonobject contains examples of uncommon object questions. It contains description and abbreviation classes from Question classification dataset.
