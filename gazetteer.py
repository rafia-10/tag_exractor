import json
import re

class GazetteerExtractor:
    def __init__(self, gazetteer_path):
        with open(gazetteer_path, 'r') as f:
            self.gazetteer = json.load(f)

    def preprocess(self, text):
        # Lowercase and remove special characters
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def extract_tags(self, text):
        text = self.preprocess(text)
        tags = []
        for category, items in self.gazetteer.items():
            for item in items:
                if item.lower() in text:
                    tags.append((item, category))
        return tags
