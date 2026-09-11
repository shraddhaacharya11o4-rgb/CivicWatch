# CivicWatch

## Smart Public Grievance and Infrastructure Monitoring System

CivicWatch is a web-based citizen grievance management platform developed using **Python and Django**. It provides a centralized system for citizens to report and track public issues, officers to manage and resolve grievances, and administrators to monitor departments, infrastructure, notifications, and feedback.

The platform also includes a **local AI-powered assistant** that helps citizens access information related to their grievances, assignments, updates, and notifications.

---

## Features

### Citizen Module

- Citizen registration and login
- Submit public grievances
- Select grievance categories
- Provide grievance location details
- Upload supporting documents/images
- Track grievance status
- View grievance updates
- View notifications
- Submit feedback
- Access AI Assistant
- Maintain chatbot conversation history

### Officer Module

- Officer login
- View grievances
- Assign grievances
- View assigned grievances
- Update grievance progress
- Add grievance updates
- Upload supporting images
- Change grievance status
- Resolve grievances

### Admin Module

- Admin login
- Manage departments
- Manage grievance categories
- Manage infrastructure assets
- Monitor infrastructure
- View grievances
- View grievance assignments
- View grievance updates
- Manage notifications
- View citizen feedback

---

## AI Assistant

CivicWatch includes a local AI-powered assistant for citizen support.

### Technologies Used

- **Ollama** – Runs the AI model locally
- **Llama 3.2** – Generates AI responses
- **Django** – Backend integration
- **AJAX** – Sends messages without refreshing the page
- **Django Sessions** – Maintains user information and conversation history

The AI Assistant can help citizens with:

- Grievance status
- Grievance details
- Assigned officer
- Department information
- Grievance updates
- Expected resolution information
- Notifications

The assistant uses the logged-in citizen's CivicWatch records to provide relevant information.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| HTML5 | Page structure |
| CSS3 | User interface |
| JavaScript | Client-side functionality |
| AJAX | Asynchronous communication |
| SQLite | Database |
| Ollama | Local AI runtime |
| Llama 3.2 | AI language model |
| Git | Version control |
| GitHub | Source code management |

---

## Grievance Workflow

```text
Citizen
   ↓
Submit Grievance
   ↓
Officer Assignment
   ↓
In Progress
   ↓
Grievance Updates
   ↓
Resolved
   ↓
Citizen Notification
   ↓
Citizen Feedback


**`Project Structure`** 

CivicWatch/
├── govt/
├── public/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── chatbot.py
│   ├── models.py
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

## Project Status

**Completed**