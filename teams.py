from participant import Participant
import random


class Teams:
    def __init__(self, participants: list[Participant], team_size: int) -> None:
        self.teams = []
        random.shuffle(participants)
        number_of_teams = len(participants) // team_size
        for _ in range(number_of_teams):
            self.teams.append(Team())
        for i in range(len(participants)):
            team_index = i % number_of_teams
            self.teams[team_index].add_member(participants[i])


class Team:
    def __init__(self) -> None:
        self.members = []
        self.captain_assigned = False
        self.name = self.create_team_name()

    def add_member(self, participant: Participant):
        if not self.captain_assigned:
            self.captain = participant
            self.captain_assigned = True
        else:
            self.members.append(participant)

    def print(self):
        print(f"Team name: {self.name}")
        print(f"Team captain: {self.captain.name}")
        print("Team members: ")
        for member in self.members:
            print(f"  - {member.name}")

    def create_team_name(self):
        with open("adjectives.txt") as adj_file:
            adjectives = [line.strip() for line in adj_file.readlines()]
        with open("crafts.txt") as crafts_file:
            crafts = [line.strip() for line in crafts_file.readlines()]
        adjective = random.choice(adjectives).title()
        craft = random.choice(crafts).title()
        return f"{adjective} {craft}"
