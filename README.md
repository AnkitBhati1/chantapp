# chantapp
Django Real-Time Chat Application

**Table of Contents**

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## About

The Django Real-Time Chat Application is platform that enables real-time communication between users. Built using Django and Django Channels, this application offers features such as user registration, authentication, instant messaging, friend recommendations, and more.

## Features

- **User Registration and Authentication:**
  - Users can create accounts and log in securely.
  - Django's built-in authentication system is utilized for enhanced security.

- **Real-Time Chat Functionality:**
  - Real-time messaging using Django Channels.
  - Users can see online contacts and initiate chats.
  - Messages are sent and received instantly for a seamless experience.

- **RESTful APIs:**
  - Django REST Framework (DRF) powers APIs for registration, login, and chat functionality.
  - API endpoints for registration, login, online user retrieval, chat initiation, and message sending.

- **Message Delivery Control:**
  - Prevent users from sending messages to offline recipients.
  - Ensure messages reach active users.

- **Friend Recommendations:**
  - Efficient recommendation algorithm for suggesting friends.
  - Helps users connect with potential friends sharing common interests.

- **Testing and Quality Assurance:**
  - Comprehensive test cases for API and application functionality.
  - Automated testing for consistent performance.
  - Error handling for various scenarios.

- **Version Control and Collaboration:**
  - Code hosted on GitHub for collaborative development.
  - Team members have access to the repository for seamless teamwork.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Django
- Django Channels
- Django REST Framework
- Redis

### Installation

1. Clone the repository:

   ```bash
   https://github.com/AnkitBhati1/chantapp.git
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
5. Start Redis server
  ''' bash
  sudo service redis-server start 
  '''
   
7. Start the development server:

   ```bash
   python manage.py runserver
   ```

Now, your Django Real-Time Chat Application should be up and running locally.

## Usage

1. Access the application at `http://localhost:8000` in your web browser.
2. Register a new account or log in if you already have one.
3. Explore the real-time chat features, send messages, and discover recommended friends.

## API Endpoints

- **User Registration**: `POST /api/register/`
- **User Login**: `POST /api/login/`
- **Get Online Users**: `GET /api/online-users/`
- **Start a Chat**: `POST /api/chat/start/`
- **Send a Message**: `WEBSOCKET /api/chat/send/`
- **Recommended Friends**: `GET /api/suggested-friends/<user_id>`

