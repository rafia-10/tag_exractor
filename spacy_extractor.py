import spacy

class SpacyExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_tags(self, text):
        doc = self.nlp(text)
        tags = []
        for ent in doc.ents:
            tags.append((ent.text, ent.label_))
        return tags
