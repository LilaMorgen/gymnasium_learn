import gymnasium as gym

# 初始化环境
env = gym.make("LunarLander-v3", render_mode="human")

# 重置环境以生成第一个观测值
observation, info = env.reset(seed=42)
for _ in range(1000):
    # 这是您将插入策略的位置
    action = env.action_space.sample()

    # 步骤（转换）通过操作
    # 接收下一个观察、奖励以及剧集是否已终止或截断
    observation, reward, terminated, truncated, info = env.step(action)

    # 如果剧集已结束，那么我们可以重置以开始新的剧集
    if terminated or truncated:
        observation, info = env.reset()

env.close()