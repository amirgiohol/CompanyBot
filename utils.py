from data import courses

def get_categories():
    return sorted(courses.keys())

def get_courses_by_category(category):
    return courses.get(category, [])

def get_course_by_id(category, course_id):
    for c in courses.get(category, []):
        if c["id"] == course_id:
            return c
    return None

def get_free_courses():
    free = []
    for cat, course_list in courses.items():
        for c in course_list:
            if c["price"] == 0:
                free.append((cat, c))
    return free
