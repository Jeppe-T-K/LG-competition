---
layout: home
title: Lily's Garden Completion Rate Prediction
subtitle: About the competition
---

Lily's Garden is a collapse-style puzzle game. For this game we are able to completely decouple the logic from the graphics and just execute the game board simulation without any graphics. We have exploited this by creating a special Linux build of Lily's Garden where the game runs a simple HTTP web server that allows an external agent to interface with the game by performing HTTP requests against the game.

We have written a OpenAI Gym based environment in Python that communicates with the simulator and we have then written an agent that uses the Lily's Garden Gym environment.

### Rules

The purpose ....
* Bla bla
