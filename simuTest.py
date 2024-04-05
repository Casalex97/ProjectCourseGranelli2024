import numpy as np
import matplotlib.pyplot as plt

c = 3e8

def distance(p1, p2):
    
    # euclidean distance
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def path_loss(distance, wall_thickness, freq):
    
    wavelength = c / freq
    free_space_loss = (4 * np.pi * distance / wavelength)**2
    penetration_loss = np.exp(-2 * wall_thickness * np.sqrt(np.pi * freq / c)) 
    return penetration_loss * free_space_loss

def main():
    # input coordinates
    tx_position = (0, 1, 0)
    rx_position = (100, 1, 0)
    obstacle_position = (70, 2, 2)  # (x, y, z)
 
    freq = 28e9 # 28 GHz transmitter frequency
    #power_tx = 10 # dBm
    #noise_power = 2 # dBm
    wall = 1 # 1m 

    #time = np.linspace(0, 10, 1000)  # Time range for simulation
    # Generate the example signal
    #signal_frequency = 1e6  # Frequency of the sinusoidal signal (1 MHz)
    #signal_amplitude = 1.0  # Amplitude of the signal
    #signal = signal_amplitude * np.sin(2 * np.pi * freq * time)

    tx_rx_distance = distance(tx_position, rx_position)
    tx_obstacle_distance = distance(tx_position, obstacle_position)
    obstacle_rx_distance = distance(obstacle_position, rx_position)

    path_loss_tx_obstacle = path_loss(tx_obstacle_distance, wall, freq)
    path_loss_obstacle_rx = path_loss(obstacle_rx_distance, wall, freq)
    total_path_loss = path_loss_tx_obstacle + path_loss_obstacle_rx


    SNR = 10 * np.log10(1/path_loss_tx_obstacle + 1/path_loss_obstacle_rx) # SNR in dB

    reflection_coefficient = 0.25 # example reflection coefficient of the obstacle
    reflected_power = reflection_coefficient * path_loss_tx_obstacle

    # Calculate received rx power
    #power_rx = power_tx - path_loss_tx_obstacle - path_loss_obstacle_rx # - reflected_power
    #total_received_power = path_loss_obstacle_rx + reflected_power

    print("Transmitter to receiver distance: ", "%.2f" % tx_rx_distance, "m")
    print("Transmitter to obstacle distance: ", "%.2f" % tx_obstacle_distance, "m")
    print("Obstacle to receiver distance:", "%.2f" % obstacle_rx_distance, "m")
    print("Signal to Noise Ratio:", "%.2f" % SNR, "dB\n")
    print("Path Loss transmitter to obstacle:", path_loss_tx_obstacle, "dB")
    print("Path Loss obstacle to receiver:", path_loss_obstacle_rx, "dB")
    print("Total path loss:", total_path_loss, "dB")
    print("Reflected signal power:", reflected_power, "dB")
    #print("Total Received Signal Power:", total_received_power, "dB")
    #print("Received Signal Power:", power_rx, "dB")

if __name__ == "__main__":
    main()
