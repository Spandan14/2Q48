import numpy as np
import random

from collections import deque

from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
import time


class Agent:
    def __init__(self, optimizer):
        self._optimizer = optimizer
        self.experience_replay = deque(maxlen=2000)

        self.gamma = 0.3
        self.starting_epsilon = 0.4
        self.epsilon = self.starting_epsilon

        self.q_network = self.build_compile_model()
        self.target_network = self.build_compile_model()

    def align_target_model(self):
        self.target_network.set_weights(self.q_network.get_weights())

    def store_experience(self, state, action, reward, next_state, terminated):
        self.experience_replay.append((state, action, reward, next_state, terminated))

    def build_compile_model(self):
        model = Sequential()
        model.add(Dense(50, activation='relu', input_shape=(16,)))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(4, activation='linear'))

        model.compile(loss='mse', optimizer=self._optimizer)
        return model

    def play(self, state):
        if np.random.rand() <= self.epsilon:
            print(f"Moving Randomly")
            return random.randint(0, 3)

        q_values = self.q_network.predict(state)
        print(f"QValues: {q_values}")
        return np.argmax(q_values[0])

    def retrain(self, batch_size):
        minibatch = random.sample(self.experience_replay, batch_size)

        for state, action, reward, next_state, terminated in minibatch:
            target = self.q_network.predict(state)

            if terminated:
                target[0][action] = reward
            else:
                t = self.target_network.predict(next_state)
                target[0][action] = reward + self.gamma * np.amax(t)

            self.q_network.fit(state, target, epochs=1, verbose=0)

