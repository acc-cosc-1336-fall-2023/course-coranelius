ratio = 0

def get_options_ratio(option, total):
    if total == 0:
        return "Total can not be zero."
    else:
        ratio = option / total
        return ratio
    
def get_faculty_rating(ratio):
    if (ratio <= 1 and ratio >= .9):
        return 'Excellent'
    if (ratio < .9 and ratio >= .8):
        return 'Very good'
    if (ratio < .8 and ratio >= .7):
        return 'Good'
    if (ratio < .7 and ratio >= .6):
        return 'Needs Improvement'
    if(ratio < .6 and ratio >= 0):
        return 'Unacceptable'