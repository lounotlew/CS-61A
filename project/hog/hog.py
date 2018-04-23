"""The Game of Hog."""

"""57532"""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times. Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    total, count, mark = 0, 0, 0
    while count < num_rolls:
        count, val = count + 1, dice()
        if val == 1:
            mark = mark + 1
        else:
            total = total + val
    if mark > 0:
        return 1
    else:
        return total


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    first_int = opponent_score // 10
    second_int = opponent_score % 10
    if num_rolls == 0:
        return 1 + max(first_int, second_int)
    else:
        return roll_dice(num_rolls, dice)


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided

def is_prime(n):
    """Return True if a non-negative number N is prime, otherwise return
    False. 1 is not a prime number!
    """
    assert type(n) == int, 'n must be an integer.'
    assert n >= 0, 'n must be non-negative.'
    k = 2
    if n == 1 or n == 0:
        return False
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)

    while score0 < goal and score1 < goal:

        if who == 0:
            points_earned = take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
            score0 = score0 + points_earned
            if score0 > goal or score1 > goal:
                return score0, score1
            if is_prime(score0 + score1) and score0 > score1 and score0 != score1:
                score0 = score0 + points_earned
            elif is_prime(score0 + score1) and score1 > score0 and score0 != score1:
                score1 = score1 + points_earned
            if score0 > goal or score1 > goal:
                return score0, score1
            who = other(who)

        if who == 1:
            points_earned = take_turn(strategy1(score1, score0), score0, select_dice(score1, score0))
            score1 = score1 + points_earned
            if score0 > goal and score1 > goal:
                return score0, score1
            if is_prime(score0 + score1) and score0 > score1 and score0 != score1:
                score0 = score0 + points_earned
            elif is_prime(score0 + score1) and score1 > score0:
                score1 = score1 + points_earned
            if score0 > goal or score1 > goal:
                return score0, score1
            who = other(who)

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    def average(*args):
        count = 1
        total = 0
        while count <= num_samples:
            total = total + fn(*args)
            count = count + 1
        return total / num_samples
    return average

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Assume that dice always
    return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    num_dice = 1
    max_average = 0
    while num_dice <= 10:
        value = make_averaged(roll_dice, num_samples=1000)(num_dice, dice)
        if max(max_average, value) != max_average:
            max_average = value
            best_num_rolls = num_dice
        num_dice = num_dice + 1
    return best_num_rolls

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test prime_strategy
        print('prime_strategy win rate:', average_win_rate(prime_strategy))

    if False: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    first_int = opponent_score // 10
    second_int = opponent_score % 10
    if (1 + max(first_int, second_int)) >= margin:
        return 0
    else:
        return num_rolls

def prime_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and 
    rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also 
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    first_int, second_int = opponent_score // 10, opponent_score % 10
    points_free_bacon = 1 + max(first_int, second_int)

    if is_prime(score + points_free_bacon + opponent_score) and (score + points_free_bacon) >= opponent_score:
        return 0
    elif is_prime(score + points_free_bacon + opponent_score) and (score + points_free_bacon) < opponent_score:
        return num_rolls
    elif points_free_bacon >= margin:
        return 0
    else:
        return num_rolls


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    First, we check if we are rolling a four-sided or a six-sided dice. If we roll a four-sided dice,
    then we want to minimize the chances of getting Pig-Out (since the probability of rolling a 1 is 25%
    on a four-sided dice, as opposed to 17% on a six-sided dice.)

    All these scenarios assume a six-sided dice:

    If the opponent has a higher score than us, we want to take bigger risks to catch up. That's why we're
    rolling 10 dice.

    If we are in the lead, we want to take fewer risks, so we reduce the number of dice we roll.

    If we're in between 80 and 90, we still want to minimize the risk of Pig-Out, but we would still want to
    roll the right number of dice to get us as close to as 100 as possible without rolling a 1.

    Same logic for 90 < score < 100.

    For all other scenarios, we want to maximize points we earn with a six-sided dice while minimizing the risk
    of rolling a 1.

    """
    if (score + opponent_score) % 7 == 0:
        return prime_strategy(score, opponent_score, margin=5, num_rolls=4)
    if (opponent_score - score) >= 26:
        return prime_strategy(score, opponent_score, margin=10, num_rolls=10)
    elif (score - opponent_score) >= 29:
        return prime_strategy(score, opponent_score, margin=10, num_rolls =3)
    elif score >= 80 and score <= 90:
        return prime_strategy(score, opponent_score, margin=7, num_rolls=5)
    elif score >= 90 and score <= 100:
        return prime_strategy(score, opponent_score, margin=3, num_rolls=3) 
    else:
        return prime_strategy(score, opponent_score, margin=9, num_rolls=6)
    # return 5 # Replace this statement


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
