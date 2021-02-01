---
layout: page
title: Setting it up
subtitle: Using Docker and Python
---

# Overview

There are two things required to interact with the game: Docker and Python3.6

This implementation has decoupled the logic from the graphics and just execute the game board simulation without any graphics. Specifically, we use a special Linux build of Lily’s Garden where the game runs a simple HTTP web server that allows an external agent to interface with the game by performing HTTP requests against the game.
To ensure compatibility between platforms, we use Docker to run this webserver in its own container.

To interact with the server, we have created an OpenAI Gym based environment in Python that communicates with the simulator.
This serves the purpose of interpreting and formatting the response from the simulator to make it compatible with common playtest algorithms.

# Simulator setup

To begin with, make sure you have Docker installed. To find instructions on how to install it, follow the instructions on [docker.com](https://www.docker.com/).

#### Pulling simulator image

Once Docker is installed, pull the `lg-simulator-competition` image from the public Docker repository:

```
docker pull jeppetk/lg-competition
```

#### Run
Run the container in the background:

```
docker run -p 8090:8080 -dt --name lg-simulator  jeppetk/lg-competition
```

#### Test
Test that the simulator server is running by visiting the following URL:

```
curl http://localhost:8090/ping
```

If it works, you should get the response `Pong`.

You should now be ready to interact with the simulator using the commands outlined on the [simulator page](simulator) or use the pre-made [OpenAI Gym environment](environment).


# Python setup

Python >3.6 is required to run the python-part of the code. We recommend using Anaconda, [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) or similar tools to manage which Python interpreter to use.

Below are instructions on how to get set up with [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

### With virtualenv

#### Clone LG-competition

First get the LG-competetion files from Github:

```
git clone https://github.com/Jeppe-T-K/LG-competition.git
cd LG-competition
```

#### Installing python packages

Next make sure you are in the correct directory and set up the virtual environment:

```
virtualenv --python=python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Test
To test whether everything works as expected, you can try to run the example with the random agent.

First make sure the simulator is running in the background. If so, run:

```
python -m examples.random_agent
```

If successful, you should see something similar to the following printed in the console:

```
Shape of observations: (13, 9, 17)
Chosen action: 24
Reward: -0.6, finished level: False, additional info: {'valid_steps': 0, 'total_steps': 1, 'successful_click': False, 'new_progress': 45, 'goal_reached': False}
Final reward: 24.799999999999976
{'valid_steps': 18, 'total_steps': 57, 'successful_click': True, 'new_progress': 0, 'goal_reached': True}
Level 2 final reward: 6.900000000000006
{'valid_steps': 21, 'total_steps': 81, 'successful_click': True, 'new_progress': 0, 'goal_reached': True}
```


# Typical errors

## Connection errors
A common error is a connection error. The Python error message looks something like this:

```
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=8090):
Max retries exceeded with url: /load (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f934855c278>:
Failed to establish a new connection: [Errno 61] Connection refused',))
```

If that is the case, verify that the simulator is running and open to the correct port (here 8090).

```
docker ps
```

should give something like this:

```
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS         PORTS                    NAMES
0497d9ba2b90   lg-simulator   "/bin/sh -c ./linux.…"   3 months ago   Up 4 minutes   0.0.0.0:8090->8080/tcp   lg-simulator-local
```
