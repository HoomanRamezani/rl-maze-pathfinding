def compute_win_rate(history):
    win_history = history['win_history']
    wins = sum(win_history)
    total = len(win_history)
    win_rate = wins / total if total > 0 else 0
    return win_rate

def compute_average_reward(history):
    rewards = history['rewards']
    average_reward = sum(rewards) / len(rewards) if rewards else 0
    return average_reward

def compute_average_trials_to_success(history):
    trials = history['trials_to_win']
    average_trials = sum(trials) / len(trials) if trials else 0
    return average_trials
