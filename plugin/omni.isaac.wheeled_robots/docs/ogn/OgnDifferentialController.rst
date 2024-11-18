.. _omni_isaac_wheeled_robots_DifferentialController_1:

.. _omni_isaac_wheeled_robots_DifferentialController:

.. ================================================================================
.. THIS PAGE IS AUTO-GENERATED. DO NOT MANUALLY EDIT.
.. ================================================================================

:orphan:

.. meta::
    :title: Differential Controller
    :keywords: lang-en omnigraph node isaacSim wheeled_robots differential-controller


Differential Controller
=======================

.. <description>

Differential Controller

.. </description>


Installation
------------

To use this node enable :ref:`omni.isaac.wheeled_robots<ext_omni_isaac_wheeled_robots>` in the Extension Manager.


Inputs
------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Desired Angular Velocity (*inputs:angularVelocity*)", "``double``", "desired rotation velocity", "0.0"
    "Dt (*inputs:dt*)", "``double``", "delta time", "0.0"
    "Exec In (*inputs:execIn*)", "``execution``", "The input execution", "None"
    "Desired Linear Velocity (*inputs:linearVelocity*)", "``double``", "desired linear velocity", "0.0"
    "Max Acceleration (*inputs:maxAcceleration*)", "``double``", "maximum linear acceleration of the robot for forward and reverse, 0.0 means not set", "0.0"
    "Max Angular Acceleration (*inputs:maxAngularAcceleration*)", "``double``", "maximum angular acceleration of the robot, 0.0 means not set", "0.0"
    "Max Angular Speed (*inputs:maxAngularSpeed*)", "``double``", "max angular speed allowed for vehicle, 0.0 means not set", "0.0"
    "Max Deceleration (*inputs:maxDeceleration*)", "``double``", "maximum linear braking of the robot, 0.0 means not set.", "0.0"
    "Max Linear Speed (*inputs:maxLinearSpeed*)", "``double``", "max linear speed allowed for vehicle, 0.0 means not set", "0.0"
    "Max Wheel Speed (*inputs:maxWheelSpeed*)", "``double``", "max wheel speed allowed, 0.0 means not set", "0.0"
    "Wheel Distance (*inputs:wheelDistance*)", "``double``", "distance between the two wheels", "0.0"
    "Wheel Radius (*inputs:wheelRadius*)", "``double``", "radius of the wheels", "0.0"


Outputs
-------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Velocity Command (*outputs:velocityCommand*)", "``double[]``", "velocity commands", "[0.0, 0.0]"


Metadata
--------
.. csv-table::
    :header: "Name", "Value"
    :widths: 30,70

    "Unique ID", "omni.isaac.wheeled_robots.DifferentialController"
    "Version", "1"
    "Extension", "omni.isaac.wheeled_robots"
    "Icon", "ogn/icons/omni.isaac.wheeled_robots.DifferentialController.svg"
    "Has State?", "False"
    "Implementation Language", "C++"
    "Default Memory Type", "cpu"
    "Generated Code Exclusions", "None"
    "uiName", "Differential Controller"
    "Categories", "isaacSim"
    "__categoryDescriptions", "isaacSim,robot controller inside Isaac Sim"
    "Generated Class Name", "OgnDifferentialControllerDatabase"
    "Python Module", "omni.isaac.wheeled_robots"

