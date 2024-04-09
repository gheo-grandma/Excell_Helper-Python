def prettify_course(course_name):
    # semplifica nome del corso togliendo tutto ciò che c'è dopo la '('
    
    stop = len(course_name)
    
    for i in range(len(course_name)):
        if course_name[i] == '(':
            stop = i - 1
            
    return course_name[:stop]