from teams import Team
from participant import Participant

name1 = "Dokter, D.J. (Danny)"
name2 = "Fabricante, Kristoffer Magic"
p1 = Participant(name1)
p2 = Participant(name2)
t = Team()
t.add_member(p1)
t.add_member(p2)
t.print()
