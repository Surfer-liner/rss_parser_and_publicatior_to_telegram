# RSS Parser Feeds, Publicating and Reacting to Messages in Telegram

## Table of Contents
- [Description](#description)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the forbes_rss_content_parser.py module](#running-the-forbes_rss_content_parserpy-module)
  - [Running the telegram_reactions.py module](#running-the-telegram_reactionspy-module)
- [Contributing](#contributing)
- [License](#license)

## Description
This application consists of two modules:
1. The `forbes_rss_content_parser.py` module is responsible for parsing the Forbes RSS feed and extracting relevant news articles based on specified categories.
2. The `telegram_reactions.py` module is responsible for reacting to messages in a Telegram group by randomly selecting a reaction from a predefined list and sending it as a reply to the message.

## Setup
### Prerequisites
- Python 3.7 or above
- pip (Python package installer)

### Installation
1. Clone the repository or download the application files.

2. Create a virtual environment for the application. Run the following command in the project directory:
    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment. Run the appropriate command based on your operating system:
- For Windows:
    ```
    venv\Scripts\activate
    ```
- For macOS/Linux:
    ```
    source venv/bin/activate
    ```

4. Install the required Python libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```
   

## Usage
1. Running the `forbes_rss_content_parser.py` module:
- Set the `rss_url` variable in the `forbes_rss_content_parser.py` file to the desired Forbes RSS feed URL.
- Specify the `categories` list with the desired categories to filter the news articles.
- Run the module to parse the RSS feed, download images (if available), and store the processed links.
- The parsed news articles will be saved in the `parsed_items` list.

2. Running the `telegram_reactions.py` module:
- Ensure the `forbes_rss_content_parser.py` module has been run at least once to populate the `parsed_items` list.
- Set the `TOKEN` and `CHAT_ID` variables in the `telegram_reactions.py` file with the respective values.
- Adjust the `reactions` list with the desired reaction emojis.
- Run the module to start the Telegram bot.
- The bot will listen for new messages in the Telegram group and randomly select a reaction to reply with.

Note: Both modules need to be running simultaneously for the complete functionality of the application.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
