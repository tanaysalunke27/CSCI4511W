import torch
from agent import Agent
from game import Game

if __name__ == "__main__":
    # Initialize the Agent and load the trained model
    model_path = 'model.pth'
    agent = Agent(source_path=model_path, dest_path=None, plotting=True)

    # Number of test episodes
    num_episodes = 100  # Change this to test on more games
    print(f"Testing the model for {num_episodes} episodes...\n")

    scores = []

    for episode in range(num_episodes):
        env = Game()
        state = env.reset()
        state = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
        done = False

        while not done:
            # Select action using the trained model
            with torch.no_grad():
                action = agent.select_action(state, train=False)

            # Step the environment
            next_state, _, terminated, truncated = env.step(action)
            done = terminated or truncated

            if not done:
                state = torch.tensor(next_state, dtype=torch.float32).unsqueeze(0)

        # Log the score
        score = env.current_score()
        scores.append(score)
        print(f"Episode {episode + 1}: Score = {score}")

    # Print average performance
    average_score = sum(scores) / len(scores)
    print("\nTesting Complete!")
    print(f"Average Score over {num_episodes} episodes: {average_score:.2f}")
