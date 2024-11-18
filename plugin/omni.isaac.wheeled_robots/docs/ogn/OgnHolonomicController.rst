.. _omni_isaac_wheeled_robots_HolonomicController_2:

.. _omni_isaac_wheeled_robots_HolonomicController:

.. ================================================================================
.. THIS PAGE IS AUTO-GENERATED. DO NOT MANUALLY EDIT.
.. ================================================================================

:orphan:

.. meta::
    :title: Holonomic Controller
    :keywords: lang-en omnigraph node isaacSim wheeled_robots holonomic-controller


Holonomic Controller
====================

.. <description>

Holonomic Controller

.. </description>


Installation
------------

To use this node enable :ref:`omni.isaac.wheeled_robots<ext_omni_isaac_wheeled_robots>` in the Extension Manager.


Inputs
------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Angular Gain (*inputs:angularGain*)", "``double``", "angular gain", "1"
    "Exec In (*inputs:execIn*)", "``execution``", "The input execution", "None"
    "Velocity Commands for the vehicle (*inputs:inputVelocity*)", "``double[3]``", "velocity in x and y and rotation", "[0.0, 0.0, 0.0]"
    "Linear Gain (*inputs:linearGain*)", "``double``", "linear gain", "1"
    "Max Angular Speed (*inputs:maxAngularSpeed*)", "``double``", "maximum angular rotation speed allowed for the vehicle", "100000"
    "Max Linear Speed (*inputs:maxLinearSpeed*)", "``double``", "maximum speed allowed for the vehicle", "100000"
    "Max Wheel Speed (*inputs:maxWheelSpeed*)", "``double``", "maximum rotation speed allowed for the wheel joints", "100000"
    "Mecanum Angles (*inputs:mecanumAngles*)", "``double[]``", "angles of the mecanum wheels with respect to wheel's rotation axis", "[]"
    "Up Axis (*inputs:upAxis*)", "``double[3]``", "the rotation axis of the vehicle", "[0.0, 0.0, 1.0]"
    "Wheel Axis (*inputs:wheelAxis*)", "``double[3]``", "the rotation axis of the wheels", "[1.0, 0.0, 0.0]"
    "Wheel Orientations (*inputs:wheelOrientations*)", "``double[4][]``", "orientation of the wheel with respect to chassis' center of mass frame ", "[]"
    "Wheel Positions (*inputs:wheelPositions*)", "``double[3][]``", "position of the wheel with respect to chassis' center of mass", "[]"
    "Wheel Radius (*inputs:wheelRadius*)", "``double[]``", "an array of wheel radius", "[]"


Outputs
-------
.. csv-table::
    :header: "Name", "Type", "Descripton", "Default"
    :widths: 20, 20, 50, 10

    "Joint Velocity Command (*outputs:jointVelocityCommand*)", "``double[]``", "velocity commands for the wheels joints", "None"


Metadata
--------
.. csv-table::
    :header: "Name", "Value"
    :widths: 30,70

    "Unique ID", "omni.isaac.wheeled_robots.HolonomicController"
    "Version", "2"
    "Extension", "omni.isaac.wheeled_robots"
    "Has State?", "False"
    "Implementation Language", "Python"
    "Default Memory Type", "cpu"
    "Generated Code Exclusions", "None"
    "uiName", "Holonomic Controller"
    "Categories", "isaacSim"
    "__categoryDescriptions", "isaacSim,robot controller inside Isaac Sim"
    "Generated Class Name", "OgnHolonomicControllerDatabase"
    "Python Module", "omni.isaac.wheeled_robots"

