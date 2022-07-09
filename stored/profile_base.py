

class ProfileBase:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

        # Recognizable features of the person: User will have to identify 2/4 ways presented below in person
        # Discord authenticates only with pass phrase, and voice if needed
        self.image = None
        self.voice = None
        self.pass_phrase = ""   # used if bot cannot double authenticate person on its own
        self.hard_token = ""    # Encrypted key that is contained in a hard token the user can provide for auth

        '''Used to contain all the admin rights a certain user can use the bot for. Prevents simply anyone from simply
        asking the bot to do things. Bot will refuse service to anyone else'''
        self.rights = {
            "info_check": True,
            "shutdown_command": True,
            "automation_command": False,
            "movement_command": False
        }

        # Discord information
        self.username = ""

        # Emotional values with the person
        self.outward_view = 0
        self.inward_view = 0

        # Personality type to display (future update)
        self.personality_preference = None  # personality class ie serious, funny, etc.

