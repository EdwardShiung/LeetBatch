# LeetBatch

LeetBatch is an automation tool for handling LeetCode submissions. The project is structured into four main layers: Database, Business Logic, Presentation, and Configuration.

## Directory Structure

```plaintext
leetcode_submit/
│── db/                        # 📂 Reserved for the database layer (for future use)
│   ├── models/                # ORM database model structures
│   ├── migrations/            # Database migrations (if needed in the future)
│   ├── database.py            # Reserved for database connection setup
│
│── logic/                     # 📂 Business logic layer
│   ├── leetcode/              # Logic specific to LeetCode interactions
│   │   ├── api_client.py      # Interacts with LeetCode via Playwright
│   │   ├── submit_manager.py  # Manages code submission and result checking
│   │   ├── login_manager.py   # Manages LeetCode login and cookies
│   │   ├── language_manager.py # Handles programming language selection
│   │   ├── result_parser.py   # Parses the submission result
│
│── presentation/              # 📂 Presentation layer (FastAPI)
│   ├── api/                   # FastAPI routing configuration
│   │   ├── routes.py          # Defines the API endpoints
│   │   ├── schemas.py         # FastAPI request/response schemas
│   ├── main.py                # FastAPI server entry point
│
│── config/                    # 📂 Configuration layer
│   ├── settings.py            # Reads the `.env` configuration file
│
│── .env                       # ✅ Environment variables (LeetCode API keys & account)
│── .gitignore                 # ✅ Ignored sensitive information
│── requirements.txt           # ✅ List of dependencies (FastAPI, Playwright)
│── cookies.json               # ✅ Playwright Session Cookies
