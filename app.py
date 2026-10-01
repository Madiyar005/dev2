class AttendanceTracker:
    def __init__(self):
        self.records = {}

    def add_record(self, student_name, is_present):
        self.records[student_name] = is_present
        return True

    def get_attendance(self, student_name):
        return self.records.get(student_name, None)