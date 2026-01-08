from src.extractor import AmulSKUExtractor

extractor = AmulSKUExtractor()

tests = [
    "please book amul taza milk 500 ml 1000",
    "ok bhai amul taza milk chahiye 500ml qty 1000",
    "500ml amul taza milk dedo 1000",
    "sir order amul butter salted 200gm 50 nos",
    "amul almond milk 1 l add 20"
]

for t in tests:
    print("\nInput:", t)
    print("Output:", extractor.extract(t))

