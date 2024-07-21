# Sam - The Coffee Shop Chatbot

Sam is a conversational agent designed to assist users with inquiries related to coffee shop operations. It uses natural language processing (NLP) and a neural network model to classify user inputs and generate appropriate responses.

## Features

- Responds to greetings, farewells, and thank you messages.
- Provides information on menu items, payment methods, and delivery charges.
- Offers a conversational interface for users to interact with the chatbot.

## Project Structure

- `intents.json`: Contains the predefined intents and their associated patterns and responses.
- `model.py`: Defines the neural network architecture.
- `spacy_utils.py`: Contains utility functions for text preprocessing (tokenizing, stemming, bag-of-words).
- `train.py`: Script for training the neural network model.
- `chat.py`: Script for running the chatbot interface.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/coffee-shop-chatbot.git
    cd coffee-shop-chatbot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Download and install SpaCy's small English model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage

### Training the Model

To train the model, run the `train.py` script:
```bash
python train.py

### Example Interaction
Let's chat! (type 'quit' to exit)
You: Hi
Sam: Hello, thanks for visiting

You: What do you sell?
Sam: We sell coffee and tea

You: Do you take credit cards?
Sam: We accept VISA, Mastercard and Paypal

You: How long does delivery take?
Sam: Delivery takes 2-4 days

You: Tell me a joke!
Sam: Why did the hipster burn his mouth? He drank the coffee before it was cool.

You: Goodbye
Sam: See you later, thanks for visiting


