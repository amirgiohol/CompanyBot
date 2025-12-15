from data import courses

def get_categories():
    return list(courses.keys())

def get_courses_by_category(category):
    return courses.get(category, [])

def get_course_by_id(category, course_id):
    for course in get_courses_by_category(category):
        if course["id"] == course_id:
            return course
    return None

def get_free_courses():
    free = []
    for cat in courses:
        for c in courses[cat]:
            if c["price"] == 0:
                free.append((cat, c))
    return free
