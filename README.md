# Lichess Player Analysis Dashboard

## Overview

The Lichess Player Analysis Dashboard is a Streamlit application designed to provide insights into a Lichess player's chess games. It fetches game data, analyzes openings, and visualizes player statistics across various game formats, allowing users to gain a deeper understanding of their chess performance and strategies.

As for games from chess.com; they require signing up via a google form to get OAuth access. Will look into it in the future.
## Features

- Fetch and display the player's game data from Lichess in PGN format.
- Analyze and visualize the most played openings by the user.
- Display win/loss/draw statistics for different game formats.
- Show rating progression over time for various game formats.
- Intuitive and interactive user interface built with Streamlit.

## Installation

To set up the project, follow these steps:

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Pandas
- Plotly
- Requests
- python-chess

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/lichess-player-analysis-dashboard.git
cd LichessDataVisualization
```
### Step 2: Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Required Packages
You can install the required packages using pip:

```bash
pip install streamlit pandas plotly requests python-chess
```
Or you can run the below command to install dependecies using requirements.txt (ensure to cd into the repo folder)

```bash
pip install -r requirements.txt
```
### Step 4: Run the Application
To start the Streamlit application, run the following command:

```bash
streamlit run main.py
```
The application will open in your default web browser, typically at http://localhost:8501

## Project Structure
The project is organized into the following modules:
```graphql
lichess-player-analysis-dashboard/
│
├── data_fetching.py    # Contains functions for fetching data from the Lichess API.
├── data_processing.py   # Contains functions for processing and analyzing game data.
├── main.py             # The main Streamlit application logic.
├── Chess_Openings.csv   # CSV file containing ECO to opening name mappings.
└── README.md           # Project documentation.
```

## Usage
 - Enter Lichess Username: In the application, enter the Lichess username you want to analyze.
 - Select Number of Games: Use the slider to choose how many of the most recent games to analyze.
 - View Results: The dashboard will display:
   - A bar chart of the most played openings.
   - A pie chart of the win/loss/draw ratios for various game formats.
   - Rating progression charts for each game format.

## License
This project is licensed under the GNU Public License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.

## Contact
For any questions or feedback, please reach out to me at anshumancos3@gmail.com

