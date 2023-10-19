rooms = {
    "the_plane": {
        "enter": """You just arrived for your internship, but now Dr Plimph wants you to come to Siberia. You stand at the bottom of stairs to board as you see the last of the team disappearing inside.""",
        "exit": """But we just got here! fine""",
        "automate": "go up",
        "directions": {
            "UP": {
                "desc": "You've come this far, surely you have to GO UP the stairs?", 
                "room": "the_cave"
            },
        }

    },
    "the_cave": {
        "enter": "You hurried from the airport and stopped suddenly on a small road. You can see the uncovered cave door",
    },
    "the_entrance": {
        "enter": "'Touch nothing!' shouts Dr. Plimph, as he hurries down the darkened hall. You stay behind, nervously wondering if you should follow.",
    },
    "the_pit": {
        "enter": "You slide to a halt covered in dust.",
        "exit": None,
        "desc": "A dark room with stone walls and floor",
        "directions": {
            "N": {"desc": "a glowing door", "room": "the_end"},
        }
    },
    "the_end": {
        "desc": "A sunny balcony with stairs down to your car",
        "enter": "The sun shines brightly here, everything is going to be ok",
    },
    "pit_hole": {
        "desc": "A deep dark hole",
        "enter": "You fall forever",
    }
}
current_room = rooms["the_plane"]

def get_room_name(room):
    for k, v in rooms.rooms.items():
        if v == room:
            return k
    raise Exception("unknown room " + repr(room)) 


