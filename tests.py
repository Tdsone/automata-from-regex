from automaton import WordGenerator

test_cases = [
    {
        "test": "(AB+ASC)",
        "expected": ["AB","ASC"]
    },
    {
        "test": "(SDJS)(HD+DJ)(ABS)",
        "expected": ["SDJSHDABS","SDJSDJABS"]
    },
    {
        "test": "AB+BH+JK",
        "expected": ["AB","BH","JK"]
    },
    {
        "test": "(AB+HU(AB+HU))+AB",
        "expected": ["AB", "HUAB", "HUHU"]
    },
    {
        "test": "",
        "expected": []
    },
]

def test_word_generator():
    for test in test_cases:
        print(f"Testing {test['test']}...")
        try:
            word_generator = WordGenerator(test["test"])
            decisions = word_generator.build_decision_list()
            computed = word_generator.generate_word(decision_list=decisions)    
            print(f"computed: {computed}")
            assert computed in test['expected']
        except Exception as e:
            if not test['test']:
                assert True
            else:
                assert False
        