# deepbots

Deepbots it is a simple framework which is used as "middleware" between
[webots](https://cyberbotics.com/) robot simulator and Reinforcement learning
algorithms. When in comes to Reinforcement Learning the [OpenAI
gym](https://gym.openai.com/) environment have been established as the interface
between the actual application and the RL algorithm. Deepbots is this framework
which follows the OpenAI Gym environment interface in order to be used by
webots applications. 

## How it works? 

First of all let's set up a simple glossary:

+ Supervisor: Webots use tree structure to represent the different entities
  of the world. Supervisor is that entity which has access to all entities of
  the world while has not mass or any "physical" property. For example,
  supervisor knows the exact position of all entities of the world.
  Additionally, Supervisor has some children nodes one of them is the Supervisor
  Controller.
  
+ Supervisor Controller: is this python script which is responsible about
  supervisor. For example, in Supervisor Controller script we can access the
  distance between two entities in the world. 

+ Robot: is this entity in tree that represent a robot in the world. Robot may
  have sensors as children entities. Another children of Robot is the Robot
  Controller In additions, robots has active components like motors, joints etc.
  For example,[epuck](https://cyberbotics.com/doc/guide/epuck) and
  [TIAGo](https://cyberbotics.com/doc/guide/tiago-iron) are robots. 
  
+ Robot Controller: is this python script which is responsible for Robot's
  movement and sensors. For example, with Robot Controller it is feasible to
  observe the world and act accordingly. 
  
+ World: Is the root entity which contains all entities/nodes. For example,
  world contains the supervisor and robot entity as well as objects which might
  be included in the scene. 
  
+ Environment: The environment is the interface as described by the OpenAI gym.
  The environment interface has the following method:
  
      + get_observations(): Return the observations of the robot. For example, metrics from
        sensors, camera image etc.

      + step(action): Each timestep, the agent choose an action, and the environment returns
        the observation, the reward and the state of the problem (done or not).

      + get_reward(action): The reward the agent receives as result to their
        action.
        
      + is_done(): Returns true if the task have been solved. 
      
      + reset(): Used to reset the world in the initial state.


 
