ev = '灩'

def calculations(behaviour, LOGS):
    if behaviour == ['Phished']:
        return "high"
    elif behaviour == ['Clicked']:
        return "moderate"
    else:
        return "low"