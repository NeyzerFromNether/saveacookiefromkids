import json

with open('data.json', 'r') as file:
  data = json.load(file)

ENEMY_SPAWN_DATA = [
  {
    #1
    "weak": 5,
    "medium": 0,
    "strong": 0,
    "elite": 0
  },
  {
    #2
    "weak": 10,
    "medium": 0,
    "strong": 0,
    "elite": 0
  },
  {
    #3
    "weak": 15,
    "medium": 1,
    "strong": 0,
    "elite": 0
  },
  {
    #4
    "weak": 0,
    "medium": 7,
    "strong": 0,
    "elite": 0
  },
  {
    #5
    "weak": 0,
    "medium": 0,
    "strong": 5,
    "elite": 0
  },
  {
    #6
    "weak": 0,
    "medium": 10,
    "strong": 3,
    "elite": 0
  },
  {
    #7
    "weak": 0,
    "medium": 12,
    "strong": 5,
    "elite": 0
  },
  {
    #8
    "weak": 0,
    "medium": 10,
    "strong": 10,
    "elite": 0
  },
  {
    #9
    "weak": 0,
    "medium": 10,
    "strong": 5,
    "elite": 0
  },
  {
    #10
    "weak": 0,
    "medium": 10,
    "strong": 0,
    "elite": 0
  },
  {
    #11
    "weak": 5,
    "medium": 10,
    "strong": 12,
    "elite": 0
  },
  {
    #12
    "weak": 0,
    "medium": 15,
    "strong": 10,
    "elite": 0
  },
  {
    #13
    "weak": 20,
    "medium": 0,
    "strong": 25,
    "elite": 0
  },
  {
    #14
    "weak": 0,
    "medium": 0,
    "strong": 15,
    "elite": 0
  },
  {
    #15
    "weak": 0,
    "medium": 0,
    "strong": 0,
    "elite": 1
  }
]

if data["hard_mode"] == True:
    ENEMY_DATA = {
        "weak": {
            "health": 15,
            "speed": 1
        },
        "medium": {
            "health": 30,
            "speed": 3
        },
        "strong": {
            "health": 40,
            "speed": 5
        },
        "elite": {
            "health": 2000,
            "speed": 1.5
        }
    }
else:
    ENEMY_DATA = {
        "weak": {
            "health": 10,
            "speed": 0.5
        },
        "medium": {
            "health": 15,
            "speed": 2
        },
        "strong": {
            "health": 20,
            "speed": 3.3
        },
        "elite": {
            "health": 400,
            "speed": 1
        }
    }