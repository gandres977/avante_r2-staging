from datetime import datetime, timezone

utcnow = datetime.now(tz=timezone.utc)
print(utcnow.strftime("%Y%m%d_%H%M%SZ"))