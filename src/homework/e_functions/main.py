from value_return import get_hour
from value_return import get_minutes
from value_return import get_seconds


epoch_seconds = 3800

seconds = get_seconds(epoch_seconds)
minutes = get_minutes(epoch_seconds)
hours = get_hour(epoch_seconds)


time = f"{hours}:{minutes}:{seconds}"

print(time)