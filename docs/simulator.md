---
layout: page
title: The Simulator
subtitle: Commands and options
---


# LG Simulator

When referring to the simulator, we mean the Unity build of the game that you are able to interact with using http requests.

`multichannelArrayState` contains all the relevant info of the current state in a flattened dictionary. The data consist of:
* `board`: Flattened vector of size `13*9*24`, following the formula `channelIndex * BOARD_WIDTH * BOARD_HEIGHT + xy[0]+xAdd + (xy[1]+yAdd) * BOARD_WIDTH`, where `xy = (index_x, index_y)` and `xAdd/yAdd > 0` if the piece is larger than 1x1
* `normList`: Suggested values to normalise board channels to be between 0 - 1. Note the values may exceed this interval in some levels, hence only a suggested list. 
* `collectGoalIdList`: List of individual collect goal ids. Note it does not inform about specific colors.
* `collectGoalGoalList`: List of individual collect goal objectives.
* `collectGoalRemaininglList`: List of individual collect goals remaining.
* `collectGoalGoal`: Sum of all collect goals objectives.
* `collectGoalRemaining`: Sum of all remaining collect goals.




## HTTP API

All endpoints, except `ping` should be called using the HTTP POST method.

### Ping

* URL: `/ping`
* Input: N/A
* Output: `Pong`

### Load level

Load a specfic level with a specific seed. Can be used to extract relevant features of the initial board state.

* URL: `/load`
* Input: `levelIndex:int`, `seed:int`
* Output: `state:string`, `multichannelArrayState:string`, `levelName:string`

### Click piece

This is not fully implemented.
* URL: `/click`
* Input: `state:string`, `x:int`, `y:int`
* Output: `clickSuccessful:bool`, `simulationResult:string`, `state:string`

### Session create

Creates a new playthrough of a specific level. This is the main function for playing the game since it keeps track of all the internal states.


* URL: `/session/create`
* Input: `returnFullState:bool`, `levelIndex:int`, `seed:int`
* Output: `sessionId:string`, `multichannelArrayState:string`, `levelName:string`, `levelMoveLimit:int`

### Session click

Method for taking an action in a current level session. Requires the `sessionId` created by the session/create API.

It is also possible to do a one-step look-ahead by using the `dryRun` flag.

* URL: `/session/click`
* Input: `sessionId:string`, `returnFullState:bool`, `x:int`, `y:int`, `dryRun:bool`
* Output: `clickSuccessful:bool`, `simulationResult:string`, `multichannelArrayState:string`, `fullState:string`

### Session status

* URL: `/session/status`
* Input: `sessionId:string`
* Output: `state:string`, `stateSparse:string`, `multichannelArrayState:string`

### Session destroy

* URL: `/session/destroy`
* Input: `sessionId:string`
* Output: `destroyed:bool`

### Sessions list

* URL: `/sessions/list`
* Input: N/A
* Output: `sessionIds:array<string>`

### Sessions clear

* URL: `/sessions/clear`
* Input: N/A
* Output: `sessionIds:array<string>` (always empty)
