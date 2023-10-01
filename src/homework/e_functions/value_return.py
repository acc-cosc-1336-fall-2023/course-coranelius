
def get_hour(epoch_seconds):
    hours = (epoch_seconds // 3600) % 24
    if hours < 10:
        hours = "0" + str(hours)
    return hours
    

def get_minutes(epoch_seconds):
    minutes = (epoch_seconds // 60) % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    return minutes

def get_seconds(epoch_seconds):
    seconds = epoch_seconds % 60
    
    if seconds < 10:
        seconds = "0" + str(seconds)
    return seconds