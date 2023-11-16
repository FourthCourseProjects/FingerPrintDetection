from DistanceCalculator import DistanceCalculator


class FingerPrintDistanceDTO:
    def __init__(self, finger_print, distance):
        self.fingerprint = finger_print
        self.distance = distance

    def __str__(self):
        return self.fingerprint.name + " --> " + str(self.distance) if self.fingerprint is not None else "Not found"


class FingerPrintComparator:
    def __init__(self, finger_prints):
        self._fingerprints = finger_prints
        self._distance_calculator = DistanceCalculator()

    def fingerprint_similar_to(self, this_finger_print):
        result = []
        for finger_print in self._fingerprints:
            dto = self.create_dto(self._distance_calculator.distance_for(this_finger_print, finger_print), finger_print)
            result.append(dto)
        return result

    def create_dto(self, distance, finger_print):
        return FingerPrintDistanceDTO(finger_print, distance)