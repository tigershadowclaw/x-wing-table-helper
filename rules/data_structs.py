class characteristicType:
    id = ""
    name = ""
    value = ""
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.id}{self.name}"

class categoryLinks:
    id = ""
    name = ""
    hidden = False
    targetId = ""
    primary = False

    def __init__(self, id: str, name: str, hidden: bool, targetId: str, primary: bool) -> None:
        self.id = id
        self.name = name
        self.hidden = hidden
        self.targetId = targetId
        self.primary = primary

class constraints:
    field = ""
    scope = ""
    value = ""
    percentValue = False
    shared = False
    includeChildSelections = False
    includeChildForces = False
    id = ""
    type = ""

    def __init__(self, field: str, scope: str, value: float, percentValue: bool, shared: bool, includeChildSelections: bool, includeChildForces: bool, id: str, type: str) -> None:
        self.field = field
        self.scope = scope
        self.value = value
        self.percentValue = percentValue
        self.shared = shared
        self.includeChildSelections = includeChildSelections
        self.includeChildForces = includeChildForces
        self.id = id
        self.type = type

class categoryEntries:
    id = ""
    name = ""
    hidden = False
    categoryLink = None
    constraint = []

    def __init__(self, id: str, name: str, hidden: bool, categoryLink: categoryLinks, constraint: constraints) -> None:
        self.id = id
        self.name = name
        self.hidden = hidden
        self.categoryLink = categoryLink
        self.constraint = constraint

class forceEntries:
    id = ""
    name = ""
    categoryLink = []


class profileType:
    id = ""
    name = ""
    characteristicTypes = []

    def __init__(self, id: str, name: str, characteristicTypes: characteristicType):
        self.id = id
        self.name = name
        self.characteristicTypes = characteristicTypes

    def __str__(self):
        return f"({self.id}){self.name} # of Characteristics: {self.characteristicTypes.count}"