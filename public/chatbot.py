import ollama

from .models import grievance
from .models import grievanceassignment
from .models import grievanceupdate
from .models import notification


def get_grievance_data(username):

    grievances = grievance.objects.filter(citizen=username)

    grievance_data = ""

    for g in grievances:

        grievance_data += (
            "Grievance ID: " + g.grievance_id + "\n"
            "Title: " + g.title + "\n"
            "Description: " + g.description + "\n"
            "Location: " + g.location + "\n"
            "Priority: " + g.priority + "\n"
            "Status: " + g.status + "\n"
            "Submission Date: " + g.submission_date + "\n"
        )

    return grievance_data


def get_assignment_update_data(username):

    grievances = grievance.objects.filter(citizen=username)

    data = ""

    for g in grievances:

        assignment = grievanceassignment.objects.filter(
            grievance=g.grievance_id
        ).first()

        updates = grievanceupdate.objects.filter(
            grievance=g.grievance_id
        ).order_by('-id')

        if assignment:

            data += (
                "Grievance ID: " + g.grievance_id + "\n"
                "Assigned Officer: " + assignment.assigned_officer + "\n"
                "Department: " + assignment.department + "\n"
                "Assigned Date: " + assignment.assigned_date + "\n"
                "Expected Resolution Date: " + assignment.expected_resolution_date + "\n"
                "Assignment Status: " + assignment.status + "\n"
            )

        for update in updates:

            data += (
                "Grievance Update:\n"
                "Update Date: " + update.update_date + "\n"
                "Officer: " + update.officer + "\n"
                "Description: " + update.description + "\n"
                "Update Status: " + update.status + "\n"
            )

        data += "\n"

    return data


def get_notification_data(username):

    notifications = notification.objects.filter(
        user=username
    ).order_by('-id')

    notification_data = ""

    for n in notifications:

        notification_data += (
            "Notification Title: " + n.title + "\n"
            "Message: " + n.message + "\n"
            "Notification Date: " + n.notification_date + "\n"
            "Priority: " + n.priority + "\n\n"
        )

    return notification_data


def get_ai_response(username, user_message, chat_history):

    grievance_data = get_grievance_data(username)
    notification_data = get_notification_data(username)
    assignment_update_data = get_assignment_update_data(username)

    messages = [
        {
            'role': 'system',
            'content': '''
            You are CivicWatch AI Assistant.

            Answer the user's question using the CivicWatch
            information provided to you.

            Keep answers short and clear.
            Use simple language.
            Do not make up information.

            If the user mentions a specific grievance ID,
            use only the information related to that grievance ID.

            If the user does not mention a grievance ID,
            use the relevant information from the user's grievances.
            
            Do not use or mention CivicWatch records for simple greetings,
            thanks, or casual conversation unless the user asks about their records.

            For greetings such as "Hello", "Hi", or "Good morning",
            respond with a simple friendly greeting.

            For messages such as "Thank you" or "Thanks",
            respond politely without mentioning grievance records.

            Only provide grievance, notification, assignment, or update
            information when the user's question is related to those records.

            Do not mix information from different grievances.

            Use the conversation history to understand
            words like "it", "this grievance", "that complaint",
            "he", or "they".
            '''
        }
    ]

    messages.extend(chat_history)

    messages.append({
        'role': 'user',
        'content': (
            "CivicWatch grievance data:\n\n"
            + grievance_data
            + "\nCivicWatch notification data:\n\n"
            + notification_data
            + "\nCivicWatch assignment and update data:\n\n"
            + assignment_update_data
            + "\nUser's question:\n"
            + user_message
        )
    })

    response = ollama.chat(
        model='llama3.2',
        messages=messages
    )

    return response['message']['content']