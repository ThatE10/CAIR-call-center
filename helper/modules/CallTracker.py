import json
import os

class CallTracker:
    def __init__(self, phone_number: str):
        # Initialize an empty user data structure to keep track of call details.
        self.phone_number = phone_number
        self.level = 0
        self.number_of_calls = 1
        self.call_duration = []
        self.conversations = {}
        self.call_status = True
        self.name = ""

    # Initializes the CallTracker instance.

    # Checks if the user data exists; if it does, update call_status to True.
    # If not, create a new user data entry and add the user's name to active calls.
    def userCall(self):
        self.number_of_calls += 1
        self.call_status = True

    # Updates the user's call_status to False, adds call_duration
    def userEndCall(self, call_duration: int):
        self.call_status = False
        self.call_duration.append(call_duration)

    # Adds a conversation transcript to the user's record.
    # 'transcript': The conversation transcript.
    # 'speaker': Either 'user' or 'LLM'.
    def addConversation(self, transcript: str, speaker: str):
        latest_convo_num = self.number_of_calls

        if latest_convo_num not in self.conversations:
            self.conversations[latest_convo_num] = []

        self.conversations[latest_convo_num].append(f"{speaker}: '{transcript}'")

    # Retrieves the latest conversation for a given user.
    # Returns: A list containing the latest conversation transcript.
    def getLatestConvo(self) -> list:
        latest_convo_num = self.number_of_calls
        return self.conversations[latest_convo_num]

    # Retrieves user information from active memory if the user is in 'active_memory'.
    # If not found, searches for the JSON file with user information.
    # Returns: A dictionary containing user information if found, otherwise an empty dictionary.
    def getUserInfo(self) -> dict:
        user_info = {
            "phone_number": self.phone_number,
            "level": self.level,
            "number_of_calls": self.number_of_calls,
            "call_duration": self.call_duration,
            "conversations": self.conversations,
            "call_status": self.call_status,
            "name": self.name,
        }
        return user_info

    # Increments the user's level by one.
    def userLevelAdvancement(self):
        self.level += 1

    import json
    import os

    def create_json(self, file_location, relative=True):
        # Ensure that the phone_number attribute exists
        if not hasattr(self, 'phone_number'):
            raise ValueError("The 'phone_number' attribute must be set before creating a JSON file.")

        # Get the phone number
        phone_number = self.phone_number

        # Determine the file path
        if relative:
            # If relative is True, treat file_location as a relative path
            file_path = os.path.join(file_location, f"{phone_number}.json")
        else:
            # If relative is False, use file_location as an absolute path
            file_path = file_location

        # Create a dictionary containing user information
        user_info = {
            "phone_number": phone_number,
            "level": self.level,
            "number_of_calls": self.number_of_calls,
            "call_duration": self.call_duration,
            "conversations": self.conversations,
            "call_status": self.call_status,
            "name": self.name,
        }

        # Write the user information to the JSON file and close the file
        with open(file_path, 'w') as json_file:
            json.dump(user_info, json_file, indent=4)
