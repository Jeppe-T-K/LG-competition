import json
import numpy as np
import gym
from gym import spaces

from game.simulator import Simulator


class LilysGardenEnv(gym.Env):

    def __init__(self, level: int = 1, **kwargs):
        """The gym environment for Lily's Garden.
        Example of starting env: env = gym.make('lg-v0', level=1)


        Parameters
        ----------
        simulator: Simulator
            instance of Simulator

        Returns
        -------

        """
        self.simulator = None
        self.level = level
        self.board_state = None
        self.board_state_full = None
        self.return_full_state = False
        self.latest_observation = None
        self.current_progress = None
        self.max_total_steps = None
        self.valid_steps = 0
        self.total_steps = 0
        self.collect_goal_goal = 0
        self.sim_seed = None
        self.board_size = (13, 9)
        self.channels = 24  # 24 from sim + action mask from env

        self.observation_space = gym.spaces.Box(low=0,
                                                high=10.,
                                                shape=(self.board_size[0], self.board_size[1], self.channels),
                                                dtype=np.float32)
        self.action_space = spaces.Discrete(self.board_size[0] * self.board_size[1])
        self.valid_actions = [1] * self.action_space.n

        self.__dict__.update(kwargs)

    def reset(self, seed=None):

        self.valid_steps = 0
        self.total_steps = 0
        sim_seed = np.random.randint(1, 2 ** 31 - 1) if seed is None else seed
        self.sim_seed = sim_seed
        new_board = self.simulator.reset(self.get_level(), sim_seed)
        obs = new_board.get('multichannelArrayState', '{}')
        if obs:
            self.board_state = json.loads(obs)
        else:
            self.board_state = None
        self.latest_observation = self._observation_from_state()
        self.current_progress = self._calculate_progress()

        return self.latest_observation

    def step(self, action: int) -> any:
        coords = self._action_to_coord(action)

        result = self.simulator.step(coords['x'], coords['y'])
        self.board_state = json.loads(result.get('multichannelArrayState', '{}'))
        valid_action = result.get('clickSuccessful', False)
        new_progress = self._calculate_progress()

        observation = self._observation_from_state()
        self.latest_observation = observation
        self.valid_steps += 1 * valid_action
        goal_reached = self.board_state['collectGoalRemaining'] < 1e-6
        self.total_steps += 1
        info_dict = dict(valid_steps=self.valid_steps,
                         total_steps=self.total_steps,
                         successful_click=valid_action,
                         new_progress=new_progress)

        info_dict['goal_reached'] = goal_reached

        reward = self._calculate_reward(info_dict)

        # Should the env be reset?
        done = goal_reached
        self.current_progress = new_progress

        return observation, reward, done, info_dict

    def render(self, mode='human'):
        raise NotImplementedError

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def set_simulator(self, simulator: Simulator):
        self.simulator = simulator

    def _calculate_progress(self):
        try:
            progress = self.board_state['collectGoalGoal'] - self.board_state['collectGoalRemaining']
        except (TypeError, KeyError):
            progress = self.current_progress
        return progress

    def _calculate_reward(self, info_dict) -> float:
        reward = (self.current_progress - info_dict['new_progress']) - .1 - .5 * (not info_dict['successful_click'])
        reward += 5 * info_dict.get('goal_reached', False)
        return reward

    def _observation_from_state(self):
        try:
            obs = np.array(self.board_state['board'],
                           dtype=np.float64).reshape(self.board_state['boardSize'], order='F')
        except (TypeError, KeyError):
            obs = None

        return obs

    def _action_to_coord(self, action: int) -> dict:
        indexes = self._action_to_index(action)
        return {'x': int(indexes['idx'] - self.board_size[0] // 2), 'y': int(indexes['idy'] - self.board_size[1] // 2)}

    def _action_to_index(self, action: int) -> dict:
        return {'idx': action % self.board_size[0], 'idy': action // self.board_size[0]}

    def _coord_to_index(self, x: int, y: int) -> dict:
        return {'idx': int(x + self.board_size[0] // 2), 'idy': int(y + self.board_size[1] // 2)}

    def _coord_to_action(self, x: int, y: int) -> int:
        return self._index_to_action(**self._coord_to_index(x, y))

    def _index_to_action(self, idx: int, idy: int) -> int:
        return idx + idy * self.board_size[0]

    def _index_to_coord(self, idx: int, idy: int) -> dict:
        return {'x': idx - self.board_size[0] // 2, 'y': idy - self.board_size[1] // 2}
