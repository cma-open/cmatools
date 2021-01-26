

from cmatools.helloworld.hello_world import hello_world
from cmatools.observations.test import this_one


def combined():
    combined = f"{this_one()} {hello_world()}"
    return combined
