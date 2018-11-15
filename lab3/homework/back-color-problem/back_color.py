from random import *
from ex11and12_checkinside import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    color_list = []
    text_list = []
    for i in shapes:
        text_list.append(i['text'])
        color_list.append(i['color'])
    text = choice(text_list)
    color = choice(color_list)
    return [text,color,randint(0,1)]

def mouse_press(x, y, text, color, quiz_type):
    q = generate_quiz() 
    
    for j in shapes:
        if is_inside([x,y],j['rect']):
            if quiz_type == 0:
                if j['text'] == text:
                    return True
            elif quiz_type == 1:
                if j['color'] == color:
                    return True