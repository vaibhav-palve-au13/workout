def courses_to_take(course_to_prereqs):
    return (sorted(courses.keys()))
    
courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']