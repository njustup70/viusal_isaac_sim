"""
This is the implementation of the OGN node defined in OgnSteeringControl.ogn
"""

# Array or tuple values are accessed as numpy arrays so you probably need this import
import numpy as np
import math

class OgnSteeringControl:
    """

    """
    @staticmethod
    def compute(db) -> bool:
        """Compute the outputs from the current input"""

        try:
            linear_x = db.inputs.target_linear_x
            linear_y = db.inputs.target_linear_y
            angular_z = db.inputs.target_angular_z
            L = db.inputs.L  # Distance between front and back wheels
            W = db.inputs.W  # Distance between left and right wheels
            R = db.inputs.R  # Wheel radius
            min_move_speed = db.inputs.min_move_speed

            # Initialize outputs
            motor_angle = np.zeros(4)  # Motor angles [rad]
            motor_speed = np.zeros(4)  # Motor speeds [m/s]

            # Calculate velocities
            vel_total1 = math.sqrt((linear_x - angular_z * L / 2) ** 2 + (linear_y + angular_z * W / 2) ** 2)
            vel_total2 = math.sqrt((linear_x + angular_z * L / 2) ** 2 + (linear_y + angular_z * W / 2) ** 2)

            if vel_total1 > min_move_speed or vel_total2 > min_move_speed:
                motor_angle[0] = math.atan2(linear_y + angular_z * W / 2, linear_x - angular_z * L / 2)
                motor_angle[1] = math.atan2(linear_y + angular_z * W / 2, linear_x + angular_z * L / 2)
                motor_angle[2] = math.atan2(linear_y - angular_z * W / 2, linear_x - angular_z * L / 2)
                motor_angle[3] = math.atan2(linear_y - angular_z * W / 2, linear_x + angular_z * L / 2)

            motor_speed[0] = vel_total1 / (R * 2 * math.pi)
            motor_speed[1] = vel_total2 / (R * 2 * math.pi)
            motor_speed[2] = vel_total1 / (R * 2 * math.pi)
            motor_speed[3] = vel_total2 / (R * 2 * math.pi)

            # Set outputs
            db.outputs.motor_angle_target = motor_angle
            db.outputs.motor_speed_target = motor_speed

            return True
           
        except Exception as error:
            # If anything causes your compute to fail report the error and return False
            db.log_error(str(error))
            return False

        # Even if inputs were edge cases like empty arrays, correct outputs mean success
        return True
