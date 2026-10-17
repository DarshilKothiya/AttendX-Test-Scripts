
import unittest

def mark_attendance(student_id, status):
    if student_id and status in ["Present", "Absent"]:
        return "Attendance marked successfully"
    return "Invalid attendance details"

class AttendanceTest(unittest.TestCase):
    def test_mark_present(self):
        self.assertEqual(
            mark_attendance("STU101", "Present"),
            "Attendance marked successfully"
        )

    def test_invalid_status(self):
        self.assertEqual(
            mark_attendance("STU101", "Late"),
            "Invalid attendance details"
        )

if __name__ == "__main__":
    unittest.main()
