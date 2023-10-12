current_room = "the_pit"
rooms = {
    "the_pit": {
        "enter": "You slide to a halt covered in dust.",
        "exit": None,
        "desc": "A dark room with stone walls and floor",
        "directions": {
            "N": {"desc": "a glowing door", "room": "the_end"},
            "D": {"desc": "a dark hole", "room": "pit_hole"}
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
