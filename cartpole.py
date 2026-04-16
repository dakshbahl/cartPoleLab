import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset()

episode_reward = 0

for step in range(500):
    if observation[2] + 0.5 * observation[3] < 0:
        action = 0
    else:
        action = 1

    observation, reward, terminated, truncated, info = env.step(action)
    episode_reward += reward

    if terminated or truncated:
        print("Episode reward:", episode_reward)
        if truncated:
            print("You made it to 500.")
        else:
            print("It fell before 500.")
        observation, info = env.reset()
        episode_reward = 0

env.close()