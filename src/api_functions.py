"""This module contains functions for the Flask API."""
def get_average_temperature(temperatures):
    """Return the average temperature."""
    if len(temperatures) == 0:
        return 0
    return sum(map(float, temperatures)) / len(temperatures)


def calculate_status(average_temp):
    """Return the status of the temperature."""
    if average_temp < 10:
        return "Too cold"
    if 11 <= average_temp <= 36:
        return "Good"
    return "Too hot"
