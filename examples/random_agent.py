import gym
from game.simulator import Simulator

# Loading in simulator and environment
sim = Simulator(host="http://localhost:8090")
env = gym.make('lg-competition-v0', level=1, simulator=sim)

# To start a new playthrough, reset environment first to get initial obs. space
obs = env.reset(seed=42)
print(f"Shape of observations: {obs.shape}")

# Taking a random step in env:
action = env.action_space.sample()  # OpenAI Gym build-in random sampling
print(f"Chosen action: {action}")

obs, reward, done, info_dict = env.step(action)
print(f"Reward: {reward}, finished level: {done}, additional info: {info_dict}")

# Continuing until level is complete:
rewards = reward
while not done:
    action = env.action_space.sample()  # OpenAI Gym build-in random sampling
    obs, reward, done, info_dict = env.step(action)
    rewards += reward
print(f"Final reward: {rewards}")
print(f"{info_dict}")

# To start a new loop, remember to reset environment. If you want to select another level, you can do as following:
env.set_level(2)
obs = env.reset(seed=42+1)
rewards = 0
done = False
while not done:
    action = env.action_space.sample()  # OpenAI Gym build-in random sampling
    obs, reward, done, info_dict = env.step(action)
    rewards += reward
print(f"Level 2 final reward: {rewards}")
print(f"{info_dict}")
...
