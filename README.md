# Project2
Fintech BootCamp Project 2
# Project2

Fintech BootCamp Project 2

# Billionaire Brawl

 Final Project located in files:
     -basic_trading_algo.ip
     -Neural_Network_algorithm.ipynb
     -ML_trading_algo.ipynb
 
 ## Decription

Trading stocks successfully requires a thorough understanding of price trends and algorithm performance. We have decided to test a trading algorithm on three different stocks Amazon, Tesla and, Meta. We used supervised learning techniques to comprehend and predict the stock information to enable us to make better trading decisions, relative to a simple non-ML algorithm. We trained the model using two years of data (2012-2014) and tested the model over the subsequent 8 years. With the non-ML trading algo as the benchmark, our objective was to compare & improve trading performance using machine learning models.

## Requirements

-Project ideation
-Data fetching/API integration
-Data analysis
-Testing
-Creating documentation

## Libraries Used 
 
 -pandas 
 -pathlib
 -numpy
 -hvplot
 -matplotlib
 -sklearn
 -finta
 -holoviews
 
 ## Features 
 
 ### Stocks, Basic Trading Algorithm, Machine Learning Models
 
! [Closing Stock Prices](Resources/closing_stock_price.png)
! [Basic and Machine Learning Algorithm](Resources/algo_eval.png)
! [Classification Report Amazon](Resources/classification_amzn.png) 
! [Classifcation Report Meta](Resources/classification_meta.png)
! [Classification Report Tesla](Resources/classifcation_tsla.png)
! [AMZN Basic Algo](Images/AMZN_basic_algo.png)
! [META Basic Algo](Images/META_basic_algo.png)
! [TSLA Basic Algo](Images/TSLA_basic_algo.png)
! [AMZN Neural Network Algo](Images/AMZN_nn_algo.png)
! [META Neural Network Algo](Images/META_nn_algo.png)
! [TSLA Neural Network Algo](Images/TSLA_nn_algo.png)
 
 
 ## Finding and Conlusions
 
 While the neural network did improve trading performance over the basic algo in most cases, it is far from optimal (especially considering we fail to beat the buy-and-hold performance of the stocks from 2014-2022). 
If we had more time, we might try:
More feature engineering (adding more, removing some, principal component analyses & dimensionality reduction)
Different supervised learning models & ensemble learning methods (“Voting Classification”)
