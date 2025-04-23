from datetime import datetime

def get_current_time(_: str = "") -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"現在の時刻は {now} です"

print(get_current_time())