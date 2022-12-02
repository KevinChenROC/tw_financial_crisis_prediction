# Description
An early warning system that automatically collect economic indicators and predicting the probabilities of stock market crashes in 10 or 20 days, with deep learning technique. For more infomation, refer to [this poster](https://drive.google.com/file/d/1GyMbHnQ0LecvTr5gDMChRze2Nxq46Og7/view?usp=sharing).

## System Architecture
Refer to [this poster](https://drive.google.com/file/d/1GyMbHnQ0LecvTr5gDMChRze2Nxq46Og7/view?usp=sharing)

## Motivation
A severe finanicial crisis can undermine the economy, leading to social and economic problems such as high unemployment rate, economic recession or depression, etc., improving the predictive performance of an EWS makes the system more valuable and reliable to assist experts to make judgement and take preventive actions. 

--- 

# Getting Started

## How to use this project
1. git clone the project
2. Prepare the prerequisites. See details below
3. Run automatic data collection and prediction in the folder of the project.
   '''
   python3 run_ETL.py
   python3 daily_prediciton.py
   '''

## Prerequisites
1. Install python dependencies in your enviroment: numpy, pandas, keras.
2. Apply for an R-Key from stock ai, and put the key in config.py

