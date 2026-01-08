import spacy
from spacy.pipeline import EntityRuler
from .preprocess import preprocess_text
import re

VARIANTS = ["raw", "almond", "soy", "toned", "full cream", "taza"]
UNITS = {"ml", "l", "gm", "kg"}

class AmulSKUExtractor:
    def __init__(self, model_path="model/amul_sku_model"):
        self.nlp = spacy.load(model_path)

        # 🔥 ADD ENTITY RULER AT RUNTIME
        if "entity_ruler" not in self.nlp.pipe_names:
            ruler = self.nlp.add_pipe("entity_ruler", before="ner")
            ruler.add_patterns([
                {"label": "QUANTITY", "pattern": [{"LIKE_NUM": True}]},
                {"label": "UNIT", "pattern": [{"LOWER": {"IN": list(UNITS)}}]},
            ])

    def extract_variant(self, product):
        for v in VARIANTS:
            if v in product.lower():
                return v
        return None

    def extract(self, text):
        clean = preprocess_text(text)
        doc = self.nlp(clean)

        result = {
            "product": None,
            "variant": None,
            "quantity": [],
            "unit": []
        }

        for ent in doc.ents:
            if ent.label_ == "PRODUCT":
                result["product"] = ent.text
                result["variant"] = self.extract_variant(ent.text)

            elif ent.label_ == "QUANTITY":
                result["quantity"].append(ent.text)

            elif ent.label_ == "UNIT":
                result["unit"].append(ent.text)

        return result
