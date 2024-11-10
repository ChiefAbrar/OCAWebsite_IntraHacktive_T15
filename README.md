# OCAWebsite_IntraHacktive_T15
# Dynamic System for BRAC University's Office of Co-curricular Activities (OCA)

## Project Overview
The goal of this system is to streamline the coordination between BRAC University’s Office of Co-Curricular Activities (OCA) and club panel members. By addressing key pain points such as event management delays, communication inefficiencies, room booking struggles, and budget approval transparency, this dynamic system aims to improve overall efficiency and transparency, while providing data-driven insights for better decision-making.

## Features Implemented
1. **Event Management System**:
   - A digital form for event submission, approval tracking, and status updates.
   - Centralized system for OCA to approve, request additional information, or reject events.

2. **Room Booking System**:
   - Real-time availability checking for rooms.
   - Instant room booking confirmations and easy rescheduling options.
   - Conflict detection to prevent double bookings.

3. **Budget Approval Tracking**:
   - Digital submission of budget requests and approvals.
   - Transparent tracking of budget status and approval history.
   - Automated notifications for approval/rejection decisions.

4. **Communication Module**:
   - Messaging system for direct communication between OCA and club members.
   - Record of all communication related to events, room bookings, and budget requests.

5. **Data-Driven Insights**:
   - Automated reporting of event participation, budget usage, and room bookings.
   - Visualized metrics and performance analytics for both OCA and club leaders.

## Technical Stack and Architecture
- **Frontend**: HTML, CSS.
- **Backend**: Python (Flask), Java(Servlet).
- **Database**: MySQL for managing events, room bookings, budget requests, and communications
- **Libraries & Tools**:
  - **Flask**: Lightweight web framework for backend operations.
  - **SQLAlchemy**: ORM for handling database models and queries.
  - **Spring Boot**: To eliminate the need for complex XML configurations and reduces boilerplate code.

### System Architecture:
1. **Frontend**: Handles user interactions, form submissions, and data display.
2. **Backend**: Manages user authentication, data processing, and communication with the database.
3. **Database**: Stores event details, room availability, budget requests, communications, and reports.

## User Guide
### Setup Instructions:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ChiefAbrar/OCAWebsite_IntraHacktive_T15.git
2. Install Python Dependencies:
    ```bash
    pip install -r requirements.txt
3. Set Up MySQL Database:
    1. Ensure that you have MySQL installed and set up a database for the project.
    2. Create a database (e.g., oca_management) and import the schema.
    3. Configure the database connection details in the config.py file:
        ```python
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://username:password@localhost:port/oca_management_system")
4. Run the Application:
    To start the server, run the Flask application:
        ```python
        python app.py
    Visit (the link provided in the terminal) in your browser to access the system.
## Troubleshooting:
    1. Database Connection Issues: If you encounter database connection errors, ensure that your MySQL server is running and the connection details in config.py are correct.
    Missing Dependencies: If any dependencies are missing after installation, run:
        ```python
        pip install -r requirements.txt

## Challenges and Solutions
1. **Room Booking Conflict Resolution**:
Challenge: Ensuring real-time room availability and preventing double bookings.
Solution: Implemented a dynamic room availability checker using MySQL and an immediate conflict detection system.
2. **Data Integrity in Budget Tracking**:
Challenge: Ensuring that budget requests are accurately tracked and approvals are transparent.
Solution: Utilized a database schema that links budget requests to events and provides a clear approval history with timestamps.
3. **Communication Efficiency**:
Challenge: Fragmented communication leading to missed updates.
Solution: Developed a centralized messaging system that logs all communications and ensures timely notifications.
## Future Enhancements(if given more time)
**Mobile App Integration**: Implement a mobile-friendly version of the system or a dedicated mobile app for easier access on the go.
**Advanced Reporting**: Add more advanced reporting features, including financial forecasting and performance predictions for future events.
**User Roles**: Implement different access levels for OCA staff, club panel members, and event attendees, allowing for tailored views and permissions.
**Making the System More Efficient**: Fixing bugs existing in the system and make it better.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
