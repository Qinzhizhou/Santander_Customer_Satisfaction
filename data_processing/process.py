# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2023.01.02
"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

class PROCESSING:

    def process():
        print("aaa")
        train = pd.read_csv("../data/input/train.csv")
        test = pd.read_csv("../data/input/test.csv")
        # sample = pd.read_csv("../input/santander-customer-satisfaction/sample_submission.csv")
        sample = pd.read_csv("../data/input/sample_submission.csv")
