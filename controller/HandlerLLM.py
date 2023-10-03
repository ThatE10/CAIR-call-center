import helper.CallUtil as call_data
import helper.UserData as user_data


from collections import deque

# this will be phone numbers of people who need to be called
people_to_process_queue = deque()


def __int__(self):
    pass


def AddConversationToProcess(self, str):
    # add the phone number to queue?
    pass


def RemoveConversationToProcess(self, str):
    # removes the phone number from the queue (optional) potentially stops processing the response.
    pass


    # You'll need to somehow process items in the queue maybe in a while loop? idk
    """
    You have to call controller.SpeechSynthesis.SynthesizeAudio(transcript, metaData)
    Update router.ManageCalls.LongWaitTimes when there is a long wait time
    """
