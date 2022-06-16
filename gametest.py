from game import Game2048
from agent import Agent

import numpy as np
import time
import os

from tensorflow.keras.optimizers import Adam

clear = lambda: os.system('cls')

environment = Game2048()
optimizer = Adam(learning_rate=0.01)
agent = Agent(optimizer)

batch_size = 64
num_of_episodes = 10
agent.q_network.summary()
time.sleep(5)

moveNames = ["Left", "Right", "Up", "Down"]
max_score = 0

for episode in range(0, num_of_episodes):
    environment.__init__()
    state = environment.state

    reward = 0
    terminated = False

    time_step = 0

    while not terminated:
        print(f"Move: {time_step}")
        old_score = environment.return_score()

        state = np.array(state).reshape(-1, 16)

        action = agent.play(state)
        environment.display_state()
        print()
        print("New State")

        environment.make_move(action)

        reward = environment.return_score() - old_score

        if reward == 0:
            reward = -20

        next_state = environment.state
        next_state = np.array(next_state).reshape(-1, 16)

        terminated = environment.check_for_termination()

        agent.store_experience(state, action, reward, next_state, terminated)

        state = next_state

        max_score = max(max_score, environment.score)

        environment.display_state()
        print(f"Score: {environment.score}")
        print(moveNames[action])
        print(f"Reward: {reward}")
        print(f"Epsilon: {agent.epsilon}")

        agent.epsilon = agent.starting_epsilon * ((num_of_episodes - episode + 4) / num_of_episodes) - max_score/100000

        if time_step % 100 == 0:
            agent.align_target_model()
            print("Copying weights to target!!")

        if episode > 4:
            print("Training from Memory...")
            agent.retrain(batch_size)
            print("Trained!")

        time_step += 1
        clear()

    print(f"Details | Score: {environment.score}, Moves Made: {time_step}")
    environment.display_state()
    time.sleep(5)
