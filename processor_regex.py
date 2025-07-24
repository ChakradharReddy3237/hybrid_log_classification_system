import re

def classify_with_regex(log_message):
    regex_patterns = {
        # User Actions
        r"User User\d+ logged (in|out)\.": "User Action",
        r"Account with ID \d+ created by User\d+\.": "User Action",
        r"System reboot initiated by user User\d+\." : "System Notification",

        # System Notifications
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully\.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .*\.csv uploaded successfully by user User\d+\.": "System Notification",
        r"Disk cleanup completed successfully\.": "System Notification",

        # Security Alerts
        r"Multiple (bad login attempts|login failures).*": "Security Alert",
        r"Unauthorized (login attempt|API request).*": "Security Alert",
        r"User \d+ tried to bypass API security.*": "Security Alert",
        r"Potential security threat.*": "Security Alert",
        r"Anomalous activity identified.*": "Security Alert",
        r"Server \d+ experienced potential security incident.*": "Security Alert",

        # Admin Privilege Escalations
        r"escalated (admin )?privileges.*": "Security Alert",
        r"Admin privilege escalation.*": "Security Alert",
        r"Elevation of admin privileges detected.*": "Security Alert",
        r"Privilege elevation detected.*": "Security Alert",

        # Errors
        r"Shard \d+ replication task .* failure": "Error",
        r"Data replication task .* failed": "Error",
        r"Replication of data .* failed": "Error",
        r"kernel panic": "Critical Error",
        r"kernel (issue|failure|malfunction)": "Critical Error",
        r"Boot process .* kernel .*": "Critical Error",
        r"Lead conversion failed.*": "Error",
        r"Attempt to access account .* was not authorized": "Security Alert",
        r"Unrecoverable issue found in .*": "Critical Error",
        r"Non-recoverable fault detected in .*": "Critical Error",

        # SSL Issues
        r"SSL certificate .* failed": "Error",
        r"Invalid SSL certificate.*": "Error",
        r"expired SSL certificate": "Error",

        # Configuration Issues
        r"System configuration .* invalid": "Error",
        r"Configuration .* corrupted.*": "Error",
        r"Cross-system configuration failure.*": "Error",
        r"Configuration malfunction.*": "Error",

        # Deprecated APIs
        r"API endpoint .* is deprecated.*": "System Notification",

        # Resource Logs (Optional - Can be ignored or set as Info)
        r"Final resource view:.*": "Resource Usage",
        r"Total usable vcpus.*": "Resource Usage",

        # HTTP Status (Nova logs)
        r'nova\.osapi_compute\.wsgi\.server .*"GET .* HTTP.*status.*200.*"': "HTTP Status",
        r'nova\.osapi_compute\.wsgi\.server .*Return code: 200.*': "HTTP Status",
        r'nova\.osapi_compute\.wsgi\.server .*RCODE\s+200.*': "HTTP Status",

        # Resource Claim Logs
        r'nova\.compute\.claims.*Total memory.*': "Resource Usage",
        r'nova\.compute\.claims.*memory limit.*': "Resource Usage",
        r'nova\.compute\.claims.*vcpu limit.*': "Resource Usage",
        r'nova\.compute\.claims.*disk limit.*': "Resource Usage",
    }

    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None  # if no match found

if __name__ == "__main__":
    log_messages = [
        "User User123 logged in.",
        "Backup started at 2023-10-01 12:00:00.",
        "Multiple bad login attempts detected.",
        "SSL certificate validation failed.",
        "System configuration invalid for module X.",
        "Hey Bro, chill ya!"
    ]

    for message in log_messages:
        classification = classify_with_regex(message)
        print(f"Log Message: {message}\nClassification: {classification}\n")
