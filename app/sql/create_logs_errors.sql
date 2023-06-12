CREATE TABLE IF NOT EXISTS logs_errors(
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type_error TEXT,
    error TEXT)