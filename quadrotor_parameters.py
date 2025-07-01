import numpy as np
# Physical parameters
g = 9.8 # Gravitational acceleration (m/s^2)
m = 5.8  # Quadrotor mass (kg)
d = 0.6  # length of the rotors' arm (distance from center to motor) (m)

# Quadrotor moments of inertia
Ixx = 0.327
Iyy = 0.327
Izz = 0.654

gamma = 0.05  # Propulor thrust/torque constant 

 # Constraints 
max_thrust = 30.0  # Max thrust for each motor (N)
min_thrust = 0.0   # Min thrust (N)
min_z = -30
max_z = 0
max_h_pos = 200
max_phi_theta = np.pi / 3
max_psi = np.pi

parameters = {
    "g" : g,
    "m" : m,
    "d" : d,
    "Ixx" : Ixx,
    "Iyy" : Iyy,
    "Izz" : Izz,
    "gamma" : gamma,
    "max_thrust" : max_thrust,
    "min_thrust" : min_thrust, 
    "min_z" : min_z,
    "max_z" : max_z, 
    "max_h_pos" : max_h_pos, 
    "max_phi_theta" : max_phi_theta,
    "max_psi" : max_psi
}

