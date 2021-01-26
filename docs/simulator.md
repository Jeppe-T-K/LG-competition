# LG Simulator

When referring to the simulator, we mean the Unity build of the game that you are able to interact with using http requests.

# Setup

## Docker
The easiest way to get started is to use Docker and fetch the simulator image.

To to this, bla bla

## Linux binary



# Interacting with the simulator

## HTTP API

All endpoints, except `ping` should be called using the HTTP POST method.

### Ping

* URL: `/ping`
* Input: N/A
* Output: `Pong`

### Load level

* URL: `/load`
* Input: `levelIndex:int`, `seed:int`
* Output: `state:string`, `multichannelArrayState:string`

### Click piece

* URL: `/click`
* Input: `state:string`, `x:int`, `y:int`
* Output: `clickSuccessful:bool`, `simulationResult:string`, `state:string`

### Session create

* URL: `/session/create`
* Input: `state:string`, `returnFullState:bool`
* Output: `sessionId:string`, `fullState:string`, `multichannelArrayState:string`

### Session click

* URL: `/session/click`
* Input: `sessionId:string`, `returnFullState:bool`, `x:int`, `y:int`
* Output: `clickSuccessful:bool`, `simulationResult:string`, `fullState:string`, `multichannelArrayState:string`

### Session status

* URL: `/session/status`
* Input: `sessionId:string`
* Output: `state:string`, `stateSparse:string`

### Session destroy

* URL: `/session/destroy`
* Input: `sessionId:string`
* Output: `destroyed:book`

### Sessions list

* URL: `/sessions/list`
* Input: N/A
* Output: `sessionIds:array<string>`

### Sessions clear

* URL: `/sessions/clear`
* Input: N/A
* Output: `sessionIds:array<string>` (always empty)
