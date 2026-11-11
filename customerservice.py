class Ticket:
    def __init__(self, name, category, issue, priority, status="Open"):
        self.id = None
        self.name = name
        self.category = category
        self.issue = issue
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class AIAssistant:
    """Simulates AI-powered triage, categorization, and response generation."""
    
    @staticmethod
    def triage_issue(issue_text):
        """Analyzes issue text to predict category and priority using intelligent heuristics."""
        text = issue_text.lower()
        
        # Determine Category
        if any(kw in text for kw in ["login", "password", "crash", "error", "bug", "freeze", "load", "access"]):
            category = "Technical"
        elif any(kw in text for kw in ["bill", "charge", "payment", "refund", "invoice", "subscription", "pricing"]):
            category = "Billing"
        elif any(kw in text for kw in ["account", "profile", "username", "settings", "deactivate"]):
            category = "Account"
        else:
            category = "General"
            
        # Determine Priority
        if any(kw in text for kw in ["urgent", "down", "emergency", "critical", "immediately", "broken"]):
            priority = "Urgent"
        elif any(kw in text for kw in ["fail", "error", "unable", "stuck", "issue"]):
            priority = "High"
        elif any(kw in text for kw in ["slow", "minor", "question", "help"]):
            priority = "Low"
        else:
            priority = "Medium"
            
        return category, priority

    @staticmethod
    def generate_response_draft(ticket):
        """Generates a contextual professional response draft based on the ticket details."""
        if ticket.category == "Technical":
            return (
                f"Dear {ticket.name},\n\n"
                f"We apologize for the inconvenience you are experiencing with '{ticket.issue}'. "
                f"Our engineering team has been alerted, and we are actively debugging the issue. "
                f"We will provide an update within 2 hours.\n\n"
                f"Best regards,\nTechnical Support Team"
            )
        elif ticket.category == "Billing":
            return (
                f"Dear {ticket.name},\n\n"
                f"Thank you for contacting us regarding your billing query: '{ticket.issue}'. "
                f"We are reviewing your transaction history and account logs to resolve this promptly. "
                f"We'll follow up with you shortly.\n\n"
                f"Best regards,\nBilling Support Team"
            )
        elif ticket.category == "Account":
            return (
                f"Dear {ticket.name},\n\n"
                f"We received your request regarding your account settings ('{ticket.issue}'). "
                f"For security purposes, we are verifying your account state and will guide you through the next steps.\n\n"
                f"Best regards,\nAccount Security Team"
            )
        else:
            return (
                f"Dear {ticket.name},\n\n"
                f"Thank you for reaching out about '{ticket.issue}'. We have logged your request and "
                f"are looking into it to ensure you receive a swift resolution.\n\n"
                f"Best regards,\nCustomer Support Team"
            )

class Customer_Support_System:
    def __init__(self):
        self.tickets = []
        self.counter = 1001

    def add_ticket(self, name, category, issue, priority):
        ticket = Ticket(name, category, issue, priority)
        ticket.id = self.counter
        self.tickets.append(ticket)
        self.counter += 1
        return ticket

    def view_all_tickets(self):
        if not self.tickets:
            print("No tickets found.\n")
            return
        print("\nID | Customer | Category | Issue | Priority | Status")
        print("-" * 65)
        for ticket in self.tickets:
            print(f"{ticket.id} | {ticket.name} | {ticket.category} | {ticket.issue} | {ticket.priority} | {ticket.status}")
        print()

    def find_ticket(self, id):
        for ticket in self.tickets:
            if ticket.id == id:
                return ticket
        return None

    def view_ticket(self, id):
        ticket = self.find_ticket(id)
        if ticket:
            print(f"\n--- Ticket #{ticket.id} ---")
            print(f"Customer name: {ticket.name}")
            print(f"Category: {ticket.category}")
            print(f"Issue: {ticket.issue}")
            print(f"Priority: {ticket.priority}")
            print(f"Status: {ticket.status}\n")
        else:
            print(f"Ticket {id} not found.\n")

    def update_status(self, id, new_status):
        ticket = self.find_ticket(id)
        if ticket:
            ticket.status = new_status
            print(f"Ticket {id} Updated Successfully. New status: {new_status}\n")
        else:
            print(f"Ticket {id} not found.\n")

    def filter_by_status(self, status):
        filtered = [t for t in self.tickets if t.status.lower() == status.lower()]
        if not filtered:
            print(f"No tickets found with status: '{status}'.\n")
            return
        print(f"\n--- Tickets with Status: {status} ---")
        print("ID | Customer | Category | Issue | Priority | Status")
        print("-" * 65)
        for ticket in filtered:
            print(f"{ticket.id} | {ticket.name} | {ticket.category} | {ticket.issue} | {ticket.priority} | {ticket.status}")
        print()

    def filter_by_priority(self, priority):
        filtered = [t for t in self.tickets if t.priority.lower() == priority.lower()]
        if not filtered:
            print(f"No tickets found with priority: '{priority}'.\n")
            return
        print(f"\n--- Tickets with Priority: {priority} ---")
        print("ID | Customer | Category | Issue | Priority | Status")
        print("-" * 65)
        for ticket in filtered:
            print(f"{ticket.id} | {ticket.name} | {ticket.category} | {ticket.issue} | {ticket.priority} | {ticket.status}")
        print()

    def run_ai_draft_for_ticket(self, id):
        ticket = self.find_ticket(id)
        if ticket:
            draft = AIAssistant.generate_response_draft(ticket)
            print(f"\n🤖 [AI Response Draft for Ticket #{ticket.id}]")
            print("=" * 60)
            print(draft)
            print("=" * 60 + "\n")
        else:
            print(f"Ticket {id} not found.\n")

if __name__ == "__main__":
    system = Customer_Support_System()
    system.add_ticket("Alice Smith", "Technical", "Login Failure", "High")
    system.add_ticket("Bob Jones", "Billing", "Unable to process payment", "Low")
    system.add_ticket("Charlie Cooper", "Technical", "System Freezing", "High")
    
    while True:
        try:
            option = int(input(
                "--- Customer Support System (with AI Assistant) ---\n"
                "1. Add a ticket (Manual or AI-Assisted)\n"
                "2. View a specific ticket\n"
                "3. View all tickets\n"
                "4. Update ticket status\n"
                "5. Filter tickets (Status/Priority)\n"
                "6. 🤖 Generate AI Response Draft for a Ticket\n"
                "7. Quit\n"
                "Enter your option (1-7): "
            ))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if option == 1:
            name = input("Enter the name of the customer: ").strip()
            issue = input("Enter the issue description: ").strip()
            
            # Ask if they want AI assistance for triage
            use_ai = input("Would you like AI to auto-assign category and priority? (y/n): ").strip().lower()
            
            if use_ai == 'y':
                category, priority = AIAssistant.triage_issue(issue)
                print(f"🤖 AI Triage Results -> Category: '{category}' | Priority: '{priority}'")
            else:
                category = input("Enter the category (Billing, Technical, Account, or General): ").strip()
                priority = input("Enter the priority (Low, Medium, High, or Urgent): ").strip()
                
            system.add_ticket(name, category, issue, priority)
            print("Ticket added successfully!\n")
            
        elif option == 2:
            try:
                ticket_id = int(input("Enter the ticket ID: ").strip())
                system.view_ticket(ticket_id)
            except ValueError:
                print("Invalid Ticket ID. Please enter a numeric ID.\n")
                
        elif option == 3:
            system.view_all_tickets()
            
        elif option == 4:
            try:
                ticket_id = int(input("Enter the Ticket ID to update: ").strip())
                new_status = input("Enter the new status (e.g., In Progress, Closed, Open): ").strip()
                system.update_status(ticket_id, new_status)
            except ValueError:
                print("Invalid Ticket ID. Please enter a numeric ID.\n")
                
        elif option == 5:
            filter_choice = input("Filter by (1) Status or (2) Priority? Enter 1 or 2: ").strip()
            if filter_choice == "1":
                status_query = input("Enter status to filter by (e.g., Open, Closed): ").strip()
                system.filter_by_status(status_query)
            elif filter_choice == "2":
                priority_query = input("Enter priority to filter by (e.g., Low, High, Urgent): ").strip()
                system.filter_by_priority(priority_query)
            else:
                print("Invalid choice. Returning to main menu.\n")
                
        elif option == 6:
            try:
                ticket_id = int(input("Enter the Ticket ID to generate an AI draft response for: ").strip())
                system.run_ai_draft_for_ticket(ticket_id)
            except ValueError:
                print("Invalid Ticket ID. Please enter a numeric ID.\n")
                
        elif option == 7:
            print("Goodbye!")
            break
            
        else:
            print("Invalid Option. Please choose between 1 and 7.\n")
