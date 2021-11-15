import textract


def extract_data(file):
    # setting up the blanks for the if statement below, if i were paid it'd be neater
    # these were originally set up as test variables so it wouldn't constantly be saving and
    # returning to the database - leaving these until i finish this concept out so i know
    # just how far i've gotten and how far i've got left.
    # title = instructor_name = instructor_phone = instructor_email = ta_name = ""
    # ta_email = course_site = course_time = office_hours = course_description = ""
    # course_objectives = prereqs = textbook = instruct_methods = ""

    # ok, now onto the REAL magic
    extracted_data = {}
    syllabus = textract.process(file).decode("utf-8")
    split_syllabus = [line for line in syllabus.splitlines() if line.split() != []]
    for line in range(len(split_syllabus)):
        # for each split_syllabus[line] in the list of strings from the PDF, check whether the appropriate
        # field has been accounted for in the dictionary of syllabus value yet, and if not check certain
        # contents of each split_syllabus[line] depending on what info needs to be accounted for and add
        # as the element to the dictionary to send back as the data package to insert into the syllabus database
        if "title" not in extracted_data:  # if course identifier hasn't been found yet
            if split_syllabus[line].startswith("IS", 0, 7):
                # 7 is the max length of the course identifier - IS 432L (if that exists)
                extracted_data["title"] = split_syllabus[line]
            elif (split_syllabus[line].startswith("ENCH", 0, 9) or split_syllabus[line].startswith("CMSC", 0, 9) or
                  split_syllabus[line].startswith("CMPE", 0, 9) or split_syllabus[line].startswith("DATA", 0, 9) or
                  split_syllabus[line].startswith("ENEE", 0, 9) or split_syllabus[line].startswith("ENME", 0, 9) or
                  split_syllabus[line].startswith("ENES", 0, 9)):
                extracted_data["title"] = split_syllabus[line]
        if "instructor_name" not in extracted_data:
            if split_syllabus[line].casefold().startswith("dr") or split_syllabus[line].casefold().startswith("prof"):
                extracted_data["instructor_name"] = split_syllabus[line]
            elif split_syllabus[line].casefold().startswith("instructor"):
                extracted_data["instructor_name"] = split_syllabus[line].strip("Instructor")
        if "instructor_phone" not in extracted_data:
            if "Phone:" in split_syllabus[line] and "instructor_name" in extracted_data:
                extracted_data["instructor_phone"] = split_syllabus[line].strip("Phone: ")
        if "instructor_email" not in extracted_data:
            if "Email:" in split_syllabus[line]:
                extracted_data["instructor_email"] = split_syllabus[line].strip("Email: ")
            elif "E-mail:" in split_syllabus[line]:
                extracted_data["instructor_email"] = split_syllabus[line].strip("E-mail: ")
        if "ta_name" not in extracted_data:
            # if "@umbc.edu" in split_syllabus[line] and "instructor_email" in extracted_data:
            #     extracted_data["ta_email"] = split_syllabus[line]
            # elif ("course_time" not in extracted_data and len(split_syllabus[line].split()) >= 2 and len(
            #         re.findall('\b[A-Z].*?\b', split_syllabus[line])) >= 2):
            #     extracted_data["ta_name"] = split_syllabus[line]
            if "ta:" in split_syllabus[line].casefold() or "teaching fellow" in split_syllabus[line - 1]:
                extracted_data["ta_name"] = split_syllabus[line]
        if "ta_email" not in extracted_data and "instructor_email" in extracted_data:
            if "@umbc.edu" in split_syllabus[line]:
                extracted_data["ta_email"] = split_syllabus[line]
        if "course_site" not in extracted_data:
            if "course" in split_syllabus[line - 1].casefold() and \
                    "site" in split_syllabus[line].casefold() and \
                    "http://" in split_syllabus[line]:
                extracted_data["course_site"] = split_syllabus[line].split('http://', 1)[1]
            elif "course" in split_syllabus[line - 1].casefold() and \
                    "site" in split_syllabus[line].casefold() and \
                    "https://" in split_syllabus[line]:
                extracted_data["course_site"] = split_syllabus[line].split('https://', 1)[1]
        if "office_hours" not in extracted_data:
            if "office hours" in split_syllabus[line].casefold():
                extracted_data["office_hours"] = split_syllabus[line].casefold().split('office hours:', 1)[1].split(',', 1)[0].title()
        if "course_time" not in extracted_data:
            if "lecture" in split_syllabus[line].casefold():
                extracted_data["course_time"] = split_syllabus[line]
        # course description not perfect due to it being multiline
        if "course_description" not in extracted_data:
            if "course description" in split_syllabus[line - 1].casefold():
                course_description = split_syllabus[line]
                for descript_line in range(1, 5):
                    if split_syllabus[line + descript_line] == split_syllabus[line + descript_line].casefold():
                        course_description += split_syllabus[line + descript_line]
                extracted_data["course_description"] = course_description
        if "course_objectives" not in extracted_data:
            if "course objectives" in split_syllabus[line - 1].casefold():
                course_objs = split_syllabus[line]
                for object_line in range(0, 5):
                    try:
                        if split_syllabus[line + object_line][0] == split_syllabus[line][0]:
                            course_objs += split_syllabus[line + object_line]
                        elif type(int(split_syllabus[line + object_line][0])) is int and \
                                split_syllabus[line + object_line][0] == (int(split_syllabus[line][0]) + 1):
                            course_objs += split_syllabus[line + object_line]
                    except ValueError:
                        pass
                extracted_data["course_objectives"] = course_objs
        if "prereqs" not in extracted_data:
            if "prerequisite" in split_syllabus[line - 1].casefold():
                extracted_data["prereqs"] = split_syllabus[line]
        if "textbook" not in extracted_data:
            if "textbook" in split_syllabus[line - 1].casefold() in split_syllabus[line]:
                extracted_data["textbook"] = split_syllabus[line]
        if "instruct_methods" not in extracted_data:
            if "instructional methods" in split_syllabus[line - 1].casefold():
                extracted_data["instruct_methods"] = split_syllabus[line]
        if "attendance_rule" not in extracted_data:
            if "attendance" in split_syllabus[line - 1].casefold():
                extracted_data["attendance_rule"] = split_syllabus[line]
        if "class_preparation" not in extracted_data:
            if "preparation" in split_syllabus[line - 1].casefold() or \
                    "preparedness" in split_syllabus[line - 1].casefold():
                extracted_data["class_preparation"] = split_syllabus[line]
        if "course_requirements" not in extracted_data:
            if "course requirements" in split_syllabus[line - 1].casefold():
                extracted_data["course_requirements"] = split_syllabus[line]
        if "grade_breakdown" not in extracted_data:
            if "grading" in split_syllabus[line - 1].casefold():
                extracted_data["grade_breakdown"] = split_syllabus[line]
        if "quizzes" not in extracted_data:
            if "quizzes" in split_syllabus[line - 1].casefold():
                extracted_data["quizzes"] = split_syllabus[line]
        if "exams" not in extracted_data:
            if "exams" in split_syllabus[line - 1].casefold():
                extracted_data["exams"] = split_syllabus[line]
        if "prog_assignments" not in extracted_data:
            if "programming" in split_syllabus[line - 1].casefold() or \
                    "projects" in split_syllabus[line - 1].casefold():
                extracted_data["prog_assignments"] = split_syllabus[line]
        if "participation" not in extracted_data:
            if "participation" in split_syllabus[line - 1].casefold():
                extracted_data["participation"] = split_syllabus[line]
        if "hands_on" not in extracted_data:
            if "hands on" in split_syllabus[line - 1].casefold():
                extracted_data["hands_on"] = split_syllabus[line]
        if "assignments" not in extracted_data:
            if "assignments" in split_syllabus[line - 1].casefold():
                extracted_data["assignments"] = split_syllabus[line]
        if "homework" not in extracted_data:
            if "homework" in split_syllabus[line - 1].casefold():
                extracted_data["homework"] = split_syllabus[line]
        if "late_policy" not in extracted_data:
            if "late polcy" in split_syllabus[line - 1].casefold():
                extracted_data["late_policy"] = split_syllabus[line]
        if "makeup_policy" not in extracted_data:
            if "makeup polcy" in split_syllabus[line - 1].casefold():
                extracted_data["makeup_policy"] = split_syllabus[line]

    return extracted_data
