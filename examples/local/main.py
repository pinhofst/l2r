import logging
from src.l2r.l2r import build_env
from src.l2r.l2r import RacingEnv

"""
This example assumes you have the simulator is running on your
local computer.
"""


def race_n_episodes(env: RacingEnv, num_episodes: int = 5):
    """Complete an episode in the environment"""

    for ep in range(num_episodes):
        logging.info(f"Episode {ep+1} of {num_episodes}")

        obs = env.reset()
        total_reward = 0

        while True:
            obs, reward, done, info = env.step(action=[0.00, 1.00])
            total_reward += reward
            if done:
                logging.info(f"Completed episode with reward: {total_reward}")
                break


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Build the environment
    env = build_env()

    # Race!
    race_n_episodes(env=env)
