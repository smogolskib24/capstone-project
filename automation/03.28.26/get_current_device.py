def get_current_device():
    import json
    
    with open('current_device.json', 'r', encoding='utf-8') as f:
        current_device = json.load(f)

    return(current_device)
    