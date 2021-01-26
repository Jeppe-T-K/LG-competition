---
layout: page
title: LG-CoRP
subtitle: Lily's Garden Completion Rate Prediction Competition
gh-repo: Jeppe-T-K/LG-competition
---

# Overview

The Lily's Garden Completion Rate Prediction (LG-CoRP) competition is based on the mobile puzzle game Lily's Garden - a match-3 style puzzle game where player must complete the levels within a given number of moves.
The objective of this competition is to accurately predict the player completion rate of these puzzle levels.
The main research contribution of the competition is not how to optimally plan and play games but rather how to create playtesting methods that are conditioned by aggregated player behavior data across millions of players.

We provide a modified version of the game that enables simulating the main gameplay as well as data (completion rate, move limit) on the given levels.
The participants are expected to create a playtesting agent which can match the player completion rate of a level. By using the number of moves spent by the agent to complete a given level across several attempts, the completion rate is then determined by calculating the fraction of attempts that finish within a given move limit.
They are allowed to make use of the simulator and player data in any way they can otherwise.
Their method will be evaluated on a number of held-out levels which include both previous and new mechanics. The winner will be the one that achieves the lowest mean relative error in completion rate on the evaluation levels.


## Getting started

The simulator is headless build of the actual game, meaning the game logic and levels are exactly as in the live game. If you are not familiar with these types of games, visit the [Game Info](gameinfo) page for an overview of the game rules and logic. To see how we represent the live game with the simulator, visit the [Game Environment](environment) page.

To get started accessing the game simulator, visit the [Getting Started](setup) page to find help on getting up and running.


## Levels and data

For the purpose of this competition, the provided simulator is able to simulate 100 levels. In addition to this, we also provide the player move limit and completion rate.

An overview of the levels along with the data can be found on the [Levels](levels) page.


## Evaluation

As mentioned, the agents will be evaluated on a number of held-out levels. To do this, we let the agent play through these levels 2000 times each and note down the number of valid steps taken to complete these levels. The agent completion rate is then simply calculated as the number of runs that finished within the given move limit of the level.

The winner will be the contestant(s) that achieves the lowest mean relative difference between the agent and player completion rates.
