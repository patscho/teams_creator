from participant import Participant
import random


class Teams:
    def __init__(self, participants: list[Participant], team_size: int) -> None:
        self.teams = []
        random.shuffle(participants)
        number_of_teams = len(participants) // team_size
        if number_of_teams == 0:
            number_of_teams = 1
        for _ in range(number_of_teams):
            self.teams.append(Team())
        for i in range(len(participants)):
            team_index = i % number_of_teams
            self.teams[team_index].add_member(participants[i])


class Team:
    """
    A class to represent a team.
    On init an empty team will be instantiated. Members need to be added using the add_member method

    ...

    Attributes:
    -----------
    None

    Methods:
    --------
    add_member(participant: Participant):
        Adds a new participant to the team.
        The first team member will be the designated team captain.

    print():
        Prints the team in a human readable way.
    """

    def __init__(self) -> None:
        """
        Constructs an emtpy team and assigns a name.
        """
        self.members = []
        self.captain_assigned = False
        self.name = self.__create_team_name()

    def add_member(self, participant: Participant):
        """
        Adds a new participant to the team.
        The first team member will be the designated team captain.
        """
        if not self.captain_assigned:
            self.captain = participant
            self.captain_assigned = True
        else:
            self.members.append(participant)

    def print(self):
        """
        Prints the team in a human readable way.
        """
        print(f"Team name: {self.name}")
        print(f"Team captain: {self.captain.name}")
        print("Team members: ")
        for member in self.members:
            print(f"  - {member.name}")

    def __create_team_name(self):
        """
        Read adjectives and crafts from file and construct a team name
        in the form of: adjective craft.
        For example: Revolting Receptionists
        """
        with open("adjectives.txt") as adj_file:
            adjectives = [line.strip() for line in adj_file.readlines()]
        with open("crafts.txt") as crafts_file:
            crafts = [line.strip() for line in crafts_file.readlines()]
        adjective = random.choice(adjectives).title()
        craft = random.choice(crafts).title()
        return f"{adjective} {craft}"
