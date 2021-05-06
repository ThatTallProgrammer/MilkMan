class Reference:
    def __init__(self):
        self.index = ""
        self.creator = ""
        self.title = ""
        self.version = ""
        self.location = ""

    def __str__(self):
        string = "Reference{{ \n" \
                 "\tindex={} \n" \
                 "\tcreator={} \n" \
                 "\ttitle={} \n" \
                 "\tversion={} \n" \
                 "\tlocation={} \n" \
                 "}}"
        return string.format(
            self.index,
            self.creator,
            self.title,
            self.version,
            self.location
        )

    def __eq__(self, other):
        if not isinstance(other, Reference):
            return False
        return self.index == other.index

    def __hash__(self):
        return hash(self.index)
