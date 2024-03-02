# Boarding Passes API

This project provides an API to sort a list of boarding passes for various transportation methods to complete a journey from point A to point B via several stops.

## How to Execute the Code

1. Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. Clone this repository to your local machine or download the source code as a ZIP file and extract it.

3. Open a terminal or command prompt and navigate to the root directory of the project.

4. Run the main.py script to see the sorted list of boarding passes:

    ```
    python main.py
    ```

    This will display the sorted list of boarding passes along with the description of the journey.

## How to Execute the Tests

1. Make sure you have followed steps 1-3 from the "How to Execute the Code" section.

2. In the terminal or command prompt, navigate to the root directory of the project.

3. Run the following command to execute the unit tests:

    ```
    python -m unittest discover -s tests
    ```

    This will run all the unit tests in the `tests` directory and display the test results.

## Assumptions

- The boarding passes are provided in a list format.
- There is a single unbroken chain of boarding passes, i.e., it's one continuous trip with no interruptions.
- The starting point is determined by finding a pass with no origin in any other pass's destination.
- The transportation types include Train, Bus, and Flight. Additional types can be easily added by extending the BoardingPass class.
- The sorting algorithm has a complexity of O(n) where n is the number of boarding passes.

