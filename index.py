from profane_detector import ProfaneDetector

profane_detector = ProfaneDetector()

to_detect = "fuck you!"
language = "en"

did_detect = profane_detector.detect_api(language, to_detect)
print(did_detect)