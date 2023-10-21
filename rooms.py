rooms = {
    "the_plane": {
        "enter": """Dr. Plimph just welcomed you to Cairo for your egyptology internship, your dream job!
But before you can unpack your bags he says that you're both going to Siberia to examine a mysterious cave covered in hieroglyphics.
At the plane stairs, you pause. Is this crazy?""",
        "exit": """We just got here, but why not?""",
        "automate": "go up",
        "directions": {
            "UP": {
                "desc": "stairs leading up to the plane where you see Dr. Plimph disappearing inside. Time to GO UP?",
                "room": "the_cave"
            },
        }

    },
    "the_cave": {
        "enter": "You hurried from the airport and stopped suddenly on a small road. To the North, you can see the uncovered cave door",
        "automate": "go north",
        "directions": {
            "N": {
                "desc": "Man that's scary, but this is your job right?",
                "room": "the_door"
            },
        }
    },
    "the_door": {
        "enter": """The gigantic door is covered in hieroglyphics. Oh, that must be why they needed Dr. Plimph!
He scans the text, starts laughing, and puts his finger in the belly-button of the small goblin in the corner.
The door slides upward with a loud crack!""",
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

# add the name to all the room objects
for name, room in rooms.items():
    room['name'] = name

def get_room_name(room):
    for k, v in rooms.rooms.items():
        if v == room:
            return k
    raise Exception("unknown room " + repr(room)) 


