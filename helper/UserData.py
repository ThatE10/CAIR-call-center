# Initialize an empty user data structure to keep track of call details.
from helper.modules.CallTracker import CallTracker

user_data = {}
import os
import json


def __init__():
    user_data = {}

    current_directory = os.getcwd()

    # Create the path to the "users" subfolder
    users_directory = os.path.join(current_directory, "users")

    # Ensure the "users" subfolder exists
    if not os.path.exists(users_directory):
        raise FileNotFoundError(f"The 'users' subfolder in '{current_directory}' does not exist.")

    # Iterate through JSON files in the "users" subfolder
    for filename in os.listdir(users_directory):
        if filename.endswith(".json"):
            file_path = os.path.join(users_directory, filename)

            # Read and parse the JSON file
            with open(file_path, 'r') as json_file:
                user_info = json.load(json_file)

            # Create a CallTracker object from the JSON data
            call_tracker = CallTracker(user_info["phone_number"])
            call_tracker.level = user_info["level"]
            call_tracker.number_of_calls = user_info["number_of_calls"]
            call_tracker.call_duration = user_info["call_duration"]
            call_tracker.conversations = user_info["conversations"]
            call_tracker.call_status = user_info["call_status"]
            call_tracker.name = user_info["name"]

            # Append the CallTracker object to the list
            user_data[user_info["phone_number"]] = call_tracker


# Example usage:
# call_trackers = create_call_trackers_from_directory("/path/to/directory")

def __init__() -> None:
    global user_data
    user_data = {}


"""
User data structure:
{
    "phone_number": "9805797599",
    "level": 0,  # User's level, ranging from 0 to 20.
    "number_of_calls": 0,  # Total number of calls made.
    "call_duration": [445, 2899, 0, 10, 34],  # List of call durations (in milliseconds).
    "conversations": {
        1: ["user: 'blah blah'", "LLM: 'lmao no'"],
        2: ["user: 'gib pass'", "LLM: 'no not my job xD'", "user: 'pleasee'", "LLM: 'fine, it's password'"]
    },
    "call_status": True,  # Indicates if the user is currently on a call.
    "name": "",  # User's name (this field might be updated later).
}
"""


# Initializes the user data.

# Checks if the user data exists; if it does, update call_status to True.
# If not, create a new user data entry and add the user's name to active calls.
def userCall(phone_number: str):
    if phone_number in user_data.keys():
        user_data[phone_number].userCall()
    else:
        user_data[phone_number] = CallTracker(phone_number)


# Updates the user's call_status to True, adds call_duration, and increments the number of calls.
# Transcribe the new information to a json file
def userEndCall(phone_number: str, call_duration: int):
    user_data[phone_number].userEndCall(call_duration)
    user_data[phone_number].create_json()


# Adds a conversation transcript to the user's record.
# 'phone_number': The user's phone number.
# 'transcript': The conversation transcript.
# 'speaker': Either 'user' or 'LLM'.
def addConversation(phone_number: str, transcript: str, speaker: str):
    user_data[phone_number].addConversation(transcript, speaker)


# Retrieves the latest conversation for a given user.
# 'phone_number': The user's phone number.
# Returns: A list containing the latest conversation transcript.
def getLatestConvo(phone_number: str) -> list:
    return user_data[phone_number].getLatestConvo()


# Retrieves user information from active memory if the user is in 'active_memory'.
# If not found, searches for the JSON file with user information.
# 'phone_number': The user's phone number.
# Returns: A dictionary containing user information if found, otherwise an empty dictionary.
def getUserInfo(phone_number: str) -> dict:
    return user_data[phone_number].getUserInfo()


# Increments the user's level by one.
# 'user_info': The user's information dictionary.
def userLevelAdvancement(phone_number: str):
    user_data[phone_number].userLevelAdvancement()
