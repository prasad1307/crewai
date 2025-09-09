#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from crewdemo1.crew import StudyNotesDemo
    

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def _default_inputs():
    return {
        'subject': 'Python Basics',           # 👈 Change this to SVM, NumPy, etc.
        'level': 'beginner',                  # beginner | intermediate | advanced
        'formatting_style': 'concise',        # concise | detailed
        'current_year': str(datetime.now().year)
    }

def run():
    try:
        StudyNotesDemo().crew().kickoff(inputs=_default_inputs())
    except Exception as e:
        raise Exception(f"Error while running StudyNotesDemo crew: {e}")

def train():
    try:
        StudyNotesDemo().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=_default_inputs()
        )
    except Exception as e:
        raise Exception(f"Error while training StudyNotesDemo crew: {e}")

def replay():
    try:
        StudyNotesDemo().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Error while replaying StudyNotesDemo crew: {e}")

def test():
    try:
        StudyNotesDemo().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=_default_inputs()
        )
    except Exception as e:
        raise Exception(f"Error while testing StudyNotesDemo crew: {e}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'run'
    if cmd == 'run':
        run()
    elif cmd == 'train':
        train()
    elif cmd == 'replay':
        replay()
    elif cmd == 'test':
        test()
    else:
        print("Unknown command. Use: run | train | replay | test")
