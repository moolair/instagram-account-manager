# Instagram Account Manager

A Python-based tool to streamline Instagram account management. This project automates the process of identifying accounts that don't follow you back, selecting them via a user-friendly UI, and migrating them to a secondary account.

## Features

- **Login Automation**: Log in to both primary and secondary accounts securely.
- **Unfollow Insights**: Fetch accounts that don't follow you back.
- **Selection UI**: Choose accounts to migrate using a simple checkbox-based interface.
- **Migration Automation**: Automatically follow selected accounts with a secondary account.

## Installation

### Prerequisites

- Python 3.8 or later
- Required libraries (install via `pip`)

### Clone the Repository
```bash
git clone https://github.com/your-username/instagram-account-manager.git
cd instagram-account-manager
```

### Install Dependencies
```bash
python3 -m pip install -r requirements.txt
```

### Setup

1. Ensure you have the correct version of Python installed.
2. Verify that your system has tkinter installed:
   ```bash
   python3 -m tkinter
   ```
3. Install [ChromeDriver](https://chromedriver.chromium.org/downloads) if using Selenium for additional automation.

## Usage

### Run the Application
```bash
python3 login_ui.py
```

### Workflow

1. **Primary Account Login**: Enter your credentials for the primary account.
2. **Fetch Data**: Automatically retrieves accounts that don't follow you back.
3. **Selection UI**: Choose which accounts to migrate using the provided checkbox UI.
4. **Secondary Account Login**: Enter your credentials for the secondary account.
5. **Migration**: Automatically follows the selected accounts with the secondary account.

### File Outputs

- `not_following_back.txt`: Contains accounts that don't follow you back.
- `selected_accounts.txt`: Contains accounts you chose to migrate.

## Project Structure

```plaintext
instagram-account-manager/
├── login_ui.py       # Handles user authentication and main workflow
├── fetch_data.py     # Fetches unfollowers from the primary account
├── migrate_follow.py # Migrates selected accounts to the secondary account
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new features, bug fixes, or enhancements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

