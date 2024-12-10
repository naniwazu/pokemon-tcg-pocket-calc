import matplotlib.pyplot as plt
import numpy as np

DEFAULT_N_MAX = 1000


def calculate_consecutive_win_probabilities(
    n_max: int = DEFAULT_N_MAX, goal: int = 5, win_rate: float = 0.5
) -> list[float]:
    """
    Calculate the probability of achieving a specified number of consecutive wins within n games

    Args:
        n_max (int): Total number of games
        goal (int): Target number of consecutive wins
        win_rate (float): Win probability per game

    Returns:
        list[float]: Probability of achieving the target consecutive wins
    """
    # Number of states: from 0 consecutive wins to the specified goal
    state_count = goal + 1

    # Initialize transition matrix
    P = np.zeros((state_count, state_count))

    # Set transition probabilities
    for i in range(state_count - 1):
        # When winning
        P[i, i + 1] = win_rate

        # When losing
        P[i, 0] = 1 - win_rate

    # Final state (specified consecutive wins) does not change
    P[state_count - 1, state_count - 1] = 1.0
    probabilities = [1 if goal == 0 else 0]
    probabilities.append(P[0, goal])
    current_matrix = np.copy(P)
    for _ in range(2, n_max + 1):
        current_matrix = np.dot(current_matrix, P)
        probabilities.append(current_matrix[0, goal])

    return probabilities


def plot_consecutive_win_probabilities(
    goal: int = 5, n_max: int = DEFAULT_N_MAX, win_rate: float = 0.5
) -> None:
    """
    Plot the graph of consecutive win probabilities

    Args:
        goal (int): Target number of consecutive wins
        n_max (int): Maximum number of games to plot
        win_rate (float): Win probability per game
    """
    probabilities = calculate_consecutive_win_probabilities(n_max, goal, win_rate)

    plt.switch_backend("Agg")
    plt.figure(figsize=(10, 6))
    plt.plot(range(n_max + 1), probabilities)
    plt.title(f"Probability of {goal} Consecutive Wins (Win Rate: {win_rate*100:.0f}%)")
    plt.xlabel("Number of Games")
    plt.ylabel(f"Probability of {goal} Consecutive Wins")
    plt.grid(True)
    plt.savefig(f"goal_{goal}_prob_{int(win_rate*100)}.png")
    plt.close()


def find_games_to_reach_probability(
    win_rates: list[float],
    target_prob: float = 0.95,
    goal: int = 5,
    max_games: int = DEFAULT_N_MAX,
) -> dict[float, int]:
    """
    Calculate the number of games required to reach a specified probability

    Args:
        win_rates (list[float]): List of win rates
        target_prob (float): Target probability
        goal (int): Target number of consecutive wins
        max_games (int): Maximum number of games to search

    Returns:
        dict: Number of games required for each win rate
    """
    required_games = {}

    for rate in win_rates:
        probabilities = calculate_consecutive_win_probabilities(
            n_max=max_games, win_rate=rate, goal=goal
        )
        for n, prob in enumerate(probabilities):
            if prob >= target_prob:
                required_games[rate] = n
                break
        else:
            required_games[rate] = None  # If target probability is not reached

    return required_games


# Main execution
if __name__ == "__main__":
    win_rates = [0.3, 0.4, 0.5, 0.6, 0.7]
    for rate in win_rates:
        plot_consecutive_win_probabilities(win_rate=rate)
    # Calculate the number of games to reach 95% for different win rates
    results = find_games_to_reach_probability(win_rates=win_rates)

    # Display results
    print("Number of games to reach 95% for each win rate:")
    for rate, games in results.items():
        print(
            f"Win rate {rate*100:.0f}%: "
            + (
                f"{games} games"
                if games is not None
                else f"More than {DEFAULT_N_MAX} games"
            )
        )
