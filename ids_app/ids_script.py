import time
import random
from prometheus_client import start_http_server, Counter

# Create a Prometheus Counter metric
# This will count the total number of failed logins
FAILED_LOGINS = Counter('failed_logins_total', 'Total number of failed login attempts')


def simulate_login_attempts():
    """Simulates user login attempts indefinitely."""
    print("Starting IDS simulation... Exposing metrics at http://localhost:8000")

    while True:
        # Simulate a random login attempt
        time.sleep(random.uniform(1, 5))  # Wait 1–5 seconds

        attempt_type = random.choice(["SUCCESS", "FAILURE", "SUCCESS", "SUCCESS"])  # Skew towards success

        if attempt_type == "FAILURE":
            user = random.choice(["admin", "root", "user123", "guest"])
            ip = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"

            # Log to console
            print(f"ALERT: Failed login detected! User: '{user}', IP: {ip}")

            # Increment the Prometheus counter
            FAILED_LOGINS.inc()
        else:
            print("Login attempt: SUCCESS")


if __name__ == '__main__':
    # Start an HTTP server to expose the /metrics endpoint on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000.")

    # Start the simulation
    simulate_login_attempts()
