import matplotlib.pyplot as plt
import numpy as np

# Define data for the timeline
events = [
    ("CP/M 1.0 Released", "1974"),
    ("CP/M-86 Released", "1980"),
    ("MS-DOS Released", "1981"),
    ("Legacy of CP/M", "Influenced DOS, UNIX, etc.")
]

# Extract event names and years
event_names = [event[0] for event in events]
years = np.arange(len(event_names))

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(years, [0] * len(years), marker='o', markersize=8, linestyle='', color='blue')  # Timeline markers
plt.yticks([])  # Remove y-axis ticks
plt.xticks(years, event_names, rotation=45, ha='right', fontsize=10)  # Set x-axis ticks and labels
plt.title("Evolution of CP/M and its Impact on Computing History", fontsize=14)
plt.tight_layout()

# Annotate the years
for i, year in enumerate(events):
    plt.text(i, -0.05, year[1], ha='center', fontsize=9)

# Add a grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Remove the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust the plot limits for better visualization
plt.xlim(-0.5, len(years) - 0.5)


# Save the figure as a JPG image
plt.savefig('timeline.jpg', format='jpg')
