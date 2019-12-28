# deepbots

Deepbots is a simple framework which is used as "middleware" between the
[Webots](https://cyberbotics.com/) robot simulator and Reinforcement Learning
algorithms. When in comes to Reinforcement Learning the [OpenAI
gym](https://gym.openai.com/) environment has been established as the most used 
interface between the actual application and the RL algorithm. Deepbots is a 
framework which follows the OpenAI gym environment interface in order to be 
used by Webots applications. 

## How it works? 

First of all let's set up a simple glossary:

+ World: Webots uses a tree structure to represent the different entities
  in the scene. The World is the root entity which contains all the entities/nodes. 
  For example, the world contains the Supervisor and Robot entities as well as 
  other objects which might be included in the scene. 
  
+ Supervisor: The Supervisor is an entity which has access to all other entities
  of the world, while having no physical presence in it. For example,
  the Supervisor knows the exact position of all the entities of the world and
  can manipulate them. Additionally, the Supervisor has the Supervisor 
  Controller as one of its child nodes.
  
+ Supervisor Controller: The Supervisor Controller is a python script which is 
  responsible for the Supervisor. For example, in the Supervisor Controller 
  script the distance between two entities in the world can be calculated. 

+ Robot: The Robot is an entity that represents a robot in the world. 
  It might have sensors and other active components, like motors, etc. 
  as child entities. Also, one of its children is the Robot Controller.
  For example, [epuck](https://cyberbotics.com/doc/guide/epuck) and
  [TIAGo](https://cyberbotics.com/doc/guide/tiago-iron) are robots.
  
+ Robot Controller: The Robot Controller is a python script which is responsible 
  for the Robot's movement and sensors. With the Robot Controller 
  it is possible to observe the world and act accordingly. 
  
+ Environment: The Environment is the interface as described by the OpenAI gym.
  The Environment interface has the following methods:
  
      + get_observations(): Return the observations of the robot. For example, metrics from
        sensors, a camera image etc.

      + step(action): Each timestep, the agent chooses an action, and the environment returns
        the observation, the reward and the state of the problem (done or not).

      + get_reward(action): The reward the agent receives as result of their
        action.
        
      + is_done(): Returns true if the task has been solved. 
      
      + reset(): Used to reset the world to the initial state.


 
