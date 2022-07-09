from stored.profile_base import ProfileBase



class Bot:
    name = "Jeff"
    hardware_installed = [["motherboard", "treads", "arm"]]
    items = ["water"]
    active_profile = None

    response_keywords ={
        "stock": "Yahoo",
        "emotion": "great",
        "name": name,
        "items": str(items),
        "active_profile": active_profile
    }





    # Use for testing profiles temporarily. Folder will be made to store JSON files of each person's information
    admin_profile = ProfileBase()
    admin_profile.first_name = "Morgan"
    admin_profile.last_name = "Carson"
    admin_profile.username = "mdcarson"

    profiles = [admin_profile]
