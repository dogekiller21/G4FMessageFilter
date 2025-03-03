# Run

Install uv

```bash
brew install uv
```

Run
```bash
uv run uvicorn app.main:app
```


Proceed to `http://127.0.0.1:8000`


# Stress test

Make sure you have `messages.db` in project root dir

Run
```bash
uv run stress_test.py
```