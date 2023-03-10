class Participant:
    """This class takes the first part from an outlook response as input
    For example from this following outlook response:
        Zee, M. van der (Marcel)	Optional Attendee	Declined
    This class uses only Zee, M. van der (Marcel) as input.
    Because we have participants from NL, PL, PH, RO and other countries and there
    is no uniform way of how names are presented in the init function the name
    in a format 'first_name middle_stuff last_name' will be constructed
    Right now this class is capable of handling the following types of input

    NL: Graaff, B. de (Bas)
    RO: Gutu, N.G. (Nicolae - Dragos)
    PH: Sarmiento, Jaybee
    PL: KAŹMIERKIEWICZ, K. (KONRAD)
    """

    def __init__(self, raw_input: str) -> None:
        self.raw_input = raw_input
        if ")" not in raw_input:
            # PH
            last_name, first_name = raw_input.split(",")
            self.last_name = last_name.strip()
            self.first_name = first_name.strip()
            self.middle = ""
        else:
            first_name_part = raw_input.split(",")[1]
            first_name = first_name_part.split("(")[-1][:-1]
            middle_part = first_name_part.split("(")[0].split(".")[-1].strip()
            self.last_name = raw_input.split(",")[0].strip()
            self.first_name = first_name
            self.middle = middle_part
        if self.first_name.isupper():
            self.first_name = self.first_name.title()
        if self.last_name.isupper():
            self.last_name = self.last_name.title()
        if " - " in self.first_name:
            self.first_name = self.first_name.split("-")[0].strip()
        if self.middle == "":
            self.name = self.first_name + " " + self.last_name
        else:
            self.name = self.first_name + " " + self.middle + " " + self.last_name
