from re import sub
from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your tests here.
from .models import Course



class CourseFormTests(TestCase):
    #test that wizard page loads
    def test_formpage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class CourseFormSeleniumTests(LiveServerTestCase):

    #test form wizard with schedule
    def testFormWizardSchedule(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/Downloads/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/syllabus_form/wizard')

        #################################################### PAGE 1 ####################################################
        #find elements for page 1/17
        department = selenium.find_element_by_id('id_1-department')
        department_office = selenium.find_element_by_id('id_1-department_office')
        department_phone = selenium.find_element_by_id('id_1-department_phone')
        course_number = selenium.find_element_by_id('id_1-course_number')
        course_name = selenium.find_element_by_id('id_1-course_name')
        semester = selenium.find_element_by_id('id_1-semester')
        year = selenium.find_element_by_id('id_1-year')
        course_acronym = selenium.find_element_by_id('id_1-course_acronym')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 1/17
        department.send_keys('Information Systems Department')
        department_office.send_keys('Room ITE 404')
        department_phone.send_keys('410-455-3206')
        course_number.send_keys('147')
        course_name.send_keys('Introduction to Programming')
        semester.send_keys('Fall')
        year.send_keys('2021')
        course_acronym.send_keys('IS')

        time.sleep(2) 
        #submit page 1/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 2 ####################################################
        #find elements for page 2/17
        instructor_name = selenium.find_element_by_id('id_2-instructor_name')
        instructor_phone = selenium.find_element_by_id('id_2-instructor_phone')
        instructor_email = selenium.find_element_by_id('id_2-instructor_email')
        instructor_fax = selenium.find_element_by_id('id_2-instructor_fax')
        instructor_website = selenium.find_element_by_id('id_2-instructor_website')
        instructor_course_delivery_site = selenium.find_element_by_id('id_2-instructor_course_delivery_site')
        instructor_office_hours = selenium.find_element_by_id('id_2-instructor_office_hours')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 2/17
        instructor_name.send_keys('Ben Johnson')
        instructor_phone.send_keys('410-499-9999')
        instructor_email.send_keys('bjohnson@umbc.edu')
        instructor_fax.send_keys('410-499-9999')
        instructor_website.send_keys('bjohnson.com')
        instructor_course_delivery_site.send_keys('blackboard.com')
        instructor_office_hours.send_keys('Wednesday 12-2 PM')
        
        time.sleep(2) 

        #submit page 2/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 3 ####################################################
        #find elements for page 3/17
        meeting_times = selenium.find_element_by_id('id_3-meeting_times')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 3/17
        meeting_times.send_keys('Section 101 M/W 8:30-9:45 AM ILSB 233\nSection 102 M/W 10:30-11:45 AM ILSB 233')

        time.sleep(2) 

        #submit page 3/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 4 ####################################################
        #find elements for page 4/17
        textbook = selenium.find_element_by_id('id_4-textbook')
        course_description = selenium.find_element_by_id('id_4-course_description')
        num_credits = selenium.find_element_by_id('id_4-num_credits')
        prerequisites = selenium.find_element_by_id('id_4-prerequisites')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 4/17
        textbook.send_keys('REVEL for Liang, online version of Introduction to Java Programming from Pearson publishing: ISBN 13: 978-134167008')
        course_description.send_keys('This course introduces the basic principles and techniques invovled in computer programming and computing.'\
            ' Methods of algorithm development, program development, and program design are taught using an object-oriented programming language.'\
            ' Projects are geared toward those typically encountered in the Information Systems field.'\
            '\n\nThis course is an introduction to both programming and the principles of computer science.'\
            ' You will learn how to program with principles that are relevant to all programming languages and also learn the basic concepts and vocabulary of computer science.'\
            ' It is a very important course in your education and will require significant weekly work on the readings and the programming projects.'\
            ' You will learn foundational computing concepts and develop programming skills.'\
            ' This course serves as preparation for IS 247.'\
            ' We will be using the Java programming language.')
        num_credits.send_keys('3')
        prerequisites.send_keys('Recommended Preparation: IS 101 or COMP 101Y')

        time.sleep(2) 

        #submit page 4/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 5 ####################################################
        #find elements for page 5/17
        course_objectives = selenium.find_element_by_id('id_5-course_objectives')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 5/17
        course_objectives.send_keys('Demonstrate skill necessary to succeed as a computing student and professional\n'\
            'Work effectively in a team to solve a complex technological challenge\n'\
            'Understand and apply fundamental concepts in computing (i.e., computational thinking, social responsibility and ethical inquiry\n'\
            'Write basic programs using variables, conditional logic, loops, and functions\n')

        time.sleep(2) 

        #submit page 5/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 6 ####################################################
        #find elements for page 6/17
        instructional_methods = selenium.find_element_by_id('id_6-instructional_methods')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 6/17
        instructional_methods.send_keys('Lecture')

        time.sleep(2) 

        #submit page 6/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 7 ####################################################
        #find elements for page 7/17
        attendance_participation = selenium.find_element_by_id('id_7-attendance_participation')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 7/17
        attendance_participation.send_keys('Regular and punctual attendance is expected of all students'\
            ' In the case of absence due to emergency (illness, dealth in the family, accident, religious holiday, or participation in official College functions,'\
            ' it is the student\'s responsibility to confer with the instructor about the absence and missed course work.')

        time.sleep(2) 

        #submit page 7/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 8 ####################################################
        #find elements for page 8/17
        class_pre_and_student_success = selenium.find_element_by_id('id_8-class_pre_and_student_success')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 8/17
        class_pre_and_student_success.send_keys('All of the reading assignments should be completed before the class in which the material is to be discussed.'\
            ' Students should expect taht for every 3 credit hours course they are devoting at least 9 additional hours preparing and studying course materials which are required or suggested.'\
            ' Students should contact the instructor for additional information about how to best achieve the goals and meet the academic expectations for this course.'\
            ' Additional support may be available through university or department resources in order to guide students toward success.')


        time.sleep(2) 

        #submit page 8/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 9 ####################################################
        #find elements for page 9/17
        course_requirements = selenium.find_element_by_id('id_9-course_requirements')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 9/17
        course_requirements.send_keys('Regular, punctual attendance is expected of all students in lecture.'\
            ' In-class assignments and homework must be completed by the time and date specified for full credit.'\
            ' Students are expected to be respectful, active contributors during group work.')

        time.sleep(2) 

        #submit page 9/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 10 ####################################################
        #find elements for page 10/17
        grade_apportionment = selenium.find_element_by_id('id_10-grade_apportionment')
        grade_descriptions = selenium.find_element_by_id('id_10-descriptions')
        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 10/17
        grade_apportionment.send_keys('In-class programming = 20%\n'\
            'Reading and Programming Homework = 10%\n'\
            'Test = 30%\n'\
            'Hands-on Programming Test = 30%\n'
            'Attendance = 10%')
        grade_descriptions.send_keys('In-class Programming: For many of the classes, there will be in-class programming assignments that I will work through in-class. At the end of class, you are expected to submit your assignment. These will be graded based on completion.\n\n'\
            'Reading and Programming Homework: There will be a weekly homework assignment. You can work with your classmates on these assignments, but you are not allowed to submit the same work.\n\n'\
            'Tests: There will be 3 two tests. One midterm and one final. The midterm is worth 10% and the final is worth 20%. These will be in-person, and you must bring you student ID.\n\n'\
            'Hands-on Programming Test: This will take place in class towards the end of the semester. You will not be able to work with your peers for this test.\n\n'\
            'Attendance: For each class, I will mark attendance. If you miss more than 3 classes, your cumulative grade at the end of the semester will drop one letter grade. '\
            'For example, if you got an \'A\' in the course but missed 4 classes, your grade will drop to a \'B\'. The missed attendances stack, so for every multiple of 3 classes that you miss, your letter grade drops.')
        time.sleep(2) 

        #submit page 10/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 11 ####################################################
        #find elements for page 11/17
        grading_standards = selenium.find_element_by_id('id_11-grading_standards')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 11/17
        grading_standards.send_keys('IS instructors are expected to have exams and evaluations, which result in a reasonable distribution of grades.'\
            ' With respect to final letter grades, the University\'s Undergraduate Catalogue states that, \"A, indicates superior achievement; B, good performance; C, adequate performance, D; minimal performance; F, falure\."'\
            ' There is specifically no mention of any numerical scores associated with these letter grades.'\
            ' Consequently, there are no pre-defined numerical demarcations that determine final letter grade.'\
            ' These numerical demaarcations that determine final letter grade can only be defined at the end of the semester after all numerical grades have been earned.'\
            ' At that point, numerical demarcations for final letter grades can be defined such that final letter grades in the course conform to the Unverisity\'s officially published definitions of the respective letter grades.'\
            ' In accordance with the published University grading policy, it is important to understand that final letter grades reflect academic achievement and not effort.'\
            ' While mistakes in the arithmetic computation of grades and grade recording errors will always be corrected, it is important to understand that in all other situations final letter grades are not negotiable and challenges to final letter grades are not entertained.'\
            ' Historical data suggest an \"A\" may be in the 91-100 range, \"B\"\'s may be from 81-90 and \"C\" grades from 70-80.'\
            ' All points from assignments and exams are additive for the semester.'\
            ' Each student starts at zero points which is an \"F\", any other grade must be earned.'\
            ' There will be no extra credit assignments available.')

        time.sleep(2) 

        #submit page 11/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 12 ####################################################
        #find elements for page 12/17
        due_dates = selenium.find_element_by_id('id_12-due_dates')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 12/17
        due_dates.send_keys('All assignments are to be handed in by the due date.'\
            ' If an assignment is not completed and submitted on time it may be accepted the following class session with an accompanying reduct of 70% of the earned grade.'\
            ' Due to some scheduling issues, some late assignments may not be accepted at all and will result in a total loss of points.')

        time.sleep(2) 

        #submit page 12/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 13 ####################################################
        #find elements for page 13/17
        make_up_policy = selenium.find_element_by_id('id_13-make_up_policy')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 13/17
        make_up_policy.send_keys('No make-up exams are allowed except through arrangement with the instructor prior to the exam date.'\
            ' As a result of creating new questions, make-up exams may be harder then the original scheduled exam.')

        time.sleep(2) 

        #submit page 13/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 14 ####################################################
        #find elements for page 14/17
        academic_integrity = selenium.find_element_by_id('id_14-academic_integrity')

        submit = selenium.find_element_by_id('submit')


        #populate the form with data for page 14/17
        academic_integrity.send_keys('By enrolling in this course, each student assumes the responsibilities of an active participant in UMBC\'s scholarly community in which everyone\'s academic work and behavior are held to the highest standard of honesty.'\
            ' Cheating, fabricating, plagiarism, and helping others to commit these acts are all forms of academic dishonesty and they are wrong.'\
            ' Academic misconduct could result in disciplinary action that may include, but is not limited to, suspension or dismissal.'\
            ' Full policies on academic integrity should be available in the UMBC Student Handbook, Faculty Handbook, or the UMBC Directory.')

        time.sleep(2) 

        #submit page 14/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 15 ####################################################
        #find elements for page 15/17
        accommodations = selenium.find_element_by_id('id_15-accommodations')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 15/17
        accommodations.send_keys('Support services for students with disabilities are provided for all students qualified under the Americans with Disabilities Act (ADA & ADAAA) and Section 504 of the Rehabilitation Act who request and are eligble for accommodations.'\
            ' The Office of Student Disability Services (SDS) is the UMBC department designated to coordinate accommodations that would create equal access for students when barriers to participation exist in University courses, programs, or activites.'\
            '\n\n If you have a documented disability and need to request acadmeic accommodations in your courses, please refer to the SDS wesbite at https://sds.umbc.edu/ for registration information and office procedures.'\
            '\n\nSDS email: disability@umbc.edu'\
            '\nSDS phone: (410)-455-2459'\
            '\nIf you will be using SDS approved accommodations in this class, please contact me (instructor) to discuss implementation of the accommodations.'\
            ' During remote instruction requirements due to COVID, communication and flexibility will be essential for success.')

        time.sleep(2) 

        #submit page 15/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 16 ####################################################
        #find elements for page 16/17

        submit = selenium.find_element_by_id('submit')
        lecture0 = selenium.find_element_by_id('id_16-lecture0')
        material0 = selenium.find_element_by_id('id_16-material0')
        due0 = selenium.find_element_by_id('id_16-due0')
        lecture1 = selenium.find_element_by_id('id_16-lecture1')
        material1 = selenium.find_element_by_id('id_16-material1')
        due1 = selenium.find_element_by_id('id_16-due1')
        lecture2 = selenium.find_element_by_id('id_16-lecture2')
        material2 = selenium.find_element_by_id('id_16-material2')
        due2 = selenium.find_element_by_id('id_16-due2')
        lecture3 = selenium.find_element_by_id('id_16-lecture3')
        material3 = selenium.find_element_by_id('id_16-material3')
        due3 = selenium.find_element_by_id('id_16-due3')
        lecture4 = selenium.find_element_by_id('id_16-lecture4')
        material4 = selenium.find_element_by_id('id_16-material4')
        due4 = selenium.find_element_by_id('id_16-due4')

        #populate the form with data for page 16/17
        lecture0.send_keys('Week 1')
        material0.send_keys('Intro Week')
        due0.send_keys('')
        lecture1.send_keys('Week 2')
        material1.send_keys('Object Oriented Programming')
        due1.send_keys('Homework 1')
        lecture2.send_keys('Week 3')
        material2.send_keys('Data Structures')
        due2.send_keys('Exam & Homework 2')
        lecture3.send_keys('Week 4')
        material3.send_keys('Algorithms')
        due3.send_keys('Homework 3')
        lecture4.send_keys('Week 5')
        material4.send_keys('Review')
        due4.send_keys('Final Exam')

        time.sleep(2) 

        #submit page 16/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 17 ####################################################
        #find elements for page 17/17
        inclement_weather = selenium.find_element_by_id('id_17-inclement_weather')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 17/17
        inclement_weather.send_keys('Any work or test due on a class date that has been canceled due to inclement weather will be due the next class meeting.'\
            ' (If the semester\'s last exam is postponed, it will be given during the time period assigned during the University\'s official Final Exam week.')

        time.sleep(2) 

        #submit page 17/17
        submit.send_keys(Keys.RETURN)

        time.sleep(20)

    #test that the button that sends the wizard back to the first step works
    def testFirstStep(self):
        selenium = webdriver.Chrome(executable_path='chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/syllabus_form/wizard')

        #################################################### PAGE 1 ####################################################
        #find elements for page 1/17
        department = selenium.find_element_by_id('id_1-department')
        department_office = selenium.find_element_by_id('id_1-department_office')
        department_phone = selenium.find_element_by_id('id_1-department_phone')
        course_number = selenium.find_element_by_id('id_1-course_number')
        course_name = selenium.find_element_by_id('id_1-course_name')
        semester = selenium.find_element_by_id('id_1-semester')
        year = selenium.find_element_by_id('id_1-year')
        course_acronym = selenium.find_element_by_id('id_1-course_acronym')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 1/17
        department.send_keys('Information Systems Department')
        department_office.send_keys('Room ITE 404')
        department_phone.send_keys('410-455-3206')
        course_number.send_keys('147')
        course_name.send_keys('Introduction to Programming')
        semester.send_keys('Fall')
        year.send_keys('2021')
        course_acronym.send_keys('IS')

        time.sleep(2) 
        #submit page 1/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 2 ####################################################
        #find elements for page 2/17
        instructor_name = selenium.find_element_by_id('id_2-instructor_name')
        instructor_phone = selenium.find_element_by_id('id_2-instructor_phone')
        instructor_email = selenium.find_element_by_id('id_2-instructor_email')
        instructor_fax = selenium.find_element_by_id('id_2-instructor_fax')
        instructor_website = selenium.find_element_by_id('id_2-instructor_website')
        instructor_course_delivery_site = selenium.find_element_by_id('id_2-instructor_course_delivery_site')
        instructor_office_hours = selenium.find_element_by_id('id_2-instructor_office_hours')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 2/17
        instructor_name.send_keys('Ben Johnson')
        instructor_phone.send_keys('410-499-9999')
        instructor_email.send_keys('bjohnson@umbc.edu')
        instructor_fax.send_keys('410-499-9999')
        instructor_website.send_keys('bjohnson.com')
        instructor_course_delivery_site.send_keys('blackboard.com')
        instructor_office_hours.send_keys('Wednesday 12-2 PM')
        
        time.sleep(2) 

        #submit page 2/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 3 ####################################################
        #find elements for page 3/17

        first = selenium.find_element_by_id('first')

        #populate the form with data for page 3/17

        time.sleep(1) 

        #submit page 3/17
        first.send_keys(Keys.RETURN)

        time.sleep(2) 


    #test that the button that sends the wizard back one page works
    def testPrevStep(self):
        selenium = webdriver.Chrome(executable_path='chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/syllabus_form/wizard')

        #################################################### PAGE 1 ####################################################
        #find elements for page 1/17
        department = selenium.find_element_by_id('id_1-department')
        department_office = selenium.find_element_by_id('id_1-department_office')
        department_phone = selenium.find_element_by_id('id_1-department_phone')
        course_number = selenium.find_element_by_id('id_1-course_number')
        course_name = selenium.find_element_by_id('id_1-course_name')
        semester = selenium.find_element_by_id('id_1-semester')
        year = selenium.find_element_by_id('id_1-year')
        course_acronym = selenium.find_element_by_id('id_1-course_acronym')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 1/17
        department.send_keys('Information Systems Department')
        department_office.send_keys('Room ITE 404')
        department_phone.send_keys('410-455-3206')
        course_number.send_keys('147')
        course_name.send_keys('Introduction to Programming')
        semester.send_keys('Fall')
        year.send_keys('2021')
        course_acronym.send_keys('IS')

        time.sleep(2) 
        #submit page 1/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 2 ####################################################
        #find elements for page 2/17
       
        prev = selenium.find_element_by_id('prev')

        time.sleep(1)

        #submit page 2/17
        prev.send_keys(Keys.RETURN)

        time.sleep(2)

    #test that the welcome for the wizard works
    def testWelcomePage(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/Downloads/chromedriver')

        #choose url to use
        #first import syllabus
        selenium.get('http://127.0.0.1:8000/add/')

        #find elements
        pdf_file = selenium.find_element_by_xpath("//input[@type='file']")
        submit = selenium.find_element_by_xpath("//input[@type='submit']")
        #need a syllabus to upload
        # pdf_file.send_keys('./syllabus_form/syllabus_pdfs/IS147-Section01-AhmedAlEroud-Syllabus.pdf')
        pdf_file.send_keys('/Users/gersonkroiz/CMSC_447/syllabus-project/syllabus_form/syllabus_pdfs/IS147-Section01-AhmedAlEroud-Syllabus.pdf')
        #submit pdf
        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        selenium.get('http://127.0.0.1:8000/syllabus_form/')

        #find elements
        search = selenium.find_element_by_id('search')

        #check that you can't do empty search
        search.send_keys(Keys.RETURN)

        time.sleep(1)

        #find elements
        search = selenium.find_element_by_id('search')
        goto = selenium.find_element_by_id('goto')
        course = selenium.find_element_by_id('id_course')

        #search invalid course
        course.send_keys('IS 999')

        time.sleep(1)

        search.send_keys(Keys.RETURN)

        #find elements
        no = selenium.find_element_by_id('no')
        goto = selenium.find_element_by_id('goto')

        time.sleep(2)

        #go back to search
        no.send_keys(Keys.RETURN)

        #find elements
        search = selenium.find_element_by_id('search')
        goto = selenium.find_element_by_id('goto')
        course = selenium.find_element_by_id('id_course')

        #search syllabus in database
        course.send_keys('IS 147')

        time.sleep(1)

        search.send_keys(Keys.RETURN)

        #find elements
        yes = selenium.find_element_by_id('yes')
        no = selenium.find_element_by_id('no')

        time.sleep(2)

        #show that you can return to search
        no.send_keys(Keys.RETURN)

        #find elements
        search = selenium.find_element_by_id('search')
        goto = selenium.find_element_by_id('goto')
        course = selenium.find_element_by_id('id_course')

        #search syllabus in database
        course.send_keys('IS 147')

        time.sleep(1)

        search.send_keys(Keys.RETURN)

        #find elements
        yes = selenium.find_element_by_id('yes')
        no = selenium.find_element_by_id('no')

        time.sleep(2)

        #show that you can use imported data for the wizard
        yes.send_keys(Keys.RETURN)

        time.sleep(2)

        #put in filler data to show how the imported data fits throughout the wizard
        #################################################### PAGE 1 ####################################################
        #find elements for page 1/17
        department = selenium.find_element_by_id('id_1-department')
        department_office = selenium.find_element_by_id('id_1-department_office')
        department_phone = selenium.find_element_by_id('id_1-department_phone')
        course_number = selenium.find_element_by_id('id_1-course_number')
        course_name = selenium.find_element_by_id('id_1-course_name')
        semester = selenium.find_element_by_id('id_1-semester')
        year = selenium.find_element_by_id('id_1-year')
        course_acronym = selenium.find_element_by_id('id_1-course_acronym')

        submit = selenium.find_element_by_id('submit')

        time.sleep(2) 

        #populate the form with data for page 1/17
        department.send_keys('Information Systems Department')
        department_office.send_keys('Room ITE 404')
        department_phone.send_keys('410-455-3206')
        course_number.send_keys('147')
        course_name.send_keys('Introduction to Programming')
        semester.send_keys('Fall')
        year.send_keys('2021')
        course_acronym.send_keys('IS')

        #submit page 1/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 2 ####################################################
        #find elements for page 2/17
        instructor_name = selenium.find_element_by_id('id_2-instructor_name')
        instructor_phone = selenium.find_element_by_id('id_2-instructor_phone')
        instructor_email = selenium.find_element_by_id('id_2-instructor_email')
        instructor_fax = selenium.find_element_by_id('id_2-instructor_fax')
        instructor_website = selenium.find_element_by_id('id_2-instructor_website')
        instructor_course_delivery_site = selenium.find_element_by_id('id_2-instructor_course_delivery_site')
        instructor_office_hours = selenium.find_element_by_id('id_2-instructor_office_hours')

        submit = selenium.find_element_by_id('submit')

        time.sleep(2) 

        selenium.find_element_by_id('id_2-instructor_email').send_keys(Keys.CONTROL + "a")
        selenium.find_element_by_id('id_2-instructor_email').clear()
        # selenium.get_element_by_id('id_2-instructor_email').clear()

        time.sleep(2) 

        #populate the form with data for page 2/17
        instructor_name.send_keys('Ben Johnson')
        instructor_phone.send_keys('410-499-9999')
        instructor_email.send_keys('bjohnson@umbc.edu')
        instructor_fax.send_keys('410-499-9999')
        instructor_website.send_keys('bjohnson.com')
        instructor_course_delivery_site.send_keys('blackboard.com')
        instructor_office_hours.send_keys('Wednesday 12-2 PM')
        print('HERE')
        
        #submit page 2/17
        submit.send_keys(Keys.RETURN)
        time.sleep(2) 
        print('HERE2')

        #################################################### PAGE 3 ####################################################
        #find elements for page 3/17
        meeting_times = selenium.find_element_by_id('id_3-meeting_times')

        submit = selenium.find_element_by_id('submit')

        time.sleep(2) 

        #populate the form with data for page 3/17
        meeting_times.send_keys('Section 101 M/W 8:30-9:45 AM ILSB 233\nSection 102 M/W 10:30-11:45 AM ILSB 233')


        #submit page 3/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 4 ####################################################
        #find elements for page 4/17
        textbook = selenium.find_element_by_id('id_4-textbook')
        course_description = selenium.find_element_by_id('id_4-course_description')
        num_credits = selenium.find_element_by_id('id_4-num_credits')
        prerequisites = selenium.find_element_by_id('id_4-prerequisites')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 4/17
        textbook.send_keys('REVEL for Liang, online version of Introduction to Java Programming from Pearson publishing: ISBN 13: 978-134167008')
        course_description.send_keys('This course introduces the basic principles and techniques invovled in computer programming and computing.'\
            ' Methods of algorithm development, program development, and program design are taught using an object-oriented programming language.'\
            ' Projects are geared toward those typically encountered in the Information Systems field.'\
            '\n\nThis course is an introduction to both programming and the principles of computer science.'\
            ' You will learn how to program with principles that are relevant to all programming languages and also learn the basic concepts and vocabulary of computer science.'\
            ' It is a very important course in your education and will require significant weekly work on the readings and the programming projects.'\
            ' You will learn foundational computing concepts and develop programming skills.'\
            ' This course serves as preparation for IS 247.'\
            ' We will be using the Java programming language.')
        num_credits.send_keys('3')
        prerequisites.send_keys('Recommended Preparation: IS 101 or COMP 101Y')


        #submit page 4/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 5 ####################################################
        #find elements for page 5/17
        course_objectives = selenium.find_element_by_id('id_5-course_objectives')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 5/17
        course_objectives.send_keys('Demonstrate skill necessary to succeed as a computing student and professional\n'\
            'Work effectively in a team to solve a complex technological challenge\n'\
            'Understand and apply fundamental concepts in computing (i.e., computational thinking, social responsibility and ethical inquiry\n'\
            'Write basic programs using variables, conditional logic, loops, and functions\n')


        #submit page 5/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 6 ####################################################
        #find elements for page 6/17
        instructional_methods = selenium.find_element_by_id('id_6-instructional_methods')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 6/17
        instructional_methods.send_keys('Lecture')


        #submit page 6/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 7 ####################################################
        #find elements for page 7/17
        attendance_participation = selenium.find_element_by_id('id_7-attendance_participation')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 7/17
        attendance_participation.send_keys('Regular and punctual attendance is expected of all students'\
            ' In the case of absence due to emergency (illness, dealth in the family, accident, religious holiday, or participation in official College functions,'\
            ' it is the student\'s responsibility to confer with the instructor about the absence and missed course work.')


        #submit page 7/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 8 ####################################################
        #find elements for page 8/17
        class_pre_and_student_success = selenium.find_element_by_id('id_8-class_pre_and_student_success')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 8/17
        class_pre_and_student_success.send_keys('All of the reading assignments should be completed before the class in which the material is to be discussed.'\
            ' Students should expect taht for every 3 credit hours course they are devoting at least 9 additional hours preparing and studying course materials which are required or suggested.'\
            ' Students should contact the instructor for additional information about how to best achieve the goals and meet the academic expectations for this course.'\
            ' Additional support may be available through university or department resources in order to guide students toward success.')


        #submit page 8/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 9 ####################################################
        #find elements for page 9/17
        course_requirements = selenium.find_element_by_id('id_9-course_requirements')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 9/17
        course_requirements.send_keys('Regular, punctual attendance is expected of all students in lecture.'\
            ' In-class assignments and homework must be completed by the time and date specified for full credit.'\
            ' Students are expected to be respectful, active contributors during group work.')


        #submit page 9/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 10 ####################################################
        #find elements for page 10/17
        grade_apportionment = selenium.find_element_by_id('id_10-grade_apportionment')
        grade_descriptions = selenium.find_element_by_id('id_10-descriptions')
        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 10/17
        grade_apportionment.send_keys('In-class programming = 20%\n'\
            'Reading and Programming Homework = 10%\n'\
            'Test = 30%\n'\
            'Hands-on Programming Test = 30%\n'
            'Attendance = 10%')
        grade_descriptions.send_keys('In-class Programming: For many of the classes, there will be in-class programming assignments that I will work through in-class. At the end of class, you are expected to submit your assignment. These will be graded based on completion.\n\n'\
            'Reading and Programming Homework: There will be a weekly homework assignment. You can work with your classmates on these assignments, but you are not allowed to submit the same work.\n\n'\
            'Tests: There will be 3 two tests. One midterm and one final. The midterm is worth 10% and the final is worth 20%. These will be in-person, and you must bring you student ID.\n\n'\
            'Hands-on Programming Test: This will take place in class towards the end of the semester. You will not be able to work with your peers for this test.\n\n'\
            'Attendance: For each class, I will mark attendance. If you miss more than 3 classes, your cumulative grade at the end of the semester will drop one letter grade. '\
            'For example, if you got an \'A\' in the course but missed 4 classes, your grade will drop to a \'B\'. The missed attendances stack, so for every multiple of 3 classes that you miss, your letter grade drops.')

        #submit page 10/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 11 ####################################################
        #find elements for page 11/17
        grading_standards = selenium.find_element_by_id('id_11-grading_standards')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 11/17
        grading_standards.send_keys('IS instructors are expected to have exams and evaluations, which result in a reasonable distribution of grades.'\
            ' With respect to final letter grades, the University\'s Undergraduate Catalogue states that, \"A, indicates superior achievement; B, good performance; C, adequate performance, D; minimal performance; F, falure\."'\
            ' There is specifically no mention of any numerical scores associated with these letter grades.'\
            ' Consequently, there are no pre-defined numerical demarcations that determine final letter grade.'\
            ' These numerical demaarcations that determine final letter grade can only be defined at the end of the semester after all numerical grades have been earned.'\
            ' At that point, numerical demarcations for final letter grades can be defined such that final letter grades in the course conform to the Unverisity\'s officially published definitions of the respective letter grades.'\
            ' In accordance with the published University grading policy, it is important to understand that final letter grades reflect academic achievement and not effort.'\
            ' While mistakes in the arithmetic computation of grades and grade recording errors will always be corrected, it is important to understand that in all other situations final letter grades are not negotiable and challenges to final letter grades are not entertained.'\
            ' Historical data suggest an \"A\" may be in the 91-100 range, \"B\"\'s may be from 81-90 and \"C\" grades from 70-80.'\
            ' All points from assignments and exams are additive for the semester.'\
            ' Each student starts at zero points which is an \"F\", any other grade must be earned.'\
            ' There will be no extra credit assignments available.')


        #submit page 11/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 12 ####################################################
        #find elements for page 12/17
        due_dates = selenium.find_element_by_id('id_12-due_dates')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 12/17
        due_dates.send_keys('All assignments are to be handed in by the due date.'\
            ' If an assignment is not completed and submitted on time it may be accepted the following class session with an accompanying reduct of 70% of the earned grade.'\
            ' Due to some scheduling issues, some late assignments may not be accepted at all and will result in a total loss of points.')

        time.sleep(2) 

        #submit page 12/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 13 ####################################################
        #find elements for page 13/17
        make_up_policy = selenium.find_element_by_id('id_13-make_up_policy')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 13/17
        make_up_policy.send_keys('No make-up exams are allowed except through arrangement with the instructor prior to the exam date.'\
            ' As a result of creating new questions, make-up exams may be harder then the original scheduled exam.')


        #submit page 13/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 14 ####################################################
        #find elements for page 14/17
        academic_integrity = selenium.find_element_by_id('id_14-academic_integrity')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 


        #populate the form with data for page 14/17
        academic_integrity.send_keys('By enrolling in this course, each student assumes the responsibilities of an active participant in UMBC\'s scholarly community in which everyone\'s academic work and behavior are held to the highest standard of honesty.'\
            ' Cheating, fabricating, plagiarism, and helping others to commit these acts are all forms of academic dishonesty and they are wrong.'\
            ' Academic misconduct could result in disciplinary action that may include, but is not limited to, suspension or dismissal.'\
            ' Full policies on academic integrity should be available in the UMBC Student Handbook, Faculty Handbook, or the UMBC Directory.')

        #submit page 14/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 15 ####################################################
        #find elements for page 15/17
        accommodations = selenium.find_element_by_id('id_15-accommodations')

        submit = selenium.find_element_by_id('submit')

        #populate the form with data for page 15/17
        accommodations.send_keys('Support services for students with disabilities are provided for all students qualified under the Americans with Disabilities Act (ADA & ADAAA) and Section 504 of the Rehabilitation Act who request and are eligble for accommodations.'\
            ' The Office of Student Disability Services (SDS) is the UMBC department designated to coordinate accommodations that would create equal access for students when barriers to participation exist in University courses, programs, or activites.'\
            '\n\n If you have a documented disability and need to request acadmeic accommodations in your courses, please refer to the SDS wesbite at https://sds.umbc.edu/ for registration information and office procedures.'\
            '\n\nSDS email: disability@umbc.edu'\
            '\nSDS phone: (410)-455-2459'\
            '\nIf you will be using SDS approved accommodations in this class, please contact me (instructor) to discuss implementation of the accommodations.'\
            ' During remote instruction requirements due to COVID, communication and flexibility will be essential for success.')

        time.sleep(2) 

        #submit page 15/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 16 ####################################################
        #find elements for page 16/17

        submit = selenium.find_element_by_id('submit')
        lecture0 = selenium.find_element_by_id('id_16-lecture0')
        material0 = selenium.find_element_by_id('id_16-material0')
        due0 = selenium.find_element_by_id('id_16-due0')
        lecture1 = selenium.find_element_by_id('id_16-lecture1')
        material1 = selenium.find_element_by_id('id_16-material1')
        due1 = selenium.find_element_by_id('id_16-due1')
        lecture2 = selenium.find_element_by_id('id_16-lecture2')
        material2 = selenium.find_element_by_id('id_16-material2')
        due2 = selenium.find_element_by_id('id_16-due2')
        lecture3 = selenium.find_element_by_id('id_16-lecture3')
        material3 = selenium.find_element_by_id('id_16-material3')
        due3 = selenium.find_element_by_id('id_16-due3')
        lecture4 = selenium.find_element_by_id('id_16-lecture4')
        material4 = selenium.find_element_by_id('id_16-material4')
        due4 = selenium.find_element_by_id('id_16-due4')

        #populate the form with data for page 16/17
        lecture0.send_keys('Week 1')
        material0.send_keys('Intro Week')
        due0.send_keys('')
        lecture1.send_keys('Week 2')
        material1.send_keys('Object Oriented Programming')
        due1.send_keys('Homework 1')
        lecture2.send_keys('Week 3')
        material2.send_keys('Data Structures')
        due2.send_keys('Exam & Homework 2')
        lecture3.send_keys('Week 4')
        material3.send_keys('Algorithms')
        due3.send_keys('Homework 3')
        lecture4.send_keys('Week 5')
        material4.send_keys('Review')
        due4.send_keys('Final Exam')


        #submit page 16/17
        submit.send_keys(Keys.RETURN)

        #################################################### PAGE 17 ####################################################
        #find elements for page 17/17
        inclement_weather = selenium.find_element_by_id('id_17-inclement_weather')

        submit = selenium.find_element_by_id('submit')
        time.sleep(2) 

        #populate the form with data for page 17/17
        inclement_weather.send_keys('Any work or test due on a class date that has been canceled due to inclement weather will be due the next class meeting.'\
            ' (If the semester\'s last exam is postponed, it will be given during the time period assigned during the University\'s official Final Exam week.')


        #submit page 17/17
        submit.send_keys(Keys.RETURN)

  #test that the welcome for the wizard work by not importing data and going directly to wizard
    def testWelcomePageNoImport(self):
        selenium = webdriver.Chrome(executable_path='/Users/gersonkroiz/Downloads/chromedriver')

        #choose url to use
        selenium.get('http://127.0.0.1:8000/syllabus_form/')

        #find elements
        search = selenium.find_element_by_id('search')
        goto = selenium.find_element_by_id('goto')
        course = selenium.find_element_by_id('id_course')

        time.sleep(1)

        goto.send_keys(Keys.RETURN)

        #we see that this leads directly to wizard
        time.sleep(3)



        

    