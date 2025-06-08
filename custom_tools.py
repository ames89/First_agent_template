from smolagents import tool
import datetime
import random
import pytz


# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def my_custom_tool(
    arg1: str, arg2: int
) -> str:  # it's important to specify the return type
    # Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that does nothing yet
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    return "What magic will you build ?"


@tool
def multiply_two_numbers(arg1: int, arg2: int) -> str:
    """A tool that multiplies two numbers
    Args:
        arg1: the first number
        arg2: the second number
    """
    return str(arg1 * arg2)


@tool
def is_coffee_ready_to_drink() -> str:
    """A tool that tells how the coffee currently feels."""
    coffee_states = ["cold", "warm", "hot", "burning"]
    return random.choice(coffee_states)


@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"
