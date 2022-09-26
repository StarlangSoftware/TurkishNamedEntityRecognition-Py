import pkg_resources

from NamedEntityRecognition.Gazetteer import Gazetteer


class AutoNER:

    person_gazetteer: Gazetteer
    organization_gazetteer: Gazetteer
    location_gazetteer: Gazetteer

    def __init__(self):
        """
        Constructor for creating Person, Organization, and Location gazetteers in automatic Named Entity Recognition.
        """
        self.person_gazetteer = Gazetteer("PERSON", pkg_resources.resource_filename(__name__, 'data/gazetteer-person.txt'))
        self.organization_gazetteer = Gazetteer("ORGANIZATION", pkg_resources.resource_filename(__name__, 'data/gazetteer-organization.txt'))
        self.location_gazetteer = Gazetteer("LOCATION", pkg_resources.resource_filename(__name__, 'data/gazetteer-location.txt'))
