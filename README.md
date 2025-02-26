# LeetBatch

LeetBatch is an automation tool for handling LeetCode submissions. The project is structured into four main layers: Database, Business Logic, Presentation, and Configuration.

## Features

- **Submit Single Question**: Submit a solution to a specific LeetCode problem using the API.
- **Submit Multiple Questions**: Submit solutions for all problems in the `QUESTION_MAPPING` and store the results in a CSV file.
- **Automated Result Parsing**: Retrieve and parse submission results, including status, runtime, memory usage, and error messages if any.
- **Flexible Language Support**: Supports multiple programming languages like Python, Java, C++, and etc.

## Requirements

- Python 3.7+
- FastAPI
- Playwright
- CSV for result storage
- A `.env` file with your LeetCode credentials
- Get cookie information after logging in to LeetCode
- QUESTION_MAPPING and LANG_MAPPING settings

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/EdwardShiung/LeetBatch.git
    cd leetcode_submission
    ```
2. Setup a virtual environment**

    It is recommended to use a virtual environment to manage your project dependencies.

    - For MacOS/Linux, run:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    - For Windows, run:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    This will create and activate the virtual environment for your project.


3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Playwright:
    ```bash
    playwright install
    ```

5. Create a `.env` file and add your LeetCode credentials:
    ```
    LEETCODE_USERNAME=your_username
    LEETCODE_PASSWORD=your_password
    ```

6. Configure any additional settings in `config/settings.py` if needed (e.g., `DATA_FOLDER`).

## Organizing Your LeetCode Solutions

Please organize your LeetCode solutions in the following way:
- Create a folder named `leetcode_solutions` inside the `db/` directory.
- Inside the `leetcode_solutions` folder, save each solution in a separate file named as `leetcode_{question_id}.{language_extension}`, for example:
  - `leetcode_1.py` for a Python solution to the problem with ID 1.
  - `leetcode_3.java` for a Java solution to the problem with ID 3.

### Setting up `data_mappings.py`

You need to configure the `QUESTION_MAPPING` and `LANG_MAPPING` in the `db/data_mappings.py` file as follows:

```python
QUESTION_MAPPING = {
    1: "two-sum",
    3: "add-two-numbers",
    4: "median-of-two-sorted-arrays"
}

LANG_MAPPING = {
    "py": "python3",
    "java": "java",
    "cpp": "cpp",
    "js": "javascript"
}
```

- **`QUESTION_MAPPING`**: A dictionary that maps LeetCode question IDs to their respective problem names (slugs).
- **`LANG_MAPPING`**: A dictionary that maps programming language shortcuts to LeetCode's supported language codes.

## Cookies Setup

LeetCode requires you to have a valid session for submitting problems. After logging into your LeetCode account, you need to grab the session cookies and store them in a file called `cookies.json`.

Here is an example of the structure of `cookies.json`:

```json
[
    {
        "name": "LEETCODE_SESSION",
        "value": "your_session_value_here",
        "domain": ".leetcode.com",
        "path": "/",
        "httpOnly": true,
        "secure": true
    },
    {
        "name": "csrftoken",
        "value": "your_csrftoken_value_here",
        "domain": ".leetcode.com",
        "path": "/",
        "httpOnly": true,
        "secure": true
    }
]
```

### Instructions:
1. **Locate `LEETCODE_SESSION` and `csrftoken`** in your browser's developer tools while logged into LeetCode.
2. Copy the `value` fields of these cookies and paste them into the respective fields in the `cookies.json` file.
3. Make sure this file is placed in the root directory of your project for automatic usage during submissions.

## How to Run

To run the FastAPI server:

```bash
uvicorn presentation.main:app --reload
```

### Submit a Single Question
Use the following endpoint to submit a single LeetCode problem:

**Endpoint**: `/api/submit/{question_id}`

**Example**:
```bash
curl -X GET "http://127.0.0.1:8000/api/submit/1"
```

### Submit Multiple Questions
Use the following endpoint to submit all questions in the `QUESTION_MAPPING`:

**Endpoint**: `/api/submit_multi_questions`

**Example**:
```bash
curl -X GET "http://127.0.0.1:8000/api/submit_multi_questions"
```

This will submit all the problems listed in `QUESTION_MAPPING` and save the results to a CSV file.


## Directory Structure

```plaintext
leetcode_submit/
│── db/                             # 📂 Reserved for the database layer (for future use)
│   ├── models/                     # ORM database model structures
│   ├── migrations/                 # Database migrations (if needed in the future)
│   ├── data_mappings.py            # Reserved for database connection setup
│   ├── leetcode_solutions          # 🚩 Put your LeeCode solutions to here!!
│
│── logic/                          # 📂 Business logic layer
│   ├── leetcode/                   # Logic specific to LeetCode interactions
│   │   ├── submit_manager.py       # Manages code submission and result checking
│   │   ├── login_manager.py        # Manages LeetCode login and cookies
│   │   ├── language_manager.py     # Handles programming language selection
│   │   ├── result_parser.py        # Parses the submission result
│   ├── file_manager.py             # File management and manipulation
│
│── presentation/                   # 📂 Presentation layer (FastAPI)
│   ├── api/                        # FastAPI routing configuration
│   │   ├── routes.py               # Defines the API endpoints
│   │   ├── schemas.py              # FastAPI request/response schemas
│   ├── main.py                     # 🚩 FastAPI server entry point
│
│── config/                         # 📂 Configuration layer
│   ├── settings.py                 # Reads the `.env` configuration file
│
│── tests/                          # 📂 Testing Directory
│   ├── functional/                 # 📂 General Testing (Business Logic)
│   │   ├── test_config.py          # Test config/settings.py
│   │   ├── test_login.py           # Test login_manager.py
│   │   ├── test_submit_manager.py  # Test submission function
│   │   ├── test_result_parser.py   # Test result parser
│   │
│   ├── api/                        # 📂 API Testing
│   │   ├── test_routes.py          # Test FastAPI (Unit Testing)
│   │   ├── test_integration.py     # Test API Integration Testing (Integration Testing)
│   │
│   ├── conftest.py                 # Pytest Setting
│
│── .env                            # ✅ Environment variables (LeetCode API keys & account)
│── .gitignore                      # ✅ Ignored sensitive information
│── requirements.txt                # ✅ List of dependencies (FastAPI, Playwright)
│── cookies.json                    # ✅ Playwright Session Cookies
│── pytest.ini                      # ✅ Pytesting Setting (Avoid to use PYTHONPATH mannually) 


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.