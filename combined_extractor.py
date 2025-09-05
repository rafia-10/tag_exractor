
from gazetteer import GazetteerExtractor
from spacy_extractor import SpacyExtractor
from llm_extractor import LLMExtractor


class CombinedTagExtractor:
    def __init__(self, gazetteer_path):
        self.gazetteer_extractor = GazetteerExtractor(gazetteer_path)
        self.spacy_extractor = SpacyExtractor()
        self.llm_extractor = LLMExtractor()


        # Priority mapping
        self.source_priority = {"gazetteer": 3, "spacy": 2, "llm": 1}

    def extract_tags(self, text):
        # Run all three extraction methods
        gaz_tags = self.gazetteer_extractor.extract_tags(text)  # list of (tag, category)
        spacy_tags = self.spacy_extractor.extract_tags(text)    # list of (tag, label)
        llm_tags = self.llm_extractor.extract_tags(text)        # list of tags (no category)

        all_tags = gaz_tags + spacy_tags + llm_tags
        # Normalize spaCy labels to gazetteer-like categories (simple mapping)

        # Deduplicate using priority
        tag_dict = {}
        for tag, cat, source in all_tags:
            tag_lower = tag.lower()
            # If tag not seen yet, or new source has higher priority
            if tag_lower not in tag_dict or self.source_priority[source] > self.source_priority[tag_dict[tag_lower][1]]:
                tag_dict[tag_lower] = (tag, source, cat)
        merged_tags = [(v[0], v[2]) for v in tag_dict.values()]
        return merged_tags


# --------- Main Execution ---------
if __name__ == "__main__":
    user_text = input("Enter your text: ")
    combined_extractor = CombinedTagExtractor("data/gazetteer.json")
    tags = combined_extractor.extract_tags(user_text)
    print("\nExtracted Tags:")
    for tag, category in tags:
        print(f"{tag} ({category})")
