# 📈 Stock Recommendation POC

This project implements a local proof-of-concept stock recommendation system. It collects stock prices for the "Magnificent Seven" companies at 5-minute intervals, stores them in a local SQLite database, and exposes an API that analyzes whether a stock matches the "cup and handle" pattern.

---

## 🚀 Features

- Local data collection with 5-minute sampling during U.S. trading hours
- Pattern detection API (`/analyze?ticker=XYZ`)
- SQLite-based storage with 3-day data retention
- Fully local — no cloud resources involved
- Modular architecture (separated core/API/scheduler/utilities)

---

## 🏗 Directory Structure

```
src/
├── api/              # FastAPI application
├── core/             # Data collection & database logic
├── scheduler/        # Price polling loop
├── utilities/        # Time functions & constants
├── tests/            # (Optional) testing scripts
├── run.py            # Main entry point to launch the system
```

---

## 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/roiesu/stock-recommendation.git
cd stock-recommendation

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

---

## ▶️ Running the system

To launch both the API server and the scheduler:

```bash
python run.py
```

This will:
- Start FastAPI on `http://127.0.0.1:8000`
- Start a scheduler that collects prices every 5 minutes (only during U.S. trading hours)

---

## 📡 API Usage

```http
GET /analyze?ticker=AAPL
```

Returns:

```json
{
  "ticker": "AAPL",
  "match": true
}
```

---

## 🛠 Configuration

Basic configuration is set in `utilities/constants.py`:

- `TICKERS`: The tracked stocks
- `DB_PATH`: SQLite database location
- `DEV_MODE`: Enables development behavior (e.g., disables trading hours check)

---

## ⚠️ Disclaimer

This project is a technical prototype only.  
It is not intended for financial decision-making or real-world trading.

---

## 📬 Feedback & Contributions

Pull requests are welcome.  
Feel free to fork and customize the system for your own use cases.
