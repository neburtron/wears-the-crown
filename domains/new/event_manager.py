import src.commands as commands

class EventManager:

    def __init__(self, events):
        self.events = []
        for event in events:
            self.events.append(event)
        self.process_events()
        
    def process_events(self):
        for event in self.events:
            contents = commands.load_json(event['file_name'])
            event_type = contents.get('type')

            # Ensure the method exists before calling it
            if hasattr(self, event_type):
                method = getattr(self, event_type)
                method(contents)
            else:
                print(f"No method found for event type: {event_type}")

    def event1(self, contents):
        print("Running event: Test1")

    def event2(self, contents):
        print("Running event: Test2")

    def event3(self, contents):
        print("Running event: Test3")

    def event4(self, contents):
        print("Running event: Test4")
        
        