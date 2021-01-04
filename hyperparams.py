#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import keras
import tensorflow as tf
from tensorflow.keras import activations, optimizers



activation = [activations.linear, activations.relu,activations.sigmoid, activations.softmax, activations.softplus, activations.softsign, activations.tanh, activations.selu, activations.elu, activations.exponential]


optimizers = [optimizers.Adam, optimizers.RMSprop, optimizers.Adagrad, optimizers.Adamax, optimizers.Nadam]



initializers =[tf.keras.initializers.RandomNormal(mean=0., stddev=1.), tf.keras.initializers.RandomUniform(),
       tf.keras.initializers.GlorotNormal(), tf.keras.initializers.GlorotUniform()]
