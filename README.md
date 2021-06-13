# MLiP
This repository contains code and supplementary material for participated Kaggle Challenges.

## Challenge 1: I'm Something of a Painter Myself 
The first challenge can be found on Kaggle: https://www.kaggle.com/c/gan-getting-started.
This challenge includes style transfer from Monet style to the 'COCO2017' dataset (https://www.tensorflow.org/datasets/catalog/coco).
As a result, we created 7000 images in the style of Monet.

We are inspired by the model introduced by Johnson et al. [1]. This model introduces neural style transfer with the use of a pre-trained VGG-16 network. 

The code and results of this challenge can be found in the corresponding folder: _Challenge1 - I'm Something of a Painter myself_.
This folder exists of the following files:
- johnson-v2.ipynb; A python notebook containing the source code
- johnson-v2.zip; A zipped version of the notebook (as it is quite large)
- model.zip; The final model created for neural style transfer
- graphs.zip; Graphs with various model outcomes (loss, norm of weights, mean gradient and variance of gradient)
- johnson_v2_best.ipynb; The notebook which gave the highest score in the challenge (but we don't use this as our final submission).
- johnson-v2_best.zip; A zipped version of the notebook (as it is quite large)



[1]Johnson, Justin, e.a. ‘Perceptual Losses for Real-Time Style Transfer and Super-Resolution’. arXiv:1603.08155 [cs], maart 2016. arXiv.org, http://arxiv.org/abs/1603.08155.


## Challenge 2: Coleridge Initiative - Show US the Data
The second challenge can be found on Kaggle: https://www.kaggle.com/c/coleridgeinitiative-show-us-the-data.  
This challenge includes the recognition of public dataset in scientifc papers.

The code and results of this challenge can be found in the corresponding folder: _Challenge2 - Coleridge Initiative - Show US the Data_.
This folder exists of the following files:
- Part I_Creating_Dataset.ipynb; A python notebook containing the source code for creating the dataset for training.
- Part_IIa_BERT_Training.ipynb; A python notebook containing the source code for training the BERT model.
- Part_IIb_SciBERT_Training.ipynb; A python notebook containing the source code for training the SciBERT model.
- Part III_With_LiteralMatching_SciBERT.ipynb; A python notebook containing the source code for predicting labels on the test set using the SciBERT model with literal matching (and final submission)
- Part III_Without_LiteralMatching_SciBERT.ipynb; A python notebook containing the source code for predicting labels on the test set using the SciBERT model without literal matching
- Part III_With_LiteralMatching_BERT.ipynb; A python notebook containing the source code for predicting labels on the test set using the SciBERT model with literal matching
- Part III_Without_LiteralMatching_BERT.ipynb; A python notebook containing the source code for predicting labels on the test set using the SciBERT model without literal matching
- trianingResults.json; the trainnig loss and learning rate of the training process of both BERT and SciBERT
- trainingProcess.py; A python script to create visualization for the training loss and learning rate of BERT and SciBERT.
- Figures/ ; The outcomes of trainingProcess.py

