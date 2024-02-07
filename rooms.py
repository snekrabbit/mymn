rooms = {
    "the_plane": {
        "desc": "the plane to siberia",
        "enter": """Dr. Plimph just welcomed you to Cairo for your egyptology internship, your dream job!
But before you can unpack your bags he says that you're both going to Siberia to examine a mysterious cave covered in hieroglyphics.
You hesitate at the stairs of the plane as you see Dr. Plimph disappear inside.""",
        "exit": """The things I do for this job""",
        "directions": {
            "UP": {
                "desc": "GO UP to follow him?",
                "room": "the_cave"
            },
        }

    },
    "the_cave": {
        "enter": "You hurried from the airport and stopped suddenly on a small road. To the North, you can see the uncovered cave door",
        "directions": {
            "N": {
                "desc": "Man that's scary, but this is your job right?",
                "room": "the_door"
            },
        }
    },
    "the_door": {
        "enter": """The gigantic door is covered in hieroglyphics. Oh, that must be why they needed Dr. Plimph!
He scans the text, starts laughing, and puts his finger in the belly-button of the small goblin in the corner.""",
        "directions": {
            "W": {"desc": "The door slides upward with a loud crack! Dr. Plimph runs inside, still lauhghing. Are you really going to follow this man?", "room": "the_hallway"},
         },
    },
    "the_hallway": {
        "enter": "'Touch nothing!' shouts Dr. Plimph, as he hurries down the darkened hall, giggling into his sleeve. You stay behind, nervously wondering if you should follow.",
        "directions": {
            "LOOK": {
                "desc": "You see a glowing rock. As you bend to look closer, you realize you're sinking into quicksand.", 
                "room": "the_pit", 
                "action": "As the sand closes over your head, you start moving faster as you realize you're sliding down a sandy tube..."
            },
         },
        "automate": "LOOK",
    },
    "the_pit": {
        "enter": "That was horrible! You emerged from the sand with a sticky plop and drop to the floor.",
        "exit": None,
        "desc": "A dark room with stone walls and floor",
        "directions": {
            "N": {"desc": "You see a glowing door", "room": "the_end"},
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

# add the name to all the room objects
for name, room in rooms.items():
    room['name'] = name

def get_room_name(room):
    for k, v in rooms.rooms.items():
        if v == room:
            return k
    raise Exception("unknown room " + repr(room))
