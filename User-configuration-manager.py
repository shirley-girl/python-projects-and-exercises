# User Configuration  Manager 
"""
Allows users to manage their settings such as theme, language and notifications
functions to be implemented: add, update,delete and view users settings
"""
test_settings ={
    "theme" : "dark",
    "volume" : "high"
}

def add_setting(settings, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
   
    

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
        

print(add_setting(test_settings,("theme", "dark")))

print(add_setting(test_settings,("language", "English")))

def update_setting(settings:dict, key_value : tuple):
    key , value = key_value
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    
print(update_setting(test_settings,("volume","low")))
print(update_setting(test_settings,("notification","enabled")))

def delete_setting(settings, key):
    
    key = key.lower()
   
    if key in settings:
        del settings[key] 
        return f"Setting '{key}' deleted successfully!"

    else:
        return f"Setting not found!"

print(delete_setting(test_settings, 'language'))

print(delete_setting(test_settings, 'font'))

def view_settings(settings):
    
    if settings == { }:
        return "No settings available."
    
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():

            result += f"{key.capitalize()}: {value}\n"
        return result
        
print(view_settings(test_settings))

    

