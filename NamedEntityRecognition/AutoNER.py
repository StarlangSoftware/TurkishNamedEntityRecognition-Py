import pkg_resources

from NamedEntityRecognition.Gazetteer import Gazetteer


class AutoNER:

    personGazetteer: Gazetteer
    organizationGazetteer: Gazetteer
    locationGazetteer: Gazetteer

    def __init__(self):
        """
        Constructor for creating Person, Organization, and Location gazetteers in automatic Named Entity Recognition.
        """
        self.personGazetteer = Gazetteer("PERSON", pkg_resources.resource_filename(__name__, 'data/gazetteer-person.txt'))
        self.organizationGazetteer = Gazetteer("ORGANIZATION", pkg_resources.resource_filename(__name__, 'data/gazetteer-organization.txt'))
        self.locationGazetteer = Gazetteer("LOCATION", pkg_resources.resource_filename(__name__, 'data/gazetteer-location.txt'))
