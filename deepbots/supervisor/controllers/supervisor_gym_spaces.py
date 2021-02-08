from gym import spaces

from .supervisor_emitter_receiver import SupervisorEmitterReceiver
from .supervisor_env import SupervisorEnv


class SupervisorGymSpaces(SupervisorEnv):
    def __init__(self,
                 action_space: spaces.Space,
                 observation_space: spaces.Space,
                 time_step=None):
        super().__init__()

        self.action_space = action_space
        self.observation_space = observation_space


class SupervisorGymSpacesEmitterReceiver(SupervisorEmitterReceiver):
    def __init__(self,
                 action_space: spaces.Space,
                 observation_space: spaces.Space,
                 emitter_name="emitter",
                 receiver_name="receiver",
                 time_step=None):

        super().__init__(emitter_name, receiver_name)

        self.action_space = action_space
        self.observation_space = observation_space

    def hande_emitter(self, action: spaces.Space):
        self.emitter.send(self.action_space.to_jsonable(action))

    def handle_receiver(self):
        if self.receiver.getQueueLength() > 0:
            string_message = self.receiver.getData().decode("utf-8")
            self.receiver.nextPacket()
            return self.observation_space.from_jsonable(string_message)
        else:
            return None
