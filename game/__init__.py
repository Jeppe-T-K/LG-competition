from gym.envs.registration import register
# from game.lilys_garden_env import LilysGardenEnv

register(
    id='lg-competition-v0',
    entry_point='game.lilys_garden_env:LilysGardenEnv'
)