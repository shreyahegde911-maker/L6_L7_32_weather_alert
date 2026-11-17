import math

def parse_reading(text):
    try:
        if not isinstance(text, str):
            return None

        parts = text.split('/')
        if len(parts) != 2:
            return None

        temp = float(parts[0])
        humidity = int(parts[1])

        if not math.isfinite(temp):
            return None
        if not 0 <= humidity <= 100:
            return None

        return temp, humidity

    except (ValueError, TypeError):
        return None


def wind_category(speed_text):
    try:
        speed = int(speed_text)

        if speed < 0:
            return None
        if speed >= 89:
            return 'warning'
        if speed >= 39:
            return 'advisory'
        return 'none'

    except (ValueError, TypeError):
        return None


def rainfall_spread(readings_csv):
    try:
        if not isinstance(readings_csv, str):
            return None

        readings = [float(r.strip()) for r in readings_csv.split(',')]

        if not readings or not all(math.isfinite(r) for r in readings):
            return None
        if any(r < 0 for r in readings):
            return None

        return max(readings) - min(readings)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")
    result = parse_reading(user_input)
    print("Temperature and Humidity:", result)

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")
    result = wind_category(user_input)
    print("Wind Category:", result)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")
    result = rainfall_spread(user_input)
    print("Rainfall Spread:", result)


if __name__ == "__main__":
    main()
