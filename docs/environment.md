---
layout: page
title: Environment
subtitle: Using an OpenAI Gym implementation
---


# Overview

In order to communicate with the game simulator and enable easy use of various reinforcement learning (RL) methods, we have set up an [OpenAI Gym](https://gym.openai.com/docs/) environment for the game.
The main aspects of this implementation are the `step` and `reset` methods.
* `step` simulates performing a tap on a boardpiece and returns the observation, reward, *done* and info.
* `reset` starts the current level and returns the first observation of the level.
Additional information and methods are detailed in the following *Environment* section.

The purpose for providing this is to get started quickly, but you are free to modify the environment (such as reward function or observation space) for this competition in any way you want.

## Environment description

### Action space



### Observation space

Channel | Name | Description
--- | --- | ---
0 | Cell | Activated parts of the game board where board pieces can fill up the space.
1-6 | Colours | Layer representing each of the 6 colors. All colors are mechanically the same.
7-8 | Clickable true/false| Whether a board piece may be clickable. Clickable board pieces are basic tile and power pieces but it does **NOT** imply tapping on said piece is a valid move. Any other board piece is non-clickable, such as rocks or other kinds of blockers.
9 | Collectgoal | Remaining collectgoal in the specific coordinate.
10 | Basic piece | Standard board piece.
11 | Bomb | Bomb power pieces.
12 | Flask | Flask power piece.
13-14 | Rocket horizontal/vertical | Rocket power piece with the direction.
15 | Gravity | Whether a board piece has gravity. If so, the board piece will fall down if the cell below is empty. Otherwise it will stay in place.
16 | Spreadable | Typically grass pieces which can spread if none of the pieces are attacked in the previous.
17 | Healable | Regenerates 1 HP if not attacked, requiring two or more consecutive attacks to clear.
18 | Spawner | Will spawn some board piece (typically collectgoals) when attacked.
19 | Colorable | Can take on the color the piece is attack with or random if done with power piece.
20-23 | Hittable by piece / neighbor / power / cluster | How a board piece can be attacked. 


#### Board state

The



### Reward

## Additions to the environment
There are a few other attributes and methods of the environment that may be relevant to consider.

### Info
When taking a step, a dictionary with additional information is also returned. The contents of this are

Name | Type | Description
--- | --- | ---
`valid_steps` | **int** | Number of valid steps taken in environment
`total_steps` | **int** | Total number of steps taken in environment
`successful_click` | **bool** | Whether the previous action was valid or not

### Methods


# Example gameplay loop
The gameplay loop of this method is as follow:
1. To start a new game
