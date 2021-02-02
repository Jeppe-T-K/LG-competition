---
layout: page
title: Tactile Games Playtest Agent
subtitle: Level Difficulty Prediction of Lily's Garden Levels
gh-repo: Jeppe-T-K/LG-competition
---

# Overview

The <a href="https://tactilegames.com/">Tactile Games</a> Playtest Agent competition is based on our game <a href="https://tactilegames.com/lilys-garden/">Lily's Garden</a>. The objective of this competition is to develop an agent capable of accurately predicting the difficulty of a series of evaluation levels. In this context, <em>level difficulty</em> will be understood as the average number of attempts that a human player makes before completing the level. Equivalently, one can also consider the level's <em>completion rate</em> which is simply defined as 1 divided by level difficulty. 

Participants in this competition will have access to a modified version of the game that enables simulating the main gameplay. Data from real players (i.e., completion rate) on the training levels will be provided as well. 

The competition is about predicting level difficulty as opposed to developing an agent capable of playing the game optimally or super-human like. Consequently, the participants are expected to work on a playtesting agent from which one can determine how difficult the level will be if played by a human.

The agentes developed will be evaluated on a number of held-out levels which will include both levels similar to the ones used for training, and some levels containing unique combinations of mechanics. The winner will be the one that achieves the lowest mean relative error in completion rate on the evaluation levels.



## Getting started

The simulator is headless build of the actual game, meaning the game logic and levels are exactly as in the live game. If you are not familiar with these types of games, visit the [Game Info](gameinfo) page for an overview of the game rules and logic. To see how we represent the live game with the simulator, visit the [Game Environment](environment) page.

To get started accessing the game simulator, visit the [Getting Started](setup) page to find help on getting up and running.


## Levels and data

For the purpose of this competition, the provided simulator is able to simulate 110 levels. In addition to this, we also provide the player move limit and completion rate.

An overview of the levels along with the data can be found on the [Levels](levels) page.


## Evaluation

As mentioned, the agents will be evaluated on a number of held-out levels. To do this, we let the agent play through these levels 2000 times each and note down the number of valid steps taken to complete these levels. The agent completion rate is then simply calculated as the number of runs that finished within the given move limit of the level.

The winner will be the contestant(s) that achieves the lowest mean relative difference between the agent and player completion rates.
