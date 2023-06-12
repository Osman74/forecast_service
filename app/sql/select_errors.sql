SELECT * FROM logs_errors
WHERE  (((julianday(datetime('now', 'localtime'))) - julianday((timestamp))) * 1440.0) < 10