import textract
import re


def extract_data(file):
    # setting up the blanks for the if statement below, if i were paid it'd be neater
    # these were originally set up as test variables so it wouldn't constantly be saving and
    # returning to the database - leaving these until i finish this concept out so i know
    # just how far i've gotten and how far i've got left.
    # title = instructor_name = instructor_phone = instructor_email = ta_name = ""
    # ta_email = course_site = course_time = office_hours = course_description = ""
    # course_objectives = prereqs = textbook = instruct_methods = ""

    # ok, now onto the REAL magic
    extracted_data = {

    }
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
                extracted_data["title"] = split_syllabus[line][:7]
            elif (split_syllabus[line].startswith("ENCH", 0, 9) or split_syllabus[line].startswith("CMSC", 0, 9) or
                  split_syllabus[line].startswith("CMPE", 0, 9) or split_syllabus[line].startswith("DATA", 0, 9) or
                  split_syllabus[line].startswith("ENEE", 0, 9) or split_syllabus[line].startswith("ENME", 0, 9) or
                  split_syllabus[line].startswith("ENES", 0, 9)):
                extracted_data["title"] = split_syllabus[line][:9]
        if "instructor_name" not in extracted_data:
            if split_syllabus[line].startswith("Dr") or split_syllabus[line].startswith("Prof"):
                extracted_data["instructor_name"] = split_syllabus[line]
            elif split_syllabus[line].startswith("Instructor:"):
                extracted_data["instructor_name"] = split_syllabus[line].strip("Instructor: ")
        if "instructor_phone" not in extracted_data:
            if "Phone:" in split_syllabus[line] and "instructor_name" in extracted_data:
                extracted_data["instructor_phone"] = split_syllabus[line].strip("Phone: ")
        if "instructor_email" not in extracted_data:
            if "Email:" in split_syllabus[line]:
                extracted_data["instructor_email"] = split_syllabus[line].strip("Email: ")
            elif "E-mail:" in split_syllabus[line]:
                extracted_data["instructor_email"] = split_syllabus[line].strip("E-mail: ")
        # TODO: grabbing TA name and email are NOT working correctly, needs future fix
        if "ta_name" not in extracted_data:
            if "<" in split_syllabus[line]:
                extracted_data["ta_name"] = split_syllabus[line].split(" <", 1)[0]
                extracted_data["ta_email"] = split_syllabus[line].split(" <", 1)[1].split(">", 1)[0]
            elif ("course_time" not in extracted_data and len(split_syllabus[line].split()) >= 2 and len(
                    re.findall('\b[A-Z].*?\b', split_syllabus[line])) >= 2):
                extracted_data["ta_name"] = split_syllabus[line]
        if "ta_email" not in extracted_data and "instructor_email" in extracted_data:
            if "umbc.edu" in split_syllabus[line]:
                extracted_data["ta_email"] = split_syllabus[line]
        if "course_site" not in extracted_data:
            if "Course" in split_syllabus[line] and \
                    ("Site" in split_syllabus[line] or "site" in split_syllabus[line]) and \
                    "https://" in split_syllabus[line]:
                extracted_data["course_site"] = split_syllabus[line].split('http://', 1)[1]
            elif "Course" in split_syllabus[line] and \
                    ("Site" in split_syllabus[line] or "site" in split_syllabus[line]) and \
                    "https://" in split_syllabus[line]:
                extracted_data["course_site"] = split_syllabus[line].split('https://', 1)[1]
        if "office_hours" not in extracted_data:
            if "office hours: " in split_syllabus[line].casefold():
                extracted_data["office_hours"] = split_syllabus[line].casefold().split('office hours: ', 1)[1].split(',', 1)[0].title()
            elif "office hours" in split_syllabus[line].casefold():
                extracted_data["office_hours"] = split_syllabus[line].casefold().split('office hours', 1)[1].split(',', 1)[0].title()
        if "course_time" not in extracted_data:
            if "lecture" in split_syllabus[line].casefold():
                extracted_data["course_time"] = split_syllabus[line].split(': ', 1)[1]
        # course description not perfect due to it being multisplit_syllabus[line]
        if "course_description" not in extracted_data:
            if "This" in split_syllabus[line] and "course" in split_syllabus[line]:
                extracted_data["course_description"] = split_syllabus[line]
        # not even going to try objectives due to same issue as course description
        if "course_objectives" not in extracted_data:
            pass
        if "prereqs" not in extracted_data:
            if "Prerequisites:" in split_syllabus[line]:
                extracted_data["prereqs"] = split_syllabus[line].split("\xa0\xa0\xa0", 1)[1].split(",", 1)[0]
            elif "Prerequisite:" in split_syllabus[line]:
                extracted_data["prereqs"] = split_syllabus[line].split("Prerequisite: ", 1)[1].split(",", 1)[0]
        if "textbook" not in extracted_data:
            if "Edition" in split_syllabus[line].title() and "\xa0" in split_syllabus[line]:
                extracted_data["textbook"] = split_syllabus[line].split("\xa0\xa0    ", 1)[
                    1]  # might need slight improvement here, remains to be seen
            elif "Edition" in split_syllabus[line].title() and "\xa0" not in split_syllabus[line]:
                extracted_data["textbook"] = split_syllabus[line]
        if "instruct_methods" not in extracted_data:
            pass
    return extracted_data
