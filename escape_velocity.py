import time


# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
escape_velocity = 11200  # Escape velocity (m/s)

rocket_art = """
        ^
       / \\
      / _ \\
     | (_) |
     |  _  |
    /|     |\\
   / |     | \\
  /__|     |__\\
     |  |  |
     |  |  |
     |  |  |
    /    |   \\
   |     |    |
   |_____|____|
     (  ) (  )
      ( )   ( )
"""

def calculate_forces(mass, time_to_escape):
    # Calculate gravitational force
    gravitational_force = mass * g

    # Calculate required acceleration to reach escape velocity
    acceleration = escape_velocity / time_to_escape

    # Calculate force needed for acceleration
    force_for_acceleration = mass * acceleration

    # Calculate total force needed
    total_force = gravitational_force + force_for_acceleration

    return gravitational_force, acceleration, force_for_acceleration, total_force

def main():
    # Show rocket art
    print(rocket_art)
    time.sleep(2)
    print("Welcome to the Rocket Launch Simulation!")
    time.sleep(1)
    
    # User input
    mass = float(input("Enter the mass of the rocket (kg): "))
    time.sleep(1)
    time_to_escape = float(input("Enter the time to reach escape velocity (s): "))
    time.sleep(3)

    # Calculate forces
    gravitational_force, acceleration, force_for_acceleration, total_force = calculate_forces(mass, time_to_escape)

    # Output results
    print("\n*** LIFTOFF! ***\n")
    print(f"Results for a rocket with mass {mass} kg:")
    print(f"Gravitational Force: {gravitational_force:.2f} N")
    print(f"Required Acceleration: {acceleration:.2f} m/s^2")
    print(f"Force Needed for Acceleration: {force_for_acceleration:.2f} N")
    print(f"Total Force Required to Escape Earth's Gravity: {total_force:.2f} N")
    print("\nThe rocket is blasting off!\n")
    time.sleep(3)
    
    # Rocket launch animation
    for i in range(5, 0, -1):
        print(f"T-minus {i}...")
        time.sleep(1)
    
    print(rocket_art)
    time.sleep(2)
    print("🚀 Rocket has launched into space!")

if __name__ == "__main__":
    main()
