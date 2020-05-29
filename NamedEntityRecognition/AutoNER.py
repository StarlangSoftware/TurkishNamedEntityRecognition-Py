from NamedEntityRecognition.Gazetteer import Gazetteer


class AutoNER:

    personGazetteer: Gazetteer
    organizationGazetteer: Gazetteer
    locationGazetteer: Gazetteer

    def __init__(self):
        """
        Constructor for creating Person, Organization, and Location gazetteers in automatic Named Entity Recognition.
        """
        self.personGazetteer = Gazetteer("PERSON", "gazetteer-person.txt")
        self.organizationGazetteer = Gazetteer("ORGANIZATION", "gazetteer-organization.txt")
        self.locationGazetteer = Gazetteer("LOCATION", "gazetteer-location.txt")
