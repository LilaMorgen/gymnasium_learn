import gymnasium as gym

# 在 Gymnasium 中初始化环境非常简单，可以通过make()函数完成
# 该函数将返回一个Env供用户交互。要查看您可以创建的所有环境，请使用pprint_registry()
env = gym.make("LunarLander-v3", render_mode="human")
observation, info = env.reset()

episode_over = False
while not episode_over:
    action = env.action_space.sample()  # 使用观察和信息的 agent 策略
    observation, reward, terminated, truncated, info = env.step(action)

    episode_over = terminated or truncated

env.close()