# Cheap Flight Notifier

This Python project serves as a cheap flight notifier, allowing users to track the price of flights from a specified source to destination. Users can set their desired price, and when the ticket price hits that desired price, the program automatically sends a mobile message notification to the user. It leverages flight data APIs and messaging services to provide real-time updates on flight prices.

## Features

- **Flight Price Tracking**: Tracks the price of flights from a specified source to destination.
- **Custom Price Alert**: Allows users to set their desired price for flight tickets.
- **Real-time Notifications**: Sends mobile message notifications to the user when the ticket price hits the desired price.
- **Flight Data APIs**: Utilizes flight data APIs to retrieve real-time information about flight prices.
- **Messaging Service Integration**: Integrates with messaging services (e.g., Twilio) to send notifications to the user's mobile phone.

## Technologies Used

- **Python Libraries**:
  - `requests` for making HTTP requests to flight data APIs
  - `Twilio` or similar libraries for sending mobile message notifications
- **Flight Data APIs**: Utilizes flight data APIs such as Skyscanner, Google Flights, or similar services for retrieving flight prices.
- **Messaging Service**: Integrates with messaging services like Twilio for sending mobile message notifications.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/cheap-flight-notifier.git`
2. Navigate to the project directory: `cd cheap-flight-notifier`
3. Install dependencies: `pip install -r requirements.txt`
4. Sign up for a developer account with a flight data API provider (e.g., Skyscanner) and obtain an API key.
5. Sign up for a messaging service provider (e.g., Twilio) and obtain credentials for sending mobile messages.

## Usage

1. Configure the flight data API key and messaging service credentials in the appropriate configuration file or environment variables.
2. Run the main Python script: `python main.py`.
3. Follow the prompts to enter the source, destination, and desired price for the flight ticket.
4. The program will continuously monitor the flight prices and send a mobile message notification when the ticket price hits the desired price.
5. Optionally, configure additional settings such as the frequency of price checks or specific airlines to track.
