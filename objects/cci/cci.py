class Cci:
    def __init__(self):
        self.cci_id = ""
        self.status = ""
        self.publishdate = ""
        self.contributor = ""
        self.definition = ""
        self.type = ""
        self.parameter = ""
        self.note = ""
        self.references = None

    def __str__(self) -> str:
        string = "Cci{{ \n" \
                 "\tid={} \n" \
                 "\tstatus={} \n" \
                 "\tpublishdate={} \n" \
                 "\tcontributor={} \n" \
                 "\tdefinition={} \n" \
                 "\ttype={} \n" \
                 "\tparameter={} \n" \
                 "\tnote={} \n" \
                 "\treferences={} \n" \
                 "}}"
        return string.format(
            self.id,
            self.status,
            self.publishdate,
            self.contributor,
            self.definition,
            self.type,
            self.parameter,
            self.note,
            self.references
        )

    def __eq__(self, other):
        if not isinstance(other, Cci):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
