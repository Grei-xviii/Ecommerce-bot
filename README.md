# E-commerce Bot

An automated web testing bot for e-commerce websites using Python and Playwright. This project demonstrates automated user interactions including account creation, login, and product search functionality.

## 📋 Project Overview

This project contains an automated testing bot that interacts with an e-commerce website (automationexercise.com) to perform common user actions such as:

- User account registration with randomly generated credentials
- Form filling with personal details
- Product searching
- Navigation through different pages
- Comprehensive logging of all automation activities

## 🗂️ Project Structure

```
Ecommerce-bot/
├── app.py              # Simple Python practice file with basic programming examples
├── Ecommerce_bot.py    # Main automation script with e-commerce testing logic
├── logs/               # Directory containing automation logs
│   └── warmup.log      # Detailed log file of bot activities and errors
└── README.md           # This file
```

## 📁 File Descriptions

### `Ecommerce_bot.py` (Main Script)
The core automation script that uses Playwright to:
- Launch a Chromium browser instance
- Navigate to the automationexercise.com website
- Create new user accounts with random credentials
- Fill comprehensive signup forms including personal details
- Search for products on the e-commerce platform
- Handle errors and log all activities

**Key Features:**
- Asynchronous operation using `asyncio`
- Random username and email generation for unique accounts
- Comprehensive form filling (name, address, contact details)
- Product search functionality
- Robust error handling and logging

### `app.py` (Practice File)
A simple Python file containing basic programming exercises including:
- Loop demonstrations (while and for loops)
- List manipulation and indexing
- Finding maximum values in arrays
- Basic Python syntax examples

### `logs/warmup.log`
Detailed log file that tracks:
- Successful operations and their timestamps
- Error messages with specific failure details
- Navigation activities
- Form submission attempts
- Timeout and connection issues

## 🛠️ Technology Stack

- **Python**: Main programming language
- **Playwright**: Web automation framework for browser control
- **asyncio**: Asynchronous programming support
- **logging**: Built-in Python logging for activity tracking
- **random**: For generating unique test data

## 🚀 Getting Started

### Prerequisites

1. Python 3.7 or higher
2. Install required dependencies:

```bash
pip install playwright asyncio
```

3. Install Playwright browsers:

```bash
playwright install
```

### Running the Bot

Execute the main automation script:

```bash
python Ecommerce_bot.py
```

The bot will:
1. Open a Chromium browser window
2. Navigate to the e-commerce site
3. Create a new user account
4. Search for products
5. Log all activities to `logs/warmup.log`

## 📊 Features

### Automated User Registration
- Generates random usernames and emails
- Fills complete registration forms
- Handles account creation process

### Product Search
- Navigates to product catalog
- Performs search queries
- Handles search results

### Comprehensive Logging
- Timestamps all activities
- Records both successful operations and errors
- Provides detailed error messages for debugging

### Error Handling
- Graceful handling of timeouts
- Connection error management
- Browser closure on failures

## 🔧 Configuration

The bot is currently configured to work with:
- **Target Site**: automationexercise.com
- **Browser**: Chromium (headless=False for visible browser)
- **Log File**: logs/warmup.log
- **Timeouts**: 10-30 seconds for various operations

## 📝 Logging

All bot activities are logged to `logs/warmup.log` with timestamps and detailed information about:
- Navigation events
- Form submissions
- Search operations
- Error conditions
- Performance metrics

## ⚠️ Known Issues

Based on the log files, common issues include:
- Certificate authority errors when connecting to the target site
- Timeout errors when waiting for specific page elements
- Browser closure during long-running operations

## 🔮 Future Enhancements

Potential improvements could include:
- Add support for multiple e-commerce sites
- Implement product addition to cart functionality
- Add checkout process automation
- Create configuration files for easy customization
- Add more robust error recovery mechanisms
- Implement parallel testing with multiple browser instances

## 🤝 Contributing

This appears to be a learning/practice project. To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project appears to be for educational/testing purposes. Please ensure compliance with the target website's terms of service and robots.txt file.

## ⚖️ Disclaimer

This bot is designed for educational and testing purposes only. Please ensure you have proper authorization before running automated scripts against any website and always respect the website's terms of service and rate limiting policies.
