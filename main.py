from participant import Participant
from teams import Teams

INPUT_FILE = "responses.txt"
TEAM_SIZE = 5


def read_input(filename):
    with open(filename) as file:
        my_input = [
            line.strip().split("\t")[0]
            for line in file.readlines()
            if "Accepted" in line
        ]
    return my_input


def main():
    names = read_input(INPUT_FILE)
    participants = []
    for name in names:
        participants.append(Participant(name))
    my_teams = Teams(participants, TEAM_SIZE)
    for team in my_teams.teams:
        team.print()
        print("------------------------------------")


if __name__ == "__main__":
    main()
