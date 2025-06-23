#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from python_developer.crew import PythonDeveloper

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

task = """Run a python program to calculate the first 10,000 terms of this series,

        multiplying the total by 4: 1 - 1/3 + 1/5 - 1/7 + ... """

def run():
    """
    Run the crew.
    """
    inputs = {

        'task': task

    }
    
    try:

        result = PythonDeveloper().crew().kickoff(inputs=inputs)

        print(result.raw)

    except Exception as e:

        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == '__main__':

    run()