import json

def set_debug(value: bool):
    global debug
    debug = value

# def load_settings():  
    # implement laterº
    
def load_debug_settings():
    global settings
    with open('doc_viewer/settings/debug_settings.json', 'r') as f:
        settings = json.load(f)