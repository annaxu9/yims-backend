colleges = {
    "Benjamin Franklin": 'BF',
    "Berkeley": 'BK',
    "Branford": 'BR',
    "Davenport": 'DC',
    "Ezra Stiles": 'ES',
    "Grace Hopper": 'GH',
    "Jonathan Edwards": 'JE',
    "Morse": 'MC',
    "Pauli Murray": "MY",
    "Pierson": 'PC',
    "Saybrook": 'SY',
    "Silliman": 'SM',
    "Timothy Dwight": 'TD',
    "Trumbull": 'TC'
}

def get_college_id(college_name):
    keys = list(colleges.keys())
    return keys.index(college_name) + 1 if college_name in keys else None

