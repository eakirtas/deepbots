from controller import Robot


class RobotEmitterReceiver:
    """
    This RobotEmitterReceiver implements only the most basic run method, that
    steps the robot and calls the handle_emitter, handle_receiver methods that
    are needed for communication with the supervisor.

    This class must be inherited by all robot controllers created by the user
    and the handle_emitter, handle_receiver, initialize_comms methods are all
    abstract and need to be implemented according to their docstrings. For a
    simpler RobotController that implements the methods in a basic form
    inherit the RobotEmitterReceiverCSV subclass or other emitter-receiver
    subclasses.
    """
    def __init__(self,
                 emitter_name="emitter",
                 receiver_name="receiver",
                 time_step=None):
        """
        The basic robot constructor.

        Initializes the Webots Robot and sets up a basic timestep if None is
        supplied.

        Also initializes the emitter and the receiver used to communicate with
        the supervisor, using the initialize_comms() method which must be
        implemented by the user. The two methods handle_emitter() and
        handle_receiver() are also implemented by the user.

        For the step argument see relevant Webots documentation:
        https://cyberbotics.com/doc/guide/controller-programming#the-step-and-wb_robot_step-functions

        :param time_step: int, positive or None
        """
        self.robot = Robot()

        if time_step is None:
            self.timestep = int(self.robot.getBasicTimeStep())
        else:
            self.timestep = time_step

        self.emitter, self.receiver = self.initialize_comms(
            emitter_name, receiver_name)

    def get_timestep(self):
        # TODO maybe remove this altogether and make self.timestep
        #  a pythonic class property. Print deprecation warning for
        #  next version?
        return self.timestep

    def initialize_comms(self, emitter_name, receiver_name):
        """
        This method should initialize and return the emitter and receiver in a
        tuple as expected by the constructor.

        A basic example implementation can be:

        emitter = self.robot.getEmitter("emitter")
        receiver = self.robot.getReceiver("receiver")
        receiver.enable(self.timestep)
        return emitter, receiver

        :return: (emitter, receiver) tuple, as initialized
        """
        raise NotImplementedError

    def handle_emitter(self):
        """
        This method should take data from the robot, eg. sensor data, parse
        it into a message and use the robot's emitter to send it to the
        supervisor. This message will be used as the observation of the robot.
        """
        raise NotImplementedError

    def handle_receiver(self):
        """
        This method should take data through the receiver in the form of a
        message and parse into data usable by the robot.

        For example the message might include a motor speed, which should be
        parsed and applied to the robot's motor.
        """
        raise NotImplementedError

    def run(self):
        """
        This method is required by Webots to update the robot in the
        simulation. It steps the robot and in each step it runs the two
        handler methods to use the emitter and receiver components.

        This method should be called by a robot manager to run the robot.
        """
        while self.robot.step(self.timestep) != -1:
            self.handle_receiver()
            self.handle_emitter()
