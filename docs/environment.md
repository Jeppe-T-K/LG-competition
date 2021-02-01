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

Board state

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
