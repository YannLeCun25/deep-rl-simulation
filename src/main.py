from environment import CustomAIEnv

def main():
    env = CustomAIEnv()
    state = env.reset()
    print(f"Initial AI State: {state}")
    next_state, reward, done, _ = env.step(action=1)
    print(f"Action taken. Reward received: {reward}")

if __name__ == "__main__":
    main()
