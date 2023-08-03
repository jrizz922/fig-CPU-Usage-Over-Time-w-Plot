import matplotlib.pyplot as plt
import psutil

# Create an empty list to store CPU percentages
percentages = []

try:
    while True:
        # Get the current CPU usage as a percentage
        percentage = psutil.cpu_percent(interval=1)
        percentages.append(percentage)

        # Clear the console output
        print(chr(27) + '[2J')
        print('Current CPU usage: %s%%' % percentage)
        print('Press Ctrl+C to generate the graph.')

except KeyboardInterrupt:
    # The user pressed Ctrl+C, generate the graph
    plt.plot(percentages)
    plt.ylabel('CPU Usage (%)')
    plt.xlabel('Time (seconds)')
    plt.title('CPU Usage Over Time')
    plt.show()
