# Battery Monitor
A Python script that monitors your laptop's battery status and sends notifications based on its charge level. This tool helps you keep track of your battery percentage and charging status, ensuring you never run out of battery unexpectedly.

Features
Real-time Battery Monitoring: Continuously checks the battery percentage.
Notifications: Alerts you when:
Battery is low (≤ 25%).
Charging starts and stops.
Battery reaches 100% charge.
Battery percentage is at critical levels (like ≤ 50%).
User-friendly Interface: Outputs user and battery information clearly.
Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x
Necessary libraries:
plyer
psutil
You can install the required libraries using pip:

bash
Copy code
pip install plyer psutil
Usage
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/shadrach098/battery-monitor.git
cd battery-monitor
Run the script:

bash
Copy code
python battery_monitor.py
The script will begin monitoring your battery status. Notifications will pop up based on the conditions defined in the code.

Code Explanation
The main function batteryC() performs the following tasks:

Initializes counters and retrieves the current battery percentage.
Continuously checks the battery status and sends notifications for different conditions:
Low battery warning
Charging status changes
Full charge notifications
Example Notification Messages
Low Battery: "Hi [User], You Have [x]% Battery remaining. Please Charge."
Charging Started: "Hi [User], Laptop Is Charging. You Have [x]% Battery remaining."
Charge Complete: "Hi [User], Charging Completed. Battery is 100% fully Charged."
Contribution
Feel free to contribute by submitting issues or pull requests.
