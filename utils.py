from data import courses

def get_categories():
    return list(courses.keys())

def get_courses_by_category(category):
    return courses.get(category, [])

def get_course_by_id(category, course_id):
    for course in courses.get(category, []):
        if course["id"] == course_id:
            return course
    return None
