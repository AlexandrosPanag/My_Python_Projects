"""
FAQ KNOWLEDGE BASE - GREEK
===========================
This file contains all predefined FAQ entries in Greek.
Each FAQ entry consists of:
- questions: List of question variations that users might ask
- answer: The response to provide for those questions
To add a new FAQ:
1. Add a new dictionary with 'questions' and 'answer' keys
2. Include multiple question variations to improve matching
3. Restart the chatbot to reload the knowledge base
"""
"""
FAQ KNOWLEDGE BASE - GREEK (Chunked for Better RAG Context)
============================================================
This file contains FAQ entries organized into semantic chunks for
improved
retrieval accuracy in RAG systems.
Each chunk contains related FAQs that share context, making it easier
for
the system to retrieve relevant information together.
"""
#
==============================================================================
# CHUNK 0: GREETINGS & GENERAL HELP
# Context: User greetings, general questions, platform overview
#
==============================================================================
CHUNK_GREETINGS = [
{
'chunk_id': 'greet_001',
'chunk_topic': 'Greeting and introduction',
'questions': [
"Hi",
"Hello",
"Hey",
"Good morning",
"Good afternoon",
"Good evening",
"Greetings",
"What can you do?",
"How can you help me?",
"What is this?",
"Help"
],
'answer': "Hello! 👋 I'm your **Open eClass LMS Assistant**
powered by TRUE RAG (Retrieval-Augmented Generation) with Phi-3
AI.\n\n**I can help you with:**\n• Account creation and login\n•
Course enrollment and navigation\n• Assignments and exercises\n•
Communication tools (forums, messages)\n• Calendar and scheduling\n•
Documents and multimedia\n• Technical support\n\n**Just ask me
anything about Open eClass!** I'll search through documentation,
FAQs, and use AI to give you the best answer.\n\n**Tip:** You can
toggle between English 🇬🇧 and Greek 🇬🇷 using the language button."
}
]
#
==============================================================================
# CHUNK 1: AUTHENTICATION & ACCOUNT CREATION
# Context: User login, registration, and password recovery
#
==============================================================================
CHUNK_AUTHENTICATION = [
{
'chunk_id': 'auth_001',
'chunk_topic': 'Login to the platform',
'questions': [
"How do I log in?",
"How do I sign in?",
"How do I login?",
"How do I access the platform?",
"Login process",
"System access"
],
'answer': "User Login:\n\nAfter you have created an account on the
Open eClass platform (either as an Instructor or Student), each time you
visit the platform you must follow the steps below:\n\n1) On the
homepage, enter your Username\n2) Enter your personal Password\n3)
Click the login button\n\nThis way you will have access to all
features of the Open eClass platform.\n\n**Forgot your
password?**\nIf you have forgotten your password, you can recover it
simply by selecting 'Forgot your password?' and following the
instructions. Note: these instructions will be sent to the email address
you provided."
},
{
'chunk_id': 'auth_002',
'chunk_topic': 'Account Creation - General',
'questions': [
"How do I create an account?",
"How do I register?",
"Account creation",
"Registration process",
"New account"
],
'answer': "To assist you better, could you please clarify:\n\n• Do
you want to create a **Student/Learner Account**?\n• Or a
**Teacher/Instructor Account**?\n\nPlease specify which type of
account you need and I will provide detailed registration
instructions."
},
{
'chunk_id': 'auth_003',
'chunk_topic': 'Instructor Account Creation',
'questions': [
"How do I create a teacher account?",
"How do I create an instructor account?",
"Instructor account creation",
"Teacher registration",
"Instructor account request"
],
'answer': "Instructor Account Creation\n\nTo obtain a new
instructor account on the platform, follow the steps below:\n\n1)
Select the 'Register' link from the platform's homepage.\n\n2) Then
select 'Create New Account' and you will be taken to the registration
form.\n\n3) In the form, you must fill in the corresponding
details.\n\n4) More specifically, you must provide:\n - Your personal
details: First name, Last name, Email address\n - The desired username
with which the system will identify you\n - From the 'Category'
field, choose the School or Department you belong to\n - Finally,
select 'Register' to complete your registration\n\nPlease
note:\nThe system will send a message to the email address you provided
in the form. Once you receive the message, you must confirm your email
address by following the link included in the message."
},
{
'chunk_id': 'auth_004',
'chunk_topic': 'Student Account Creation',
'questions': [
"How do I create a student account?",
"How do I create a learner account?",
"Student account creation",
"Student registration",
"Student account request"
],
'answer': "Student Account Creation:\n\nTo obtain a new student
account on the platform, follow the steps below:\n\n1) Select the
'Register' link on the platform's homepage.\n2) Then select 'New
Account Request' under the 'Student Account' section.\n3) Enter your
details in the registration form:\n - Your personal details (First
name, Last name, Phone, Email)\n - The desired username and
password\n - Your student ID number or enrollment details (if
required)\n4) Click 'Submit Request'.\n\nImportant:\n- You will
receive a confirmation email at the address you provided.\n- Follow the
link in the email to activate your account.\n- After activation, you
can log in and access the courses."
}
]
#
==============================================================================
# CHUNK 2: STUDENT PORTFOLIO & NAVIGATION
# Context: Viewing courses, portfolio management, course
enrollment/unenrollment
#
==============================================================================
CHUNK_STUDENT_PORTFOLIO = [
{
'chunk_id': 'portfolio_001',
'chunk_topic': 'User portfolio and overview',
'questions': [
"What is the portfolio?",
"What is the user portfolio?",
"User portfolio what is it?",
"User portfolio description",
"What do I see when I log in?",
"What do I see right after login?",
"Homepage after login",
"Which page do I see when I enter username and password?",
"Portfolio overview"
],
'answer': (
"User Portfolio\n\n"
"Upon entering the platform (entering username and password), "
"you arrive at the **user portfolio**, a space that allows you to
"
"organize and manage your participation in the platform's online
courses.\n\n"
"In the portfolio you will see:\n\n"
"• The courses you are enrolled in (link **\"My
courses\"**).\n"
" For courses in which you are registered, the option "
" **\"Unenroll\"** appears on the right so you can remove them
from your list if you wish.\n\n"
"• On the **right side** of the screen there are options
concerning:\n"
" -- Course enrollment\n"
" -- Editing your profile\n"
" -- Your personal course calendar\n\n"
"• On the **left side** of the screen, various links appear "
"(Courses, Manuals, Communication, etc.) related to the overall "
"view of your portfolio and profile on the platform.\n\n"
"Finally, by clicking the title of a course from the course list, "
"you enter the corresponding online course.\n\n"
"For more information see:\n"
"https://docs.openeclass.org/en/student/portfolio"
)
},
{
'chunk_id': 'portfolio_002',
'chunk_topic': 'Course viewing',
'questions': [
"My courses",
"Where can I find my courses?",
"How can I see the courses I attend?",
"Course list",
"Where are my courses?",
"User portfolio",
"Viewing courses",
"Course display"
],
'answer': "My Courses\n\nTo see which courses you are enrolled in
you have two options:\n\n1. From the home screen:\nWhen you have
logged in to eClass, the user portfolio automatically appears with the
list of courses you are enrolled in.\n\n2. From the \"My courses\"
menu:\nIt is located in the dropdown menu in the upper-right corner of
your screen.\n\nInformation displayed:\nIn this area you will see all
the courses you participate in. Each course shows:\n• Course title\n•
Instructor names\n• Management options (Unenroll, Favorites)\n\n📚
For more information, visit:
https://docs.openeclass.org/en/student/portfolio/my_courses"
},
{
'chunk_id': 'portfolio_003',
'chunk_topic': 'Unenrolling from a course',
'questions': [
"How do I unenroll from a course?",
"How do I withdraw from a course?",
"Delete course",
"Remove from course",
"How do I stop attending a course?",
"Course unenrollment",
"How to leave a course?",
"How to remove myself from a course?",
"Unenroll from course"
],
'answer': "Unenrolling from a Course\n\nHow to unenroll:\n\nIn
the courses in which you are enrolled, you have the option to select
\"Unenroll\" so you can withdraw from the course.\n\nSteps:\n1.
Go to your course list (from the homepage or from the \"My courses\"
menu)\n2. Locate the course you want to unenroll from\n3. Select the
\"Unenroll\" option shown for that course\n4. Confirm your
action\n\nImportant:\n• Unenrolling removes the course from your
list\n• You will no longer have access to the course content\n• You
may re-enroll later if the course is open\n\n📚 For more information,
visit: https://docs.openeclass.org/en/student/portfolio/my_courses"
},
{
'chunk_id': 'portfolio_004',
'chunk_topic': 'Favorite courses',
'questions': [
"How do I mark a course as favorite?",
"How do I set a course as favorite?",
"Favorite courses",
"How do I add a course to favorites?",
"Mark course as favorite",
"How do I add a star to a course?",
"Course priority",
"How do I place a course at the top?",
"Favorite courses",
"Star courses"
],
'answer': "Marking a Course as Favorite\n\nA new feature available
to the user profile is the ability to mark courses you are enrolled in
as \"Favorites\".\n\nHow to mark a course as favorite:\n\n1.
Display your course list using one of the two methods:\n • From the
eClass home screen (user portfolio)\n • From the \"My courses\"
menu (upper-right corner)\n\n2. Click the star icon next to the course
you want\n\n3. The icon will turn into a colored star (★) and the
course will move to the top of your list\n\nAdvantages:\n• Quick
access to the courses you use most frequently\n• Favorite courses
appear first when you enter eClass\n• Better organization of your
courses\n\nHow to remove a course from favorites:\nSimply click the
star (★) again so the course returns to its original position in the
list.\n\n📚 For more information, visit:
https://docs.openeclass.org/en/student/portfolio/my_courses"
},
{
'chunk_id': 'portfolio_005',
'chunk_topic': 'Personal blog',
'questions': [
"What is the blog?",
"What is My Blog?",
"How does the blog work?",
"Where can I find the blog?",
"How do I write on the blog?",
"How do I view my personal blog?",
"Platform blog",
"How do I comment on a blog post?",
"How do I rate a blog post?"
],
'answer': (
"My Blog\n\n"
"The \"My Blog\" subsystem (known as a blog) is a type of webpage
that displays content in chronological order, with the most recent
entries appearing at the top. "
"Usually, a blog consists of text posts related to the courses you are
enrolled in. "
"Your personal blog is accessible through your profile by clicking the
\"Personal blog\" option.\n\n"
"Registered users of the platform can comment on one of your blog posts
simply by clicking the comments link.\n\n"
"Finally, platform users can rate one of your posts positively or
negatively.\n\n"
"For more information see here:\n"
"https://docs.openeclass.org/en/student/portfolio/my_blog"
)
}
]
#
==============================================================================
# CHUNK 3: ASSIGNMENTS & SUBMISSIONS
# Context: Assignment submission, Turnitin plagiarism check
#
==============================================================================
CHUNK_ASSIGNMENTS = [
{
'chunk_id': 'assignments_001',
'chunk_topic': 'Assignment submission',
'questions': [
"How do I submit an assignment?",
"Where do I upload my assignment?",
"How do I upload an assignment?",
"Assignment submission steps",
"Exercise submission process"
],
'answer': "To submit an assignment: 1) Navigate to the
'Assignments' section in your course, 2) Click the title of the
specific assignment, 3) Click the 'Submit Assignment' button, 4)
Upload your file or paste your text, 5) Click 'Submit' to complete.
Check the deadline before submitting!"
},
{
'chunk_id': 'assignments_002',
'chunk_topic': 'Plagiarism check / Turnitin',
'questions': [
"What is plagiarism check?",
"What is Turnitin?",
"Plagiarism check",
"How does Turnitin work?",
"How is plagiarism check performed?",
"How do I submit an assignment to Turnitin?",
"How do I view the similarity of my assignment?",
"Turnitin platform",
"Assignment plagiarism detection",
"How do I submit to Turnitin?"
],
'answer': (
"Plagiarism Check / Turnitin\n\n"
"Turnitin is a software system for detecting duplication and plagiarism
in academic assignments. "
"With Turnitin integrated into the open eClass platform, the course
instructor can check whether the assignments uploaded by students are
their own work or the result of copying.\n\n"
"Students prepare their assignments, and Turnitin compares their
content against its databases and other sources. "
"This allows the instructor to determine whether the submitted work is
plagiarized.\n\n"
"To upload a new assignment with Turnitin enabled, you must first
accept the terms as defined by Turnitin.\n\n"
"Then, select the \"Upload Assignment\" link and locate your
assignment file on your local disk. "
"Accepted formats include: MS WORD, MS PowerPoint, Postscript PDF, RTF,
HTML, WordPerfect. "
"After locating the file, enter your assignment title and then select
the \"Upload and Review\" link.\n\n"
"At this stage, you can preview the assignment before submitting it or
cancel the process using the appropriate control screen. "
"To make the final submission, select the \"Submit to Turnitin\"
link.\n\n"
"After submitting your assignment to Turnitin, you can view the
similarity percentage it has compared to Turnitin's databases. "
"Additionally, through the \"ALL Sources\" option you can view the
sources from which similarities originate. "
"Turnitin highlights in red the part of your assignment that matches
its databases. "
"After submission, you can also check the grade assigned by the
instructor and download your submitted file to your local disk.\n\n"
"For more information see here:\n"
"https://docs.openeclass.org/en/student/assignments/turnitin"
)
}
]
#
==============================================================================
# CHUNK 4: COURSE CONTENT & MATERIALS
# Context: Documents, announcements, course materials
#
==============================================================================
CHUNK_COURSE_CONTENT = [
{
'chunk_id': 'content_001',
'chunk_topic': 'Course announcements',
'questions': [
"What are announcements?",
"How do I view announcements?",
"Important announcement?",
"Where can I find the announcements?",
"Course announcements",
"Announcements update",
"How do I get notified about news?",
"How do I view an important announcement?",
"Where do announcements appear?"
],
'answer': (
"Announcements\n\n"
"The \"Announcements\" subsystem allows the instructor to inform
registered users about issues related to the specific course. "
"Through this subsystem, you can stay updated on all actions and
activities announced by the instructor.\n\n"
"Each announcement shows the title, the posting date, and a distinctive
red icon marking it as important.\n\n"
"This icon appears on every announcement that has been marked as
important and is \"pinned\" at the top of the announcements
list.\n\n"
"For more information see here:\n"
"https://docs.openeclass.org/en/student/announcements"
)
},
{
'chunk_id': 'content_002',
'chunk_topic': 'Documents and educational material',
'questions': [
"What are the documents?",
"Access to documents?",
"Where can I find the documents?",
"How do I view the documents?",
"How do I download documents?",
"Course documents",
"Educational material",
"How do I save a file?",
"How do I open a document?"
],
'answer': (
"Documents\n\n"
"The \"Documents\" subsystem is the space where the course's
educational material is stored, organized, and presented. "
"In this subsystem, you can find available texts, notes, presentations,
images, diagrams, etc., organized in a system of folders and
subfolders.\n\n"
"Depending on the instructor's organization, the available files may be
grouped into folders. "
"You can use this subsystem like a traditional file manager.\n\n"
"To open and view a specific file, simply click on the file title. "
"If you wish to download and save a file to your local computer, select
the \"Save\" link.\n\n"
"It is possible that an explanatory comment appears under the file
name, helping you understand its contents without needing to open it
first.\n\n"
"For more information see here:\n"
"https://docs.openeclass.org/en/student/documents"
)
}
]
#
==============================================================================
# CHUNK 5: USER GROUPS & COLLABORATION
# Context: Group enrollment, group discussions, group work
#
==============================================================================
CHUNK_USER_GROUPS = [
{
'chunk_id': 'groups_001',
'chunk_topic': 'User group overview',
'questions': [
"User groups",
"What are user groups?",
"What is a user group?",
"How do groups work?",
"User groups",
"Group work",
"Collaboration in groups",
"What do groups do?",
"Why are groups needed?",
"Information about user groups"
],
'answer': "User Groups\n\n**What User Groups Are:**\n\nBetter
collaboration and interaction between learners and the course instructor
can be achieved through the user group
subsystem.\n\n**Features:**\n\nSuch a group consists of a
collection of registered course users who are able to:\n\n• Share the
same discussion area\n• Access the same documents\n• Collaborate on
the same group assignments\n• Communicate and coordinate more
effectively\n\n**Purpose:**\nUser groups facilitate group work,
collaboration, and interaction among group members.\n\n📚 For more
information,
visit:\nhttps://docs.openeclass.org/en/4.0/student/groups"
},
{
'chunk_id': 'groups_002',
'chunk_topic': 'Enrollment in a user group',
'questions': [
"How do I enroll in a user group?",
"How do I join a group?",
"Group enrollment",
"How do I enter a group?",
"Participation in a user group",
"Join group",
"How do I become a group member?",
"Group registration",
"How do I participate in a group?"
],
'answer': "Enrollment in a User Group\n\n**How to
enroll:**\n\nTo enroll in a new user group created by the course
instructor:\n\n**Steps:**\n1. Go to the course's \"User
Groups\" subsystem\n2. Find the group you want to join\n3. Select
the enrollment icon located on the right side of the screen\n4. Your
enrollment will be completed automatically\n\n**Important:**\n•
The instructor creates the user groups\n• After enrolling, you gain
access to all group tools\n• You can participate in discussions,
documents, and group assignments\n\n📚 For more information,
visit:\nhttps://docs.openeclass.org/en/4.0/student/groups"
},
{
'chunk_id': 'groups_003',
'chunk_topic': 'Unenrolling from a user group',
'questions': [
"How do I unenroll from a user group?",
"How do I leave a group?",
"Unenrollment from group",
"How do I exit a group?",
"Removal from user group",
"Leave group",
"How do I leave the group?",
"Delete from group",
"How do I stop being in a group?"
],
'answer': "Unenrolling from a User Group\n\n**How to
unenroll:**\n\nThe reverse process is followed when you are already
enrolled in a group and wish to leave it.\n\n**Steps:**\n1. Go to
the course's \"User Groups\" subsystem\n2. Find the group you want
to unenroll from\n3. Select the unenrollment icon located on the right
side of the screen\n4. After unenrolling, you will receive a
confirmation message\n\n**What happens next:**\n• You will no
longer have access to the group's discussions\n• You will not be able
to view the group's documents\n• You will not participate in group
assignments\n• You may re-enroll later if you wish\n\n📚 For more
information,
visit:\nhttps://docs.openeclass.org/en/4.0/student/groups"
},
{
'chunk_id': 'groups_004',
'chunk_topic': 'Enrollment and unenrollment in groups (combined)',
'questions': [
"Enrollment and unenrollment in groups",
"How do I join or leave a group?",
"Managing group participation",
"Join or leave group",
"Group enrollment unenrollment"
],
'answer': "Enrollment / Unenrollment in User Groups\n\n**Enroll
in a Group:**\nTo enroll in a new user group created by the course
instructor, simply select the enrollment icon at the right edge of the
subsystem screen.\n\n**Unenroll from a Group:**\nFollow the
reverse process when you want to leave a group. After unenrolling, you
will receive a success message.\n\n**Quick Steps:**\n1. Go to the
\"User Groups\" subsystem\n2. For enrollment: Click the enrollment
icon next to the group\n3. For unenrollment: Click the unenrollment
icon next to your group\n\n📚 For more information,
visit:\nhttps://docs.openeclass.org/en/4.0/student/groups"
},
{
'chunk_id': 'groups_005',
'chunk_topic': 'Group discussions',
'questions': [
"How do I create a topic in discussions?",
"How do I create a new discussion topic?",
"Group discussions",
"How do I start a discussion in the group?",
"New discussion topic",
"Group forum",
"How do I write in discussions?",
"Create post in group",
"How do I reply to a discussion?",
"Reply to discussion topic"
],
'answer': "Creating a Topic in Group Discussions\n\nWithin a user
group, you can participate in the group's discussions.\n\n**To
create a new topic:**\n\n1. Select the \"Discussions\" link
within your group\n\n2. Select the \"New topic\" link\n\n3.
Enter:\n • The topic title\n • The message body (main content)\n\n4.
Select \"Submit\" to save the new topic\n\n**To reply to an
existing topic:**\n\n1. Locate the topic you wish to reply
to\n\n2. Select the \"Reply\" link\n\n3. Enter the body of your
message\n\n4. Select \"Submit\" to complete the
process\n\n**Useful Tips:**\n• Use descriptive titles for your
topics\n• Keep discussions relevant to the group's subject\n• Reply to
existing topics instead of creating new ones on the same subject\n\n📚
For more information,
visit:\nhttps://docs.openeclass.org/en/4.0/student/groups/forum"
}
]
#
==============================================================================
# CHUNK 6: COURSE MANAGEMENT (TEACHER) - COMPLETED
# Context: Course settings, user management, permissions
#
==============================================================================
CHUNK_COURSE_MANAGEMENT = [
{
'chunk_id': 'management_002',
'chunk_topic': 'Course settings',
'questions': [
"Course management settings",
"Course tools settings",
"How do I change the course settings?",
"Course access type",
"Course deletion",
"Course backup",
"Course renewal",
"Settings",
"How do I make a backup of the course?"
],
'answer': """Course Management Settings
The "Settings" subsystem allows you to modify some basic operating
parameters of the online Course.
**Editing Course Identity:**
• Course title
• Instructor names
• School/Department
• Course code
• Interface language
**Access Type:**
• Open: Free access without registration
• Registration Required: Users must enroll
• Closed: Only invited users
**Course Management:**
• Create course backup
• Renew course for a new semester
• Delete course
• Visibility settings
📚 For more information:
https://docs.openeclass.org/en/teacher/course_management"""
},
{
'chunk_id': 'management_003',
'chunk_topic': 'Course user management',
'questions': [
"User management",
"How do I add a user to the course?",
"How do I remove a user from the course?",
"User enrollment",
"User unenrollment",
"User roles",
"User permissions",
"Course user list"
],
'answer': """Course User Management
The "Users" subsystem allows you to manage the registered users in
your course.
**User Overview:**
• List of all enrolled students
• List of instructors and assistants
• Contact information
**Adding Users:**
1. Select "Add User"
2. Search for the user by username or email
3. Select the role (Student, Assistant, Instructor)
4. Confirm the addition
**Removing Users:**
• Select the user from the list
• Click the delete icon
• Confirm the removal
**User Roles:**
• Instructor: Full management permissions
• Assistant: Limited management permissions
• Student: Viewing and participation permissions
📚 For more information:
https://docs.openeclass.org/en/teacher/users"""
}
]
#
==============================================================================
# CHUNK 7: COMMUNICATION TOOLS
# Context: Announcements, forums, messaging, notifications
#
==============================================================================
CHUNK_COMMUNICATION = [
{
'chunk_id': 'communication_001',
'chunk_topic': 'Discussion areas',
'questions': [
"What are discussion areas?",
"Course forum",
"How do forums work?",
"Course discussions",
"How do I create a discussion topic?",
"How do I reply to a discussion?",
"Discussion board",
"Discussion area"
],
'answer': """Discussion Areas
Discussion Areas (Forums) are spaces for asynchronous communication
between instructors and students.
**Features:**
• Organized thematic categories
• Creation of new discussion topics
• Replies to existing topics
• Attached files
• Notifications for new posts
**Creating a New Topic:**
1. Select the appropriate category
2. Click "New Topic"
3. Enter title and text
4. Add files (optional)
5. Submit the topic
**Replying to a Topic:**
1. Open the discussion topic
2. Click "Reply"
3. Write your response
4. Submit
**Best Practices:**
• Use descriptive titles
• Keep discussions relevant
• Respect other participants
• Avoid duplicate posts
📚 For more information:
https://docs.openeclass.org/en/student/forums"""
},
{
'chunk_id': 'communication_002',
'chunk_topic': 'Messages and notifications',
'questions': [
"Messages",
"How do I send a message?",
"Notifications",
"How do I check my messages?",
"Inbox",
"Private messages",
"How do I reply to a message?",
"Platform correspondence"
],
'answer': """Messages and Notifications
The messaging system allows direct communication between platform users.
**Sending a Message:**
1. Click the messages icon (top right)
2. Select "New Message"
3. Choose recipient(s)
4. Write the subject and text
5. Send
**Receiving Messages:**
• Platform notification (red indicator)
• Email notification (optional)
• Access through the messages icon
**Types of Notifications:**
• New course announcements
• New forum posts
• Assignment grades
• Assignment deadlines
• Private messages
**Notification Settings:**
You can customize notifications from your profile:
• Choose notification types
• Email or platform-only notifications
• Delivery frequency
📚 For more information:
https://docs.openeclass.org/en/student/messages"""
}
]
#
==============================================================================
# CHUNK 8: ASSESSMENTS & GRADING
# Context: Tests, quizzes, exercises, grading
#
==============================================================================
CHUNK_ASSESSMENTS = [
{
'chunk_id': 'assessment_001',
'chunk_topic': 'Exercises and Tests',
'questions': [
"What are exercises?",
"How do I do exercises?",
"Quiz",
"Assessment test",
"Online exams",
"How do I start a test?",
"How do I submit a test?",
"Online quiz",
"Self-assessment exercises"
],
'answer': """Exercises and Assessment Tests
Exercises and tests are tools used to assess student knowledge.
**Types of Exercises:**
• Multiple choice
• True/False
• Fill in the blanks
• Matching
• Open-ended questions
**Taking a Test:**
1. Select the test from the list
2. Read the instructions carefully
3. Answer the questions
4. Submit your answers
5. View results (if available)
**Important Information:**
• Time limit (if applicable)
• Number of attempts
• Result availability
• Grading method
**Tips:**
• Check your internet connection
• Do not close the window during the test
• Save often (if possible)
• Watch the remaining time
📚 For more information:
https://docs.openeclass.org/en/student/exercises"""
},
{
'chunk_id': 'assessment_002',
'chunk_topic': 'Grading and evaluation',
'questions': [
"How do I see my grades?",
"Course grades",
"Assignment evaluation",
"Where can I see my grades?",
"Grades",
"Grade status",
"How am I graded?",
"Grading system"
],
'answer': """Grading and Evaluation
The grading system allows you to monitor your progress in the course.
**Viewing Grades:**
1. Go to the "Gradebook" subsystem
2. View your grades by activity:
• Assignments
• Tests/Exercises
• Participation
• Final grade
**Types of Evaluation:**
• Automatic (for multiple-choice tests)
• Manual (for assignments and open questions)
• Combined
**Displayed Information:**
• Grade per activity
• Submission date
• Grading date
• Instructor comments
• Course average
**Notifications:**
You receive notifications when:
• An assignment is graded
• Final grades are announced
• Instructor comments are added
📚 For more information:
https://docs.openeclass.org/en/student/gradebook"""
}
]
#
==============================================================================
# CHUNK 9: MULTIMEDIA & INTERACTIVE CONTENT
# Context: Videos, videoconference, H5P, interactive content
#
==============================================================================
CHUNK_MULTIMEDIA = [
{
'chunk_id': 'multimedia_001',
'chunk_topic': 'Multimedia and videos',
'questions': [
"Multimedia",
"Course video",
"How do I watch a video?",
"Multimedia",
"Video lectures",
"Audio files",
"Video viewing",
"Multimedia playback"
],
'answer': """Multimedia and Videos
The Multimedia subsystem provides access to audiovisual educational
material.
**Types of Multimedia:**
• Video lectures
• Recorded presentations
• Educational videos
• Podcasts
• Interactive multimedia
**Video Playback:**
1. Select the video from the list
2. The video plays in your browser
3. Use the playback controls:
• Pause/Play
• Volume
• Full screen
• Playback speed
**Downloading Multimedia:**
• Download the file for offline viewing
• Available in various resolutions
**Interactive Content:**
• In-video questions
• Notes at specific timestamps
• Chapters and bookmarks
📚 For more information:
https://docs.openeclass.org/en/student/multimedia"""
},
{
'chunk_id': 'multimedia_002',
'chunk_topic': 'Telecollaboration and Videoconference',
'questions': [
"Telecollaboration",
"Videoconference",
"Online meeting",
"BigBlueButton",
"How do I join a video conference?",
"Virtual classroom",
"Live session",
"How do I enter an online class?",
"Live lecture"
],
'answer': """Telecollaboration and Videoconference
The telecollaboration system allows the hosting of online meetings and
lectures.
**BigBlueButton:**
A videoconferencing platform integrated into eClass:
• Real-time video and audio
• Screen sharing
• Chat
• Interactive whiteboard
• Polls
**Joining a Session:**
1. Locate the meeting link
2. Click to join
3. Allow microphone/camera access
4. Participate in the session
**Participation Tools:**
• Enable/disable microphone
• Enable/disable camera
• Raise hand for questions
• Chat for written communication
• View shared screen
**Technical Requirements:**
• Stable internet connection
• Modern web browser
• Microphone and camera (optional)
• Headphones (recommended)
📚 For more information:
https://docs.openeclass.org/en/student/videoconference"""
},
{
'chunk_id': 'multimedia_003',
'chunk_topic': 'H5P interactive content',
'questions': [
"H5P",
"Interactive content",
"Interactive content",
"How do I play H5P?",
"Interactive videos",
"Interactive exercises",
"H5P activities"
],
'answer': """H5P Interactive Content
H5P is a tool for creating interactive educational content.
**Types of Interactive Content:**
• Interactive videos with questions
• Presentations with quizzes
• Memory games
• Drag-and-drop exercises
• Timelines
• Virtual tours
• Flashcards
**Using H5P Content:**
1. Select the H5P activity
2. Interact with the content
3. Answer the questions (if any)
4. Receive immediate feedback
**Advantages:**
• Immediate feedback
• Gamification elements
• Self-regulated learning
• Engaging experience
• Better knowledge retention
**Progress Tracking:**
• Your answers may be recorded
• You can view your results
• Activities may be repeatable
📚 For more information:
https://docs.openeclass.org/en/student/h5p"""
}
]
#
==============================================================================
# CHUNK 10: CALENDAR & SCHEDULING
# Context: Course calendar, deadlines, events
#
==============================================================================
CHUNK_CALENDAR = [
{
'chunk_id': 'calendar_001',
'chunk_topic': 'Course calendar',
'questions': [
"Calendar",
"Calendar",
"How do I view the calendar?",
"Assignment deadlines",
"Deadlines",
"Course events",
"When is the assignment due?",
"Course schedule",
"Events"
],
'answer': """Course Calendar
The Calendar displays all important dates and events related to the
course.
**Types of Events:**
• Assignment submission deadlines
• Exam/test dates
• Lectures and meetings
• Educational events
• Personal reminders
**Viewing the Calendar:**
1. From the menu, select "Calendar"
2. View events in:
• Daily view
• Weekly view
• Monthly view
**Filters:**
• All courses
• Specific course
• Event type
• Time period
**Notifications:**
• Email reminder before the event
• Platform notification
• Option to customize reminder time
**Synchronization:**
• Export to iCal/Google Calendar
• Import to personal calendar
• Automatic syncing
📚 For more information:
https://docs.openeclass.org/en/student/calendar"""
}
]
#
==============================================================================
# CHUNK 11: PROFILE & PERSONAL SETTINGS
# Context: User profile, preferences, personal information
#
==============================================================================
CHUNK_PROFILE = [
{
'chunk_id': 'profile_001',
'chunk_topic': 'User profile',
'questions': [
"Profile",
"Profile",
"How do I change my profile?",
"Personal information",
"Edit profile",
"Profile photo",
"How do I update my details?",
"User information"
],
'answer': """User Profile
Your profile contains your personal information and settings.
**Editing Your Profile:**
1. Click your name (top right)
2. Select "Profile"
3. Click "Edit"
4. Update your details
5. Save the changes
**Profile Information:**
• First and Last Name
• Email
• Phone
• Department/School
• Profile photo
• Biography
**Changing Profile Photo:**
1. Go to your profile
2. Click the camera icon
3. Upload a new photo
4. Adjust it (crop)
5. Save
**Privacy:**
• Choose what others can see
• Email visible or hidden
• Phone visible or hidden
• Profile public or private
📚 For more information:
https://docs.openeclass.org/en/student/profile"""
},
{
'chunk_id': 'profile_002',
'chunk_topic': 'Password change',
'questions': [
"Change password",
"Password change",
"How do I change my password?",
"I forgot my password",
"Password reset",
"Recover password",
"Reset password",
"New password",
"Password recovery"
],
'answer': """Password Change
**Changing Your Password (when logged in):**
1. Go to your Profile
2. Select "Change Password"
3. Enter your current password
4. Enter your new password
5. Confirm the new password
6. Save
**Forgot Your Password?**
1. On the login page
2. Click "Forgot your password?"
3. Enter your email or username
4. Check your email
5. Follow the reset link
6. Create a new password
**Secure Password Requirements:**
• At least 8 characters
• Combination of letters and numbers
• At least one uppercase letter
• At least one special symbol (recommended)
**Security Tips:**
• Use a unique password
• Do not share your password
• Change it periodically
• Do not store it on insecure devices
📚 For more information:
https://docs.openeclass.org/en/student/profile"""
},
{
'chunk_id': 'profile_003',
'chunk_topic': 'Settings and preferences',
'questions': [
"Settings",
"Preferences",
"Settings",
"Preferences",
"How do I change my settings?",
"Interface language",
"Email notifications",
"Platform customization"
],
'answer': """User Settings and Preferences
**General Settings:**
1. Click your name
2. Select "Settings"
3. Adjust the options:
**Interface Language:**
• Greek
• English
• Other available languages
**Notification Settings:**
• Email for new announcements
• Email for messages
• Email for grades
• Email for deadlines
• Notification frequency (immediate/daily/weekly)
**Display Settings:**
• Interface theme (light/dark)
• Font size
• Content density
• Sidebar visibility
**Privacy Settings:**
• Who can see your profile
• Email visibility
• Phone visibility
• Activity history
**Calendar Settings:**
• First day of the week
• Time zone
• Date format
• Reminders
📚 For more information:
https://docs.openeclass.org/en/student/settings"""
}
]
#
==============================================================================
# CHUNK 12: COURSE ENROLLMENT
# Context: Finding courses, enrolling in courses, access codes
#
==============================================================================
CHUNK_ENROLLMENT = [
{
'chunk_id': 'enrollment_001',
'chunk_topic': 'Course enrollment',
'questions': [
"How do I enroll in a course?",
"How do I register for a course?",
"Enroll in a new course",
"How do I find courses?",
"Course search",
"How do I enter a course?",
"Enroll in course",
"Join a course"
],
'answer': """Course Enrollment
**Enrollment Steps:**
1. **Course Search:**
• From the homepage, select "Courses"
• Use the search engine
• Filter by School/Department
• Browse through categories
2. **Course Selection:**
• Click the course title
• View course information (description, instructors)
• Check the access type
3. **Enrollment:**
• Click "Enroll in Course"
• Enter enrollment key (if required)
• Confirm your enrollment
**Access Types:**
• **Open Course:** Immediate enrollment without approval
• **Course with Key:** Enrollment key required from the instructor
• **Closed Course:** Instructor approval required
**Enrollment Key:**
• Provided by the instructor
• May be visible in the course description
• Ask the instructor if you do not have it
**After Enrollment:**
• The course appears in your course list
• You gain full access to content
• You receive announcements and notifications
📚 For more information:
https://docs.openeclass.org/en/student/enrollment"""
},
{
'chunk_id': 'enrollment_002',
'chunk_topic': 'Course search',
'questions': [
"How do I find courses?",
"Course search",
"Search courses",
"Course catalog",
"Available courses",
"How do I search for a course?",
"Finding courses"
],
'answer': """Course Search
**Search Methods:**
**1. Keyword Search:**
• Use the search bar
• Enter title, code, or keywords
• View the results
**2. Browse by Category:**
• Select School or Department
• Browse courses in the category
• Apply additional filters
**3. Search Filters:**
• Access type (open/closed)
• Semester
• Instructor
• Department/School
• Language
**Course Information:**
For each course you can see:
• Title and code
• Short description
• Instructors
• Access type
• Number of enrolled users
• Last update
**Preview:**
• Click the course to see details
• View the content (if visible)
• Read learning objectives
**Favorites/Wishlist:**
• Add courses to wishlist
• Track courses of interest
• Enroll later
📚 For more information:
https://docs.openeclass.org/en/student/course_search"""
}
]
#
==============================================================================
# CHUNK 13: TECHNICAL SUPPORT & TROUBLESHOOTING
# Context: Common issues, browser requirements, technical help
#
==============================================================================
CHUNK_TECHNICAL = [
{
'chunk_id': 'technical_001',
'chunk_topic': 'Technical issues and support',
'questions': [
"Technical support",
"I have a problem",
"I can't log in",
"The system is not working",
"Technical issues",
"Help",
"Support",
"Assistance",
"Platform problem"
],
'answer': """Technical Support
**Common Issues:**
**1. Login Problems:**
• Check your username and password
• Ensure Caps Lock is off
• Clear your browser cache
• Try a different browser
**2. Slow Performance:**
• Check your internet connection
• Close other applications
• Refresh the page
• Try again later
**3. File Problems:**
• Check file size
• Check file type
• Try a different browser
• Compress large files
**4. Video/Audio Issues:**
• Check browser settings
• Allow autoplay
• Update your browser
• Try a different device
**Supported Browsers:**
• Google Chrome (latest version)
• Mozilla Firefox (latest version)
• Microsoft Edge (latest version)
• Safari (latest version)
**Contacting Support:**
If the problem persists:
1. Select "Contact" from the menu
2. Describe the issue in detail
3. Include screenshots (if possible)
4. Mention browser and operating system
📚 For more information:
https://docs.openeclass.org/en/support"""
},
{
'chunk_id': 'technical_002',
'chunk_topic': 'System requirements',
'questions': [
"System requirements",
"System requirements",
"What do I need?",
"Which browser should I use?",
"Technical specifications",
"Compatibility",
"How do I use the platform?"
],
'answer': """System Requirements
**Minimum Requirements:**
**Browser:**
• Google Chrome 90+
• Mozilla Firefox 88+
• Microsoft Edge 90+
• Safari 14+
• Opera 76+
**Operating System:**
• Windows 10 or newer
• macOS 10.14 or newer
• Linux (latest distributions)
• iOS 13+ (mobile)
• Android 8.0+ (mobile)
**Internet Connection:**
• Minimum: 2 Mbps
• Recommended: 5 Mbps+
• For videoconference: 10 Mbps+
**Hardware:**
• Processor: Dual-core 2 GHz+
• RAM: 4 GB minimum, 8 GB recommended
• Screen: 1024x768 minimum
**Extras for Videoconferencing:**
• Microphone
• Camera (optional)
• Headphones (recommended)
• Stable connection
**Browser Settings:**
• JavaScript enabled
• Cookies enabled
• Pop-ups allowed for the platform
• Autoplay enabled for videos
**Mobile App:**
Available for:
• iOS (App Store)
• Android (Google Play)
📚 For more information:
https://docs.openeclass.org/en/requirements"""
}
]
#
==============================================================================
# CHUNK 14: ADVANCED FEATURES
# Context: Badges, certificates, gamification, learning analytics
#
==============================================================================
CHUNK_ADVANCED = [
{
'chunk_id': 'advanced_001',
'chunk_topic': 'Badges and achievements',
'questions': [
"Badges",
"Badges",
"Achievements",
"Achievements",
"How do I earn badges?",
"What are badges?",
"Gamification",
"Rewards"
],
'answer': """Badges and Achievements
**What Badges Are:**
Badges are digital achievements you earn when you meet specific criteria
within a course.
**Types of Badges:**
• **Participation:** For active participation
• **Completion:** For completing activities
• **Achievement:** For success in exams
• **Collaboration:** For group work
• **Excellence:** For top performance
**How to Earn Badges:**
1. Complete assignments and exercises
2. Participate in discussions
3. Achieve high grades
4. Submit work on time
5. Collaborate with others
**Viewing Badges:**
• Go to your profile
• Select "My Badges"
• View earned badges
• View available badges
**Sharing:**
• Display on your profile
• Export to Mozilla Backpack
• Add to LinkedIn
• Showcase your skills
📚 For more information:
https://docs.openeclass.org/en/student/badges"""
},
{
'chunk_id': 'advanced_002',
'chunk_topic': 'Certificates of completion',
'questions': [
"Certificates",
"Certificates",
"How do I get a certificate?",
"Certificate of completion",
"Proof of completion",
"Attendance certificate"
],
'answer': """Certificates of Completion
**What Certificates Are:**
Official documents that certify the successful completion of a course.
**Requirements to Obtain a Certificate:**
• Completion of all required activities
• Achievement of minimum grade (e.g., 50%)
• Minimum attendance/engagement (if required)
• Submission of all assignments
**Downloading the Certificate:**
1. Successfully complete the course
2. Go to "My Profile"
3. Select "Certificates"
4. Download the certificate (PDF)
**Certificate Contents:**
• Learner's name
• Course title
• Completion date
• Grade (if shown)
• Instructor/institution signature
• Unique verification code
**Verification:**
• Each certificate has a unique code
• Verification via QR code
• Digital signature
• Online verification
**Uses of Certificates:**
• Professional portfolio
• Resume/CV
• LinkedIn profile
• Job applications
• Further studies
📚 For more information:
https://docs.openeclass.org/en/student/certificates"""
}
]
#
==============================================================================
# CHUNK 15: GLOSSARY & DEFINITIONS
# Context: Common terms and definitions used in the platform
#
==============================================================================
CHUNK_GLOSSARY = [
{
'chunk_id': 'glossary_001',
'chunk_topic': 'Glossary of terms',
'questions': [
"What does it mean?",
"Definition",
"Glossary",
"Term explanation",
"What is the...?",
"Glossary",
"Definitions"
],
'answer': """Glossary of Basic Terms
**eClass / Open eClass:**
Open Academic Online System for Asynchronous eLearning
**User Portfolio:**
Personal area where your courses and settings appear
**Announcements:**
Messages from instructors about important course-related topics
**Documents:**
Educational material (notes, presentations, files)
**Assignments:**
Tasks you must complete and submit
**Exercises/Quiz:**
Assessment tests with automatic or manual grading
**Forum / Discussion Areas:**
Spaces for asynchronous communication and discussion
**User Groups:**
Subgroups of students for group work and collaboration
**Multimedia:**
Videos, audio, and other audiovisual material
**Videoconference / Telecollaboration:**
Live online meetings via BigBlueButton
**Gradebook:**
Area where your grades are displayed
**H5P:**
Interactive educational content
**Badges:**
Digital achievements marking your progress
**Turnitin:**
Plagiarism detection system for assignments
📚 For the full glossary:
https://docs.openeclass.org/en/glossary"""
}
]
#
==============================================================================
# CHUNK 16: WIKIS & COLLABORATIVE EDITING
# Context: Wiki pages, collaborative content creation
#
==============================================================================
CHUNK_WIKI = [
{
'chunk_id': 'wiki_001',
'chunk_topic': 'Wiki and collaborative editing',
'questions': [
"What is the Wiki?",
"How does the Wiki work?",
"Course Wiki",
"How do I edit the Wiki?",
"Collaborative editing",
"How do I create a Wiki page?",
"Collaborative editing"
],
'answer': """Wiki - Collaborative Editing
**What the Wiki Is:**
The Wiki is a tool that allows participants in a course to collectively
create and edit content.
**Features:**
• Collaborative writing
• Version history
• Links between pages
• Multimedia content
• Content search
**Creating a New Page:**
1. Go to the course Wiki
2. Click "New Page"
3. Enter the title
4. Write the content
5. Format the text
6. Add images/links
7. Save
**Editing an Existing Page:**
1. Open the page
2. Click "Edit"
3. Make your changes
4. Add a comment describing the change
5. Save
**Formatting Tools:**
• Titles and subtitles
• Bold, italic, underline
• Lists (numbered, bullet)
• Tables
• Images and videos
• Hyperlinks
• Code blocks
**Version History:**
• View all previous versions
• Compare versions
• Restore previous version
• See who made changes
**Best Practices:**
• Write descriptive change comments
• Review before saving
• Respect the work of others
• Collaborate effectively
• Use clear structure
📚 For more information:
https://docs.openeclass.org/en/student/wiki"""
}
]
#
==============================================================================
# CHUNK 17: GLOSSARY (COURSE-SPECIFIC)
# Context: Course-specific glossary terms
#
==============================================================================
CHUNK_COURSE_GLOSSARY = [
{
'chunk_id': 'glossary_002',
'chunk_topic': 'Course glossary',
'questions': [
"Course glossary",
"Course definitions",
"Term dictionary",
"Course glossary",
"Technical terms",
"Course terminology"
],
'answer': """Course Glossary
**What the Course Glossary Is:**
A collection of definitions and explanations of terms related to the
specific course.
**Using the Glossary:**
1. Go to the course's "Glossary"
2. Search for a term
3. Browse alphabetically
4. Read the definition
**Features:**
• Alphabetical sorting
• Term searching
• Links to related terms
• Images and examples
• Pronunciation (if available)
**Contributing to the Glossary:**
Depending on settings, you may be able to:
• Add new terms
• Comment on definitions
• Rate definitions
• Suggest improvements
**Automatic Linking:**
• Glossary terms may appear automatically as links within the course
content
• Hover to preview the definition
• Click for full definition
**Exporting:**
• Print the glossary
• Export as PDF
• Download for offline use
📚 For more information:
https://docs.openeclass.org/en/student/glossary"""
}
]
#
==============================================================================
# CHUNK 18: E-PORTFOLIO
# Context: Student e-portfolio, showcasing work
#
==============================================================================
CHUNK_EPORTFOLIO = [
{
'chunk_id': 'eportfolio_001',
'chunk_topic': 'Electronic Portfolio (ePortfolio)',
'questions': [
"ePortfolio",
"Electronic portfolio",
"What is the ePortfolio?",
"How do I create a portfolio?",
"Showcase work",
"Show work"
],
'answer': """Electronic Portfolio (ePortfolio)
**What the ePortfolio Is:**
A personal digital space where you collect, organize, and present your
educational work.
**ePortfolio Contents:**
• Assignments and projects
• Certificates and badges
• Curriculum vitae (CV)
• Personal goals
• Reflective writing
• Creative work
• Achievements
**Creating an ePortfolio:**
1. Go to "ePortfolio"
2. Select "Create New"
3. Set a title and description
4. Add content:
- Text
- Files
- Images
- Videos
- Links
**Organization:**
• Create sections
• Categorize content
• Chronological order
• Thematic structure
**Privacy Settings:**
• Private (only you)
• Available to instructors
• Shared with classmates
• Public (everyone)
**Sharing:**
• Generate a unique URL
• Export to PDF
• Add to LinkedIn
• Share with employers
**Uses:**
• Academic assessment
• Professional development
• Job applications
• Self-assessment
• Learning reflection
📚 For more information:
https://docs.openeclass.org/en/student/eportfolio"""
}
]
#
==============================================================================
# CHUNK 19: LEARNING PATH & PROGRESS TRACKING
# Context: Learning paths, prerequisites, progress monitoring
#
==============================================================================
CHUNK_LEARNING_PATH = [
{
'chunk_id': 'learning_path_001',
'chunk_topic': 'Learning path and progress',
'questions': [
"Learning path",
"Learning path",
"Course progress",
"Prerequisites",
"Prerequisites",
"How do I view my progress?",
"Progress tracking",
"Completion status"
],
'answer': """Learning Path and Progress Tracking
**Learning Path:**
A structured sequence of activities and content that you must follow.
**Prerequisites:**
• Activities that must be completed first
• Minimum grade required to advance
• Specific order of modules
• Availability dates
**Progress Tracking:**
View your progress through:
1. **Progress Bar:**
• Completion percentage
• Visual representation
• Per module/activity
2. **Checklist:**
• Activity list
• Completed (✓)
• Pending
• Deadlines
3. **Learning Analytics:**
• Study time
• Access frequency
• Performance on exercises
• Comparison with class average
**Modules:**
• Locked (until prerequisites are completed)
• Open (currently accessible)
• Completed (finished)
**Progress Notifications:**
• Module completion
• New content unlocked
• Approaching goals
• Deadline reminders
**Certificate of Completion:**
• Awarded when all requirements are met
• Automatically generated
• Downloadable as PDF
**Tips:**
• Follow the recommended sequence
• Check your progress regularly
• Do not skip prerequisites
• Ask for help if you get stuck
📚 For more information:
https://docs.openeclass.org/en/student/learning_path"""
}
]
#
==============================================================================
# CHUNK 20: ATTENDANCE & PARTICIPATION
# Context: Attendance tracking, participation monitoring
#
==============================================================================
CHUNK_ATTENDANCE = [
{
'chunk_id': 'attendance_001',
'chunk_topic': 'Attendance and participation',
'questions': [
"Attendance",
"Attendance",
"How do I see my attendance?",
"Absences",
"Participation",
"Participation tracking",
"How is attendance recorded?"
],
'answer': """Attendance and Participation
**Attendance:**
System for recording attendance in lectures and activities.
**Types of Attendance:**
• Physical presence (for face-to-face sessions)
• Online presence (videoconference)
• Participation in activities
• Active participation (forums, chat)
**Attendance Recording:**
**Automatic:**
• Joining a videoconference
• Participating in a live session
• Completing required activities
**Manual:**
• Instructor records attendance
• QR code scanning
• Attendance code
**Viewing Attendance:**
1. Go to "Attendance"
2. View:
• Total attendance
• Total absences
• Attendance percentage
• By date/activity
**Participation Measurement:**
• Number of forum posts
• Assignment submissions
• Exercise completion
• Interaction with content
• Time spent on the platform
**Attendance Requirements:**
• Minimum attendance percentage (if applicable)
• Mandatory lectures
• Impact on final grade
• Option to justify absences
**Notifications:**
• Low-attendance warning
• Mandatory lecture reminder
• Attendance confirmation
**Absence Justification:**
(If permitted)
1. Select the absence
2. Submit justification
3. Attach supporting documents
4. Wait for approval
📚 For more information:
https://docs.openeclass.org/en/student/attendance"""
}
]
#
==============================================================================
# CHUNK 21: MOBILE APP
# Context: Mobile application usage, features, limitations
#
==============================================================================
CHUNK_MOBILE = [
{
'chunk_id': 'mobile_001',
'chunk_topic': 'Mobile application',
'questions': [
"Mobile app",
"Mobile application",
"iOS app",
"Android app",
"How do I download the app?",
"eClass mobile",
"Smartphone app",
"Tablet app"
],
'answer': """Open eClass Mobile Application
**Downloading the App:**
**iOS (iPhone/iPad):**
• App Store
• Search: "Open eClass"
• Free download
**Android:**
• Google Play Store
• Search: "Open eClass"
• Free download
**Features:**
• Access all courses
• Push notifications
• Offline viewing (saved content)
• Send messages
• Submit assignments
• Participate in forums
• View announcements
• Watch videos
**Login:**
1. Open the app
2. Enter the platform URL
3. Log in with username/password
4. The app saves your credentials
**Push Notifications:**
You receive instant notifications for:
• New announcements
• New messages
• Assignment deadlines
• Grades
• Forum replies
**Offline Mode:**
• Save documents for offline viewing
• Download videos
• Read announcements
• Write replies (sent when online)
**Limitations:**
• Some advanced features are available only on the web version
• Large files are better handled on a computer
• Videoconferencing is recommended on a computer
**Synchronization:**
• Automatic sync
• Real-time updates
• Sync across devices
**App Settings:**
• Notification management
• Video quality (WiFi/mobile data)
• Automatic file downloads
• Theme (light/dark)
📚 For more information:
https://docs.openeclass.org/en/mobile"""
}
]
#
==============================================================================
# CHUNK 22: H5P INTERACTIVE CONTENT
# Context: H5P activities, interactive learning materials
#
==============================================================================
CHUNK_INTERACTIVE_CONTENT = [
{
'chunk_id': 'interactive_001',
'chunk_topic': 'H5P interactive content creation',
'questions': [
"How do I create H5P content?",
"Create interactive content",
"H5P creation",
"Interactive learning objects",
"How to make interactive resources?",
"eClass interactive content"
],
'answer': """Creating Interactive H5P Content
The "Interactive Content" subsystem in the eClass platform is a tool for
creating interactive learning objects.
It consists of more than 40 types of educational resources and is based
on the open-source H5P platform.
**To create new interactive content:**
1. Go to the "Interactive Content" subsystem
2. Click the "Create" button
3. Select the desired H5P content type
4. Fill in the required fields and add your material
5. Save and preview your interactive object
H5P allows you to create quizzes, presentations, interactive videos,
games, timelines, matching activities, and much more.
📚 For additional guidance, explore official H5P examples and
documentation.
https://docs.openeclass.org/en/student/h5p/h5p_create"""
}
]
#
==============================================================================
# CHUNK 23: PERSONAL STATISTICS
# Context: User activity statistics, analytics, usage data
#
==============================================================================
CHUNK_PERSONAL_STATISTICS = [
{
'chunk_id': 'stats_001',
'chunk_topic': 'My statistics',
'questions': [
"My statistics",
"Personal statistics",
"User statistics",
"Where can I see my statistics?",
"Activity statistics",
"User stats",
"Student analytics"
],
'answer': """My Statistics
A learner can view their personal statistics through the link "My
Statistics".
After selecting it, they must define several criteria that affect how
the statistics will be displayed.
**Filtering Settings:**
1. **"From" and "To" fields:**
Define the start and end dates of the timeframe displayed.
2. **Display by month or by year:**
Choose how the statistics will be grouped.
**Displayed Statistics:**
After selecting the filters, the user can view:
• The total number of visits to the platform
• A chart showing their course preference percentages
• The total time spent in each course
• A table showing their most recent logins to the platform
These statistics provide a detailed overview of the learner's activity
and help track learning engagement and participation.
📚 For more information:
https://docs.openeclass.org/en/student/portfolio/personal_stats"""
}
]
#
==============================================================================
# CHUNK 24: QUESTIONNAIRES
# Context: Course questionnaires, surveys, feedback forms
#
==============================================================================
CHUNK_QUESTIONNAIRES = [{
'chunk_id': 'questionnaire_001',
'chunk_topic': 'Course questionnaires',
'questions': [
"Questionnaires",
"Course questionnaire",
"How do I complete a questionnaire?",
"Survey participation",
"Course survey",
"How to submit questionnaire?",
"eClass questionnaire"
],
'answer': """Questionnaires
The "Questionnaire" subsystem allows you to participate in course
questionnaires created by the instructor.
To participate in a questionnaire, simply click on its title. Then
proceed to answer the series of questions presented.
**Participating in Course Questionnaires:**
1. Select the questionnaire by clicking its title
2. Answer all the displayed questions
3. Review your answers if needed
**Submitting the Questionnaire:**
• Complete the process by clicking the "Submit" button
• After submission, the system displays the message "You have already
participated"
This confirms that your response has been recorded.
**Viewing Results:**
To view the results of the questionnaire, click the button located on
the right side of the screen.
📚 For more information:
https://docs.openeclass.org/en/student/questionnaire"""
}
]
#
==============================================================================
# CHUNK 25: CHAT / LIVE MESSAGING
# Context: Real-time messaging, chat rooms, communication with
instructor
#
==============================================================================
CHUNK_LIVE_MESSAGING = [
{
'chunk_id': 'chat_001',
'chunk_topic': 'Chat',
'questions': [
"Chat",
"How do I use the chat?",
"Live chat",
"Chat with instructor",
"How do I send a message in chat?",
"Course chat",
"Online chat",
"Live messaging"
],
'answer': """Chat
The "Chat" subsystem allows you to exchange messages in real time.
To participate in an existing chat created by the course instructor,
simply click on its title.
**Sending a Message:**
1. Type the text you want
2. Press the "Send" button
3. Your message will immediately appear in the chat
**New Feature -- Multiple Chat Rooms:**
A new feature has been added allowing the use of multiple separate chat
rooms.
This enables the creation of specialized communication spaces, such as:
• Chat with the instructor for resolving questions
• Scheduled communication hours with the instructor
• Group chat rooms for user groups
• Topic-specific discussion rooms
**Joining a New Chat:**
1. Select the link for the specific chat
2. Enter the chat room
3. Begin exchanging messages (questions -- answers) with the instructor
or classmates
The chat system provides immediate communication and helps with fast
clarification of questions.
📚 For more information:
https://docs.openeclass.org/en/student/chat"""
}
]
#
==============================================================================
# CHUNK 26: RECORDING
# Context: Audio recording messages, creating recorded greetings
#
==============================================================================
CHUNK_RECORDING = [
{
'chunk_id': 'recording_001',
'chunk_topic': 'Audio Recording Messages',
'questions': [
"What is recording?",
"How do I create a recording?",
"Recording",
"Course recording",
"How do I record a message?",
"Creating a recorded message",
"Recorded greeting",
"How do I record?",
"Audio recording eClass"
],
'answer': "Audio Recording Messages\n\nThrough the
\"Documents\" subsystem, course instructors have the ability to
create \"Recording\" files.\nThese files can be very useful for
creating recorded welcome messages for the course.\n\n**Steps to
Create a Recording:**\n\n1. **Start the Process:**\n • Go to
the \"Documents\" subsystem\n • Select the \"Recording\"
link\n\n2. **Enable Microphone:**\n • Click the \"Start\"
button\n • Accept microphone usage (you will be asked for
permission)\n • Make sure your microphone is working properly\n\n3.
**Perform Recording:**\n • Start speaking/recording\n •
**Maximum time:** 5 minutes per recording\n • You can see the timer
showing the time\n\n4. **Complete Recording:**\n • When finished,
click the \"Stop Recording\" button\n • Recording stops and is
saved temporarily\n\n5. **Save to Documents:**\n • Select
\"Save to Documents\"\n • Add a title for the recording\n • Add a
description (optional)\n • Confirm the save\n\n**Important
Notes:**\n\n**Release Microphone:**\nAfter completing the
recording, it would be good to use the \"Release Microphone\"
option.\nSome browsers keep the microphone locked even after recording
ends.\n\n**Benefits:**\n• Creating personalized welcome
messages\n• Recording instructions and explanations\n• Asynchronous
communication with added value\n• Better personal connection with
students\n\n**Typical Uses:**\n• Course welcome\n• Explanations
of difficult concepts\n• Feedback on assignments\n• Unit background
information\n• Study tips\n\n**Additional Tips:**\n• Test your
microphone before you start\n• Stay calm and speak clearly\n• Avoid
ambient noise\n• Plan what you will say in advance\n• Keep recordings
short (up to 5 minutes)\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/student/documents/rec_audio"
}
]
#
==============================================================================
# CHUNK 27: RUBRICS
# Context: Creating rubrics, grading criteria, assessment rubrics
#
==============================================================================
CHUNK_RUBRICS = [
{
'chunk_id': 'rubrics_001',
'chunk_topic': 'Assessment Rubrics',
'questions': [
"What are rubrics?",
"How do I create a rubric?",
"Rubrics",
"Assessment criteria",
"How do I grade with a rubric?",
"Assignment rubrics",
"Descriptive assessment",
"Rubric grading"
],
'answer': """Assessment Rubrics
**What Are Rubrics:**
A rubric is one of the most effective tools for assessing student
performance.
It is a type of descriptive assessment based on specific criteria and
quality gradations.
**Benefits of Rubrics:**
• Clear assessment criteria
• Objective grading
• Same criteria for everyone
• Clear process for students
• Facilitates feedback
• Favorable for group assignments
**Creating a Rubric - Steps:**
1. **Access the System:**
• In "Assignments" select the "Rubrics" link
• In the new window select "Create Rubric"
2. **Fill in Basic Information:**
• Rubric title (e.g., "Research Assignment Assessment")
• Rubric description (optional)
3. **Define Criteria:**
• Add at least one criterion
• For each criterion set:
- Criterion name (e.g., "Content", "Structure", "Spelling")
- Criterion description
- Levels (descriptions of performance levels)
- Values (e.g., Excellent=10, Good=8, Satisfactory=6, Inadequate=4)
- **Weight percentage** (e.g., 30%, 40%, 30%)
**Important Observations:**
**Grading Scale:**
• 100-point scale (0-100)
• Each criterion has its own values
**Weight Percentage:**
• The sum of all criteria weights must be **exactly 100%**
• Example with 1 criterion: 100%
• Example with 3 criteria: 30% + 40% + 30% = 100%
• **Attention:** The system will not accept a rubric if the sum ≠
100%
**Criterion Values:**
• The **maximum value** must be **the same for all criteria**
• This maximum value determines the maximum possible grade
• Example: If max value = 10 and we have 3 criteria with weights 30%,
40%, 30%
- Criterion A (30%): Excellent=10, Good=8, Satisfactory=6, Inadequate=4
- Criterion B (40%): Excellent=10, Good=8, Satisfactory=6, Inadequate=4
- Criterion C (30%): Excellent=10, Good=8, Satisfactory=6, Inadequate=4
**Example Rubric:**
\| Criterion \| Weight \| Excellent (10) \| Good (8) \| Satisfactory (6)
\| Inadequate (4) \|
\|-----------\|--------\|----------------\|----------\|-----------------\|----------------\|
\| Content \| 40% \| Very complete \| Complete \| Partially complete \|
Incomplete \|
\| Structure \| 35% \| Excellent organization \| Good organization \|
Fair organization \| Poor organization \|
\| Spelling \| 25% \| No errors \| 1-2 errors \| 3-5 errors \| 6+ errors
\|
\| **Total** \| **100%** \| \| \| \| \|
4. **Save Rubric:**
• Select "Save"
• The rubric is ready to use
**Using Rubric for Assessment:**
1. **When Creating an Assignment:**
• Select "Grading Type" = "Rubrics"
• Select the appropriate rubric from the dropdown menu
2. **When Grading:**
• Open the student submission
• Select a value for each criterion
• Add comments
• Grade is calculated automatically based on weights
**Calculating Final Grade:**
Final Grade = (Criterion A × 0.40) + (Criterion B × 0.35) + (Criterion C
× 0.25)
**Best Practices:**
• Create clear and specific criteria
• Use descriptive levels (not just numbers)
• Give equal weight to criteria or adjust accordingly
• Inform students of criteria in advance
• Check that the sum of weights = 100%
• Keep the maximum value the same for all criteria
📚 For more information:
https://docs.openeclass.org/en/teacher/assignments/rubrics"""
},
{
'chunk_id': 'rubrics_002',
'chunk_topic': 'Grading Assignments with Rubrics',
'questions': [
"How do I grade with a rubric?",
"How do I grade an assignment with a rubric?",
"Grading with rubric",
"Using rubric in assignment",
"Feedback with rubric",
"How do I give grades with criteria?"
],
'answer': """Grading Assignments with Rubrics
**Assigning a Rubric to an Assignment:**
1. **When Creating an Assignment:**
• In the "Grading Type" field select "Rubrics"
• From the dropdown menu select the appropriate rubric
• Save the assignment
**Grading Submission:**
1. **Opening Submissions:**
• Go to the "Assignments" subsystem
• Select the assignment
• View student submissions
2. **Evaluating Submission:**
• Click on the submission
• The rubric appears
• For each criterion:
- Read the performance level descriptions
- Select the appropriate performance level
- See the corresponding value
3. **Add Feedback:**
• Add comments for each criterion (optional)
• Write general comment (optional)
• This helps the student understand the grading
4. **Complete Grading:**
• Grade is calculated automatically
• System applies the weight percentages
• Save the grading
**Automatic Grade Calculation:**
Example with 3 criteria (40%, 35%, 25%):
- Criterion A: Level 8 × 40% = 3.2 points
- Criterion B: Level 10 × 35% = 3.5 points
- Criterion C: Level 6 × 25% = 1.5 points
- **Final Grade = 8.2 / 10**
**Student's View of Grading:**
Student sees:
• What grade they received for each criterion
• Instructor's comments
• Final grade
• Comparison with criteria (what it should have been)
**Instructor Benefits:**
• Faster and fairer grading
• Consistency in grading
• Clear documentation of assessment
• Time savings
**Student Benefits:**
• Understanding of assessment criteria
• Clear feedback
• Knowledge of what to improve
• Fairer assessment
**Tips:**
• Use one rubric per type of assignment
• Give students the rubric in advance
• Write helpful comments for improvement
• Be consistent in applying criteria
• Test the rubric on a small test first
📚 For more information:
https://docs.openeclass.org/en/teacher/assignments/rubric_grading"""
}
]
#
==============================================================================
# CHUNK 28: PEER REVIEW
# Context: Peer assessment, student evaluation, collaborative feedback
#
==============================================================================
CHUNK_PEER_REVIEW = [
{
'chunk_id': 'peer_review_001',
'chunk_topic': 'Peer Assessment',
'questions': [
"What is peer assessment?",
"Peer review",
"How does peer review work?",
"Peer assessment",
"Peer evaluation",
"Grading assignments by peers",
"How do I evaluate a peer's assignment?",
"Exchange feedback"
],
'answer': "Peer Assessment (Peer Review)\n\n**What Is Peer
Assessment:**\nPeer assessment (peer review) is the evaluation of
work by one or more people with similar abilities to the work's
creators.\n\nPeer review is used in learning management systems, where
learners can assess their peers' assignments.\n\n**Benefits of Peer
Review:**\n• Valuable educational exercise\n• Different ideas and
perspectives\n• Increased decision-making skills\n• Development of new
academic skills\n• Mutual feedback\n• Deeper understanding of the
subject\n• Critical thinking and analysis\n\n**Viewing Assignments
for Evaluation:**\n1. Go to the \"Assignments\" subsystem\n2.
Select an assignment with \"Peer Review\"\n3. Find the
\"Assignments to Evaluate\" section\n4. See your peers'
assignments\n\n**Evaluating an Assignment:**\n1. Open the
assignment to evaluate\n2. Read the content carefully\n3. Use the
assessment rubric:\n • Select a grade for each criterion\n • Write
comments and feedback\n • Give specific examples\n4. Submit the
evaluation\n\n**Receiving Feedback:**\n1. Wait for the evaluation
period to end\n2. Go to your assignment\n3. See your peers'
evaluations\n4. Read the comments and feedback\n5. Use them for
improvement\n\n**Important Dates:**\n• **Assignment Start
Date:** When it begins\n• **Submission Deadline:** When it
ends\n• **Evaluation Start:** When you can evaluate\n•
**Evaluation End:** When evaluation ends\n\n**Evaluation
History:**\nSee:\n• How many evaluations you received\n• Who
evaluated you\n• Overall comments\n• Assignment
results\n\n**Assignment Distribution:**\n• Automatic assignment
(3-5 evaluations per user)\n• Random peer selection\n• Equal workload
distribution\n• Avoid self-assessment\n\n**Good Evaluation
Practices:**\n• Read the entire assignment carefully\n• Know the
assessment criteria\n• Provide constructive feedback\n• Be objective
and fair\n• Mention positive and negative points\n• Suggest
improvements\n• Be respectful and professional\n\n**Tips:**\n•
Don't grade only with numbers\n• Write helpful and specific
comments\n• Follow the assessment rubric\n• Use polite language\n•
Give examples and suggestions\n• Respect your peer's effort\n\n📚
For more
information:\nhttps://docs.openeclass.org/en/student/assignments/peer_review"
},
{
'chunk_id': 'peer_review_002',
'chunk_topic': 'Creating Assignment with Peer Review',
'questions': [
"How do I create an assignment with peer review?",
"Creating peer assessment assignment",
"Setup peer review assignment",
"Assignment with mutual evaluation",
"How do I set peer review on an assignment?",
"Setting up peer assessment"
],
'answer': "Creating Assignment with Peer
Review\n\n**Prerequisite: Creating a Rubric**\n\nBefore creating
the assignment, you must create a rubric:\n\n1. **Access the
System:**\n • Go to the \"Assignments\" subsystem\n • Select the
\"Rubrics\" link\n • Click \"Create Rubric\"\n\n2. **Fill
in Rubric:**\n • Rubric title\n • Description\n • Define
criteria\n\n3. **Setting Criteria:**\n • Criterion name\n •
Description\n • Levels (performance levels)\n • Values (e.g.,
Excellent=10, Good=8, etc.)\n • **Weight percentage** (sum =
100%)\n\n**Example Weight Percentage:**\n- 1 criterion: 100%\n-
2 criteria: 50% + 50% = 100%\n- 3 criteria: 30% + 40% + 30% =
100%\n\n**Important:** System does not accept sum ≠ 100%\n\n4.
**Save Rubric:**\n • Select \"Save\"\n • Rubric is
ready\n\n**Creating Assignment with Peer Review**\n\n1.
**Access:**\n • Go to the \"Assignments\" subsystem\n • Click
\"Create Assignment\"\n\n2. **Fill in Basic Information:**\n
• Assignment title\n • Description and instructions\n\n3. **Select
Grading Type:**\n • In the \"Grading Type\" field\n • Select
**\"Peer Review\"**\n\n4. **Setting Peer Evaluation:**\n
• **Evaluations per user:** 3-5\n (How many students will evaluate
each assignment)\n • Select the rubric for evaluation\n\n5.
**Setting Dates (VERY IMPORTANT):**\n\n **Assignment Submission
Fields:**\n • **Start Date:** When it begins\n • **Submission
Deadline:** When it ends\n\n **Peer Evaluation Fields:**\n •
**Evaluation Start:** AFTER the submission deadline\n •
**Evaluation End:** When evaluation ends\n\n**ATTENTION - Date
Order:**\nCorrect date order must be:\n1. Start Date (first)\n2.
Submission Deadline (second)\n3. Evaluation Start (third - AFTER
deadline)\n4. Evaluation End (fourth)\n\nIf you set \"Evaluation
Start\" before \"Submission Deadline\" ends, the system will
reject saving!\n\n6. **Assignment Options:**\n • Automatic
assignment distribution\n • Equal workload distribution\n • Comments
(if allowed)\n\n7. **Final Submission:**\n • Click
\"Submit\"\n • Assignment is created\n\n**After
Creation:**\n\n1. **\"Assign Assignments\" Link
Appears:**\n • New link appears on the assignment\n • Click to
perform automatic assignment\n\n2. **Automatic Assignment:**\n •
System randomly distributes assignments\n • Each student receives 3-5
to evaluate\n • Avoids assigning their own work\n\n3. **View
Assignments:**\n • See who was assigned to whom\n • Track
progress\n\n4. **Transfer Grades:**\n • After evaluation period
ends\n • Click \"Transfer Grades\"\n • Select \"Record
Changes\"\n • Grades transfer to the assignment\n\n**View
Results:**\n• Peer grades\n• Instructor grades (if any)\n• Peer
comments\n• Evaluation history\n• Grade comparison\n\n**Best
Practices for Instructors:**\n• Use clear rubric\n• Provide student
preparation\n• Explain peer review importance\n• Teach critical
analysis\n• Set dates correctly\n• Monitor the process\n• Adjust
grades if needed\n\n**Tips:**\n• Test first with small group\n•
Communicate expectations\n• Provide examples of good evaluations\n•
Monitor feedback quality\n• Encourage constructive criticism\n\n📚
For more
information:\nhttps://docs.openeclass.org/en/teacher/assignments/peer_review"
}
]
#
==============================================================================
# CHUNK 29: ATTENDANCE TRACKING
# Context: Electronic attendance logs, managing attendance records
#
==============================================================================
CHUNK_ATTENDANCE_TRACKING = [
{
'chunk_id': 'attendance_tracking_001',
'chunk_topic': 'Attendance Log - Overview',
'questions': [
"What is an attendance log?",
"How do I create an attendance log?",
"Attendance log",
"Electronic attendance log",
"Creating an attendance log",
"Course attendance log",
"How do I track attendance?"
],
'answer': "Attendance Log - Overview\n\n**What Is an Attendance
Log:**\nThrough the \"Attendance\" subsystem, you have the
ability to create and manage a series of electronic attendance logs for
the course.\n\n**Creating a New Attendance Log:**\n1. Go to the
\"Attendance\" subsystem\n2. Select the \"New Attendance Log\"
link\n3. Fill in the following fields:\n • **Attendance Log
Title:** (e.g., \"Winter Semester Attendance Log\")\n • **Start
Date:** When the log begins\n • **End Date:** When the log
ends\n • **Number of Required Attendances:** (e.g., 8 attendance
out of 12 lectures)\n\n4. Confirm creation\n\n**Attendance Log
Features:**\n• Track student attendance\n• Set required number of
attendances\n• Link with activities/assignments\n• Automatic
attendance registration\n• Export to CSV format\n• User and group
management\n\n**Benefits:**\n• Electronic recording (no
paper)\n• Easier management\n• Automatic data processing\n• Immediate
access to statistics\n• Data export\n\n**Important:**\nThe
attendance log is a space for managing attendance that contains
activities, assignments, and exercises.\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/attendance"
},
{
'chunk_id': 'attendance_tracking_002',
'chunk_topic': 'Attendance Log Settings and Management',
'questions': [
"Attendance log settings",
"How do I change attendance log settings?",
"Modifying an attendance log",
"Editing an attendance log",
"Changing attendance log title",
"Changing required attendances"
],
'answer': "Attendance Log Settings and Management\n\n**Attendance
Log Functions:**\nA series of actions are available on the main
screen of the created attendance log:\n\n**1. Settings:**\nBy
selecting the \"Settings\" function you have the ability to
modify:\n • The title of the attendance log\n • The attendance log
start date\n • The attendance log end date\n • The number of required
student attendances\n\n**2. Students:**\nShows the students
participating in this specific attendance log\n • List of all enrolled
students\n • View attendance per student\n • Manage
participation\n\n**3. Add:**\nYou can add:\n • Activities (e.g.,
labs, lectures)\n • Assignments (submissions that record attendance)\n
• Exercises (online exercises that record attendance)\n\n**Process
of Modifying Settings:**\n1. Go to the attendance log\n2. Select
\"Settings\"\n3. Make the required changes\n4. Save the
changes\n\n**Important Settings:**\n\n**Attendance Log
Title:**\n• Use descriptive titles\n• Contains semester/period
information\n\n**Dates:**\n• Must cover the entire academic
semester\n• Connect with added subsystems\n\n**Number of Required
Attendances:**\n• Determines the minimum attendance threshold\n•
E.g., 8 out of 12 lectures\n• Can be used for grade
calculation\n\n**Best Practices:**\n• Create one attendance log
per semester\n• Set realistic required attendance number\n• Inform
students of requirements\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/attendance"
},
{
'chunk_id': 'attendance_tracking_003',
'chunk_topic': 'Adding Students to Attendance Log',
'questions': [
"How do I add students to an attendance log?",
"Adding students to attendance log",
"Importing users to attendance log",
"Which students are in the attendance log?",
"Adding user groups"
],
'answer': "Adding Students to Attendance Log\n\n**Access Student
Management:**\n1. Go to the attendance log\n2. Select the
\"Students\" link\n3. Select the \"here\" link\n\n**Three
Available Options:**\n\n**1. Add All Students:**\nTo include
all enrolled students from the course:\n • Set registration date
\"From\"\n • Set registration date \"To\"\n • Complete the
process by selecting the \"Update\" link\n • All students who
registered between these dates are added\n\n**2. Add Specific
Students:**\nTo import specific students:\n • Select the students
you want from the left column\n • Move them to the right column (drag
and drop or with transfer button)\n • Complete the process by selecting
the \"Update\" link\n\n**3. Add User Groups:**\nTo add all
members of specific groups:\n • Select the group or groups you want
from the left column\n • Move them to the right column\n • Complete
the process by selecting the \"Update\" link\n • All group members
are added to the attendance log\n\n**Student Management:**\n•
View student list\n• Add new students\n• Remove students\n• Export
student list\n\n**Important:**\nAfter adding students, you can
add activities, assignments, and exercises that will record
attendance.\n\n**Best Practices:**\n• Add all students at the
beginning of the semester\n• Use groups for easier management\n•
Update regularly when new students enroll\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/attendance"
},
{
'chunk_id': 'attendance_tracking_004',
'chunk_topic': 'Adding Activities, Assignments, and Exercises',
'questions': [
"How do I add an activity to the attendance log?",
"Adding an assignment to attendance log",
"Adding an exercise to attendance log",
"How do I connect activities with attendance log?",
"Automatic attendance registration"
],
'answer': "Adding Activities, Assignments, and Exercises\n\nAfter
students have been added to the attendance log, you can add a series of
\"subsystems\" which may be:\n• Activities\n• Assignments\n•
Exercises\n\n**1. Adding an Activity:**\n\nTo add an
activity:\n 1. Select the \"Add - Activity\" link\n 2. Set the
activity date\n 3. Provide relevant information (e.g., \"Lab
session\", \"Lecture 5\", etc.)\n 4. Complete the process by
selecting the \"Save\" link\n\n**Examples of Activities:**\n•
Lectures\n• Labs\n• Meetings\n• Seminars\n• Lab
exercises\n\n**2. Adding an Assignment:**\n\nTo add an
assignment to the attendance log:\n 1. Select the \"Add -
Assignment\" link\n 2. From the list of existing assignments select
the one you want\n 3. Assignment is added to the attendance
log\n\n**Automatic Attendance Registration:**\nYou can select the
\"Automatic Attendance Registration\" option\n • When the student
submits the assignment, attendance is automatically recorded\n •
Facilitates attendance management\n\n**Assignment Selection:**\n•
See available course assignments\n• Select those you want to connect
with attendance log\n• You can add multiple assignments\n\n**3.
Adding an Exercise:**\n\nTo add an exercise to the attendance
log:\n 1. Select the \"Add - Exercise\" link\n 2. From the list of
existing exercises select the one you want\n 3. Exercise is added to
the attendance log\n\n**Automatic Attendance
Registration:**\nSimilar to assignments:\n • When the student
completes the exercise, attendance is automatically recorded\n • Useful
for online exercises and quizzes\n\n**Exercise Selection:**\n•
See available course exercises\n• Select those you want to connect with
attendance log\n• You can add multiple exercises\n\n**Important -
Automatic Attendance Registration:**\nIt is emphasized that when
adding either an assignment or exercise to the attendance log, you can
select the \"Automatic Attendance Registration\" option.\n\nThis
means that:\n • When a student participates in an exercise or
assignment contained in this attendance log\n • The platform
automatically records their attendance\n • No manual recording is
needed\n\n**Benefits of Automatic Registration:**\n• Time
savings\n• Avoids errors\n• Objective recording\n• Immediate
updates\n\n**Example Flow:**\n1. You create \"Assignment
1\"\n2. You add \"Assignment 1\" to the attendance log\n3. You
select \"Automatic Attendance Registration\"\n4. Student submits
Assignment 1\n5. → System automatically records
attendance\n\n**Best Practices:**\n• Connect activities that
require physical or active participation\n• Use automatic registration
for online activities\n• Combine different types of activities\n\n📚
For more
information:\nhttps://docs.openeclass.org/en/teacher/attendance"
},
{
'chunk_id': 'attendance_tracking_005',
'chunk_topic': 'Exporting Attendance Log to CSV',
'questions': [
"How do I export the attendance log to CSV?",
"Exporting attendance log",
"CSV export attendance",
"How do I download the attendance log?",
"Exporting attendance data",
"Attendance log settings and export"
],
'answer': "Exporting Attendance Log to CSV Format\n\n**Export in
Different Encodings:**\n\nTo export the attendance log to a CSV
file, two options are available depending on the encoding you
need:\n\n**1. Export as Windows-1253 (Greek Encoding):**\n 1. Go
to the attendance log\n 2. Select the link \"Export in windows-1253
encoding\"\n 3. You get a CSV file with Greek characters\n 4. File
is compatible with older applications (e.g., older Excel for
Windows)\n\n**2. Export as UTF-8 (International Encoding):**\n 1.
Go to the attendance log\n 2. Select the link \"Export in UTF-8
encoding\"\n 3. You get a CSV file with UTF-8 encoding\n 4. File is
compatible with modern applications (e.g., LibreOffice, Google
Sheets)\n\n**Export Contents:**\nThe CSV file will contain:\n•
Student names\n• Number of attendances\n• Number of absences\n•
Attendance percentage (%)\n• Status (completed/not completed)\n•
Detailed activity dates\n\n**Using the CSV File:**\n• Open in
Excel\n• Open in LibreOffice Calc\n• Open in Google Sheets\n• Import
to other systems\n• Edit and print\n• Send to others\n\n**Encoding
Differences:**\n\n**Windows-1253 (Greek):**\n• Supports Greek
characters\n• Compatible with older software\n• May have issues on
non-Windows systems\n\n**UTF-8 (International):**\n• Supports all
characters (Greek, English, etc.)\n• Modern and widely compatible\n•
Recommended for modern applications\n• Works on all operating
systems\n\n**Selection Recommendation:**\n• Use **UTF-8** for
modern applications\n• Use **Windows-1253** if you have issues with
Greek characters in older software\n\n**Export Process:**\n1. Go
to the attendance log you want to export\n2. Select the appropriate
encoding\n3. Click the export link\n4. File downloads
automatically\n5. Open the file with your preferred
application\n\n**Possible Issues:**\n• **Greek characters not
displaying correctly:** Try UTF-8\n• **File won't open:** Make
sure you have a CSV application (Excel, LibreOffice)\n• **Wrong
encoding:** Try the other option\n\n**File Storage:**\n• Save
with name containing date (e.g., \"Attendance_2024_01.csv\")\n•
Create folder for attendance files\n• Keep copies for security\n\n📚
For more
information:\nhttps://docs.openeclass.org/en/teacher/attendance"
}
]
#
==============================================================================
# CHUNK 30: TELECONFERENCING
# Context: Creating video conferences, managing sessions, platform
selection
#
==============================================================================
CHUNK_TELECONFERENCING = [
{
'chunk_id': 'teleconference_001',
'chunk_topic': 'Teleconferencing - Overview',
'questions': [
"What is teleconferencing?",
"How do I create a teleconference?",
"Videoconference",
"Video conference",
"Online meeting",
"Synchronous online learning",
"Course teleconference",
"How do I do live teaching?",
"Virtual classroom"
],
'answer': "Teleconferencing - Overview\n\n**What Is
Teleconferencing:**\nThe \"Teleconferencing\" subsystem aims to
allow two or more remote users to communicate and collaborate with each
other in real time (synchronous online learning).\n\nIn this way,
instructors and learners can be virtually in the same place at the same
time while their physical location can be
anywhere.\n\n**Benefits:**\n• Live communication in real time\n•
High quality audio and video\n• Screen sharing\n• Interactive
content\n• Educational supplement\n• Flexible access from
anywhere\n\n**Enabling the Teleconferencing Tool:**\n\n1.
**View Active Tools:**\n • If the \"Teleconferencing\" tool is
enabled in your course\n • It will appear in the course's \"Active
tools\"\n\n2. **Enable Tool:**\n • Otherwise go to \"Inactive
tools\"\n • Select the \"Teleconferencing\" tool\n • Click the
tool's enable switch\n\n**Creating a New Teleconference:**\n1.
Select the \"New Teleconference\" link\n2. Select the
teleconferencing platform\n3. Fill in the meeting details\n4. Set the
settings\n5. Add participants\n6. Save\n\n**Available
Platforms:**\n• BigBlueButton (BBB)\n• Jitsi\n• Google Meet\n•
Webex\n• Zoom\n\n**Important:**\nA necessary prerequisite for
the teleconferencing platform you want (e.g., Webex) to appear in the
list is that the eClass platform administrator has enabled
it.\n\n**Teleconferencing Features:**\n• Multiple platform
support\n• Scheduled meetings\n• Audio and video quality\n• Content
sharing\n• Chat and file exchange\n• Meeting recording (optional)\n•
Participation from any device\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/tc"
},
{
'chunk_id': 'teleconference_002',
'chunk_topic': 'Creating Teleconference - Settings',
'questions': [
"How do I create a new teleconference?",
"Teleconference settings",
"How do I schedule a meeting?",
"Teleconference date and time",
"Setting participants",
"Adding participants to teleconference",
"Participant notification"
],
'answer': "Creating Teleconference - Details and
Settings\n\n**Creation Steps:**\n\n1. **Platform
Selection:**\n • Click \"New Teleconference\"\n • Select the
teleconferencing platform you want:\n - BigBlueButton (BBB)\n -
Jitsi\n - Google Meet\n - Webex\n - Zoom\n\n2. **Fill in Basic
Information:**\n • **Teleconference Title:** (e.g., \"Lecture
5 - Introduction to Topic A\")\n • **Description:**
(optional)\n\n3. **Set Date and Time:**\n • **Date:** When it
will happen\n • **Start Time:** Start time\n • **End Time:**
End time\n\n**Teleconference Settings:**\n\n**1.
Visibility:**\n • Visible (appears in the course)\n • Hidden (not
publicly visible)\n\n**2. Display in Announcements:**\n • Yes
(announcement about the meeting)\n • No (no announcement)\n\n**3.
Start Participation:**\n • Set how many minutes early participants
should enable participation\n • Example: 15 minutes before
start\n\n**4. Maximum Number of Participants:**\n • Set maximum
number of participants\n • **Recommended:** 6-20 depending on
platform\n • More participants = lower quality\n\n**5. Participant
Selection:**\n • **Everyone:** All enrolled students\n •
**Specific:** Choose certain students or groups\n\n**6. Notify
Participants:**\n • Enabled (they receive notification)\n • Disabled
(no notification)\n\n**7. Recording (if available):**\n • Yes
(meeting is recorded)\n • No (no recording)\n\n**8. Other
Settings:**\n • Screen sharing (enabled/disabled)\n • Chat
(enabled/disabled)\n • Polls
(enabled/disabled)\n\n**Completion:**\n1. Review all
settings\n2. Click \"Add\" button\n3. Teleconference is
created\n4. Appears in teleconference list\n\n**Example
Settings:**\n- Title: \"Live Lecture - Week 5\"\n- Date:
15/01/2024\n- Time: 10:00 - 11:30\n- Visible: Yes\n- Announcement:
Yes\n- Start participation: 15 minutes early\n- Max participants:
10\n- Participants: Everyone\n- Notification: Yes\n\n**Best
Practices:**\n• Plan in advance\n• Give clear title\n• Set
realistic time\n• Choose appropriate platform\n• Send
notifications\n• Check settings before\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/tc"
},
{
'chunk_id': 'teleconference_003',
'chunk_topic': 'Selecting Teleconferencing Platform',
'questions': [
"Which platform should I use?",
"Differences between platforms",
"BBB vs Zoom vs Webex",
"Comparison of teleconferencing platforms",
"How do I choose a platform?",
"Which platform is better?",
"Platform features"
],
'answer': "Selecting Teleconferencing Platform\n\n**Available
Platforms:**\n\nThe eClass platform supports many teleconferencing
platforms. However, a necessary prerequisite for the platform to appear
in the selection list is that the eClass administrator has enabled
it.\n\n**1. BigBlueButton (BBB):**\n• Open source software\n•
Built-in to eClass\n• Very good compatibility\n• Free to use\n• Ideal
for education\n\n**2. Jitsi:**\n• Open source software\n• Simple
and easy to use\n• Low requirements\n• Good quality\n•
Free\n\n**3. Google Meet:**\n• Integrates with Google
Workspace\n• Simple access\n• Clear quality\n• Meeting recording\n•
Requires Google account\n\n**4. Webex Meetings:**\n• Professional
software\n• High quality\n• Many features\n• Cost for large
groups\n• Suitable for large meetings\n\n**5. Zoom:**\n• Popular
software\n• Easy to use\n• Good video quality\n• Limited free
version\n• Cost for unlimited meetings\n\n**Feature
Comparison:**\n\n\| Feature \| BBB \| Jitsi \| Google Meet \| Webex
\| Zoom
\|\n\|---------\|-----\|-------\|------------\|-------\|------\|\n\|
Cost \| Free \| Free \| Free* \| Free* \| Free* \|\n\| Participants
\| Depends \| 200+ \| 150+ \| 100+ \| 100+ \|\n\| Quality \| Good \|
Good \| Excellent \| Excellent \| Excellent \|\n\| Screen Share \| Yes
\| Yes \| Yes \| Yes \| Yes \|\n\| Chat \| Yes \| Yes \| Yes \| Yes \|
Yes \|\n\| Recording \| Yes \| Yes \| Yes \| Yes \| Yes \|\n\| Polls
\| Yes \| No \| Yes \| Yes \| Yes \|\n\| Privacy \| Very good \| Very
good \| Good \| Good \| Good \|\n\n**Selection
Tips:**\n\n**Teacher with 5-20 Students:**\n→ **BigBlueButton
or Jitsi**\n- Suitable for courses\n- Free\n- Built-in to
eClass\n\n**Medium Class (20-50 Students):**\n→ **Google Meet
or Webex**\n- Good quality\n- Handle many participants\n-
Professional appearance\n\n**Large Institution (100+
Students):**\n→ **Zoom or Webex**\n- Capable of large
audiences\n- High quality\n- Many features\n\n**Data
Privacy/Privacy Concerns:**\n→ **BigBlueButton or Jitsi**\n-
Open source software\n- Better privacy\n- Don't collect third-party
data\n\n**Technical Support:**\n→ **Google Meet or Zoom**\n-
Good technical support\n- Fewer technical issues\n\n**Curriculum
Integration:**\n→ **BBB**\n- Built-in to eClass\n- No need for
external account\n- Better
integration\n\n**Important:**\nPlatform availability depends on
your eClass administrator's settings. Contact the administrator if you
don't see the platform you want.\n\n**Best Practices:**\n• Test
platforms in advance\n• Choose based on class size\n• Inform students
in advance\n• Provide alternative options\n• Usually use the same
platform\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/tc"
}
]
#
==============================================================================
# CHUNK 30B: TELECONFERENCING - BIGBLUEBUTTON DETAILED
# Context: BigBlueButton specific features, joining, audio setup,
interface
#
==============================================================================
CHUNK_TELECONFERENCING_BBB = [
{
'chunk_id': 'teleconference_bbb_001',
'chunk_topic': 'Teleconferencing with BigBlueButton - Starting',
'questions': [
"How do I start BigBlueButton?",
"Connecting to BigBlueButton",
"Teleconferencing with BigBlueButton tool",
"How do I join a live session?",
"Enabling BigBlueButton",
"Starting a video conference",
"I click on teleconference",
"How do I connect to BBB?"
],
'answer': "Teleconferencing with BigBlueButton -
Starting\n\n**Accessing the Teleconference:**\n\nHaving now
created a new teleconference, you should \"click\" on it to start it
running.\n\n1. **Find the Teleconference:**\n • Go to the
\"Teleconferencing\" subsystem\n • See the list of scheduled
meetings\n • Find the meeting you want to start\n\n2. **Start
Meeting:**\n • Click on the teleconference title\n • New screen
appears with participation options\n\n**Selecting Participation
Method:**\n\nIn the new window that appears, you must select your
participation method:\n\n**1. Microphone (With Audio):**\n • By
selecting \"Microphone\" you have the ability to hear and speak\n •
Two-way communication (bidirectional audio)\n • Ideal for activity and
participation\n • Requires standard microphone\n\n**2. Listen Only
(Without Audio):**\n • By selecting \"Listen only\" you have the
ability to hear and communicate via written messages (public chat)\n •
Useful for:\n - Microphone problems\n - Noisy environment\n -
Internet restrictions\n - Passive participation\n\n**Microphone
Usage Approval:**\n\nHaving selected \"Microphone\" you will be
asked to accept microphone usage.\n\n1. **Permission Request:**\n
• Browser will ask for microphone access\n • Appropriate button or
window appears\n\n2. **Accept:**\n • Click \"Accept\" or
\"Allow\" to continue\n • Necessary for audio use\n\n3.
**Reject:**\n • If you click \"Reject\", you won't have audio
access\n • You can change this later\n\n**Audio Test:**\n\nOn
the following screen, the platform will ask you to do a test to see if
you hear your own voice and select the corresponding marking.\n\n1.
**Recording Your Voice:**\n • System asks you to speak\n • You
will hear the test phrase\n\n2. **Verification:**\n • Do you hear
your own voice?\n • Is the audio level appropriate?\n\n3.
**Selection:**\n • \"Yes, I hear my voice\" - Continue to
meeting\n • \"No, I don't hear it\" - Check audio
settings\n\n**Entering Main Screen:**\n\nAfter completing the
audio test, you enter BigBlueButton's main screen.\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/tc/fulfillment"
},
{
'chunk_id': 'teleconference_bbb_002',
'chunk_topic': 'BigBlueButton Interface - Main Screen',
'questions': [
"How does BigBlueButton work?",
"BigBlueButton tools",
"BigBlueButton main screen",
"Where is the microphone in BBB?",
"Microphone control",
"BigBlueButton camera",
"BBB icons",
"Basic teleconferencing tools"
],
'answer': "BigBlueButton Interface - Main
Screen\n\n**BigBlueButton Main Screen:**\n\nYou are now on the
main screen of the BigBlueButton application.\n\n**Interface
Structure:**\n\n**1. Main Area (Center):**\n • Large display of
presentation or instructor\n • Shared screen (if active)\n • Camera
feeds (if active)\n\n**2. Left Sidebar:**\n • List of
participants\n • Raised hands (Raise Hand)\n • Status of each
participant (active, muted, etc.)\n\n**3. Right Sidebar:**\n •
Chat (public/private)\n • Notes\n • External video\n • Other
tools\n\n**4. Bottom Control Bar:**\n • Microphone control\n •
Camera control\n • Screen sharing\n • Show/Hide interface\n • Leave
meeting\n\n**Microphone Control:**\n\nThose who chose to connect
with a microphone will see the corresponding icon at the
bottom.\n\n**Microphone Icon:**\n • 🎙 Green: Microphone enabled
(Active)\n • 🎙 Red with line: Microphone disabled (Muted)\n • 🔊
Volume icon: Adjust volume\n\n**Enabling/Disabling
Microphone:**\n\nClicking on the microphone icon will let you enable
or disable it.\n\n1. **Enable:**\n • Click the microphone icon\n
• Turns green\n • You can now speak\n\n2. **Disable:**\n • Click
the microphone icon again\n • Turns red with line\n • Your audio is
not transmitted\n\n**Other Bottom Bar Icons:**\n\n**Camera
(Video):**\n • 📹 Camera icon\n • Click to enable/disable\n • Share
your video or see others\n\n**Screen Sharing:**\n • 🖥 Screen
icon\n • Share your content with everyone\n • Useful for
presentations\n\n**Leave:**\n • 🚪 Exit icon (Hang Up)\n • Leave
the meeting\n • Cannot rejoin after (unless you click the link
again)\n\n**Raise Hand:**\n • ✋ Hand icon\n • Notifies
presenter you want to speak\n • Useful in large
meetings\n\n**Settings:**\n • ⚙ Settings icon\n • Adjust
preferences\n • Audio volume adjustment\n • Display
settings\n\n**Polls:**\n • 📊 Poll icon\n • Presenter creates
questions\n • Vote in real time\n\n**Tips for Good
Communication:**\n• Keep your microphone stable\n• Mute when not
speaking (minimize noise)\n• Interested: Keep camera on if possible\n•
Use chat for questions/comments\n\n📚 For more
information:\nhttps://docs.openeclass.org/en/teacher/tc/fulfillment"
},
{
'chunk_id': 'teleconference_bbb_003',
'chunk_topic': 'BigBlueButton Features',
'questions': [
"BigBlueButton chat",
"Screen sharing",
"Notes board",
"BigBlueButton polls",
"How do I share my screen?",
"How do I write in chat?",
"BigBlueButton whiteboard",
"Collaboration tools"
],
'answer': "BigBlueButton Features - Collaboration Tools\n\n**1.
Chat (Conversation):**\n\n**Public Chat:**\n • Everyone sees
the messages\n • Good for general questions\n • Message history
available\n\n**Private Chat:**\n • Personal messages with
participant\n • Discrete communication\n • Only for involved
parties\n\n**Using Chat:**\n 1. See chat window on right side\n
2. Type your message\n 3. Press Enter to send\n 4. Messages appear
immediately\n\n**2. Screen Sharing (Screen
Sharing):**\n\n**Starting Screen Share:**\n 1. Click \"Share
Screen\" icon\n 2. Select which screen/window to share\n 3. Click
\"Share\"\n 4. Everyone sees your screen\n\n**During
Share:**\n • Other windows are grayed out\n • You control what's
shown\n • Audio continues normally\n • Presenter has
influence\n\n**Stop Sharing:**\n 1. Click \"Stop Sharing\"\n
2. Screen sharing ends\n\n**3. Notes Board
(Whiteboard):**\n\n**Starting:**\n 1. Click \"Whiteboard\"
icon\n 2. White page appears\n\n**Drawing Tools:**\n • Pencil
(Pencil) - Free drawing\n • Shapes (Shapes) - Squares, circles, etc.\n
• Text (Text) - Add text\n • Eraser (Eraser) - Delete\n • Colors
(Colors) - Choose color\n\n**Using:**\n • Draw and annotate in
real time\n • Everyone sees changes\n • Useful for
explanations\n\n**4. Polls (Polls):**\n\n**Creating Poll
(Instructor):**\n 1. Click \"Polls\" icon\n 2. Create multiple
choice question\n 3. Add the options\n 4. Click
\"Publish\"\n\n**Participating in Poll (Student):**\n 1. See
poll on screen\n 2. Select an answer\n 3. Results appear in real
time\n\n**5. White Board (Presentation):**\n\n**Uploading
File:**\n 1. Click \"Upload Presentation\" icon\n 2. Select file
(PDF, PowerPoint, etc.)\n 3. File converts to
slides\n\n**Navigating Slides:**\n • Arrows (Arrows) -
Next/Previous\n • Thumbnails (Thumbnails) - Find slide\n • Slide
number - Go directly\n\n**Annotating Presentation:**\n • Enable
\"Drawing Tools\"\n • Draw/write on slide\n • Useful for
emphasizing points\n\n**6. Participant Videos:**\n\n**Enabling
Camera:**\n 1. Click camera icon\n 2. Select camera (if multiple)\n
3. Give permission\n 4. Others see your video\n\n**Video
Display:**\n • Position: Bottom left (usually)\n • Size: Change by
dragging\n • Sorting: Presenter controls\n\n**7. Recording (if
enabled):**\n\n**Getting Recording:**\n • Instructor enables
recording\n • Everyone notified with \"Recording\" indicator\n •
Available after meeting\n\n**Tips for Good Use:**\n• Use Chat for
uninterrupted questions\n• Screen sharing for more engaging content\n•
Polls for interaction\n• Whiteboard for live explanations\n\n📚 For
more
information:\nhttps://docs.openeclass.org/en/teacher/tc/fulfillment"
}
]
#
==============================================================================
# CHUNK 30C: TELECONFERENCING - GOOGLE MEET
# Context: Google Meet setup, linking meetings, features
#
==============================================================================
CHUNK_TELECONFERENCING_GOOGLEMEET = [
{
'chunk_id': 'teleconference_googlemeet_001',
'chunk_topic': 'Teleconferencing with Google Meet',
'questions': [
"What is Google Meet?",
"How do I create a Google Meet meeting?",
"Google Meet",
"Creating Google Meet teleconference",
"Teleconferencing with Google Meet",
"How do I use Google Meet?",
"Google Meet features",
"Setup Google Meet"
],
'answer': """Teleconferencing with Google Meet
**What Is Google Meet:**
Google Meet is software that allows users to make voice calls and video
calls with high clarity.
This way, the organization of digital lessons and participation of
learners in them is achieved.
**Google Meet Features:**
• Ability to participate in meetings via web browser or Android/iOS
applications
• Screen sharing for presenting documents, spreadsheets, presentations,
or other browser tabs
• Hosts can deny entry and remove users during a call
• Ability to raise and lower hand
• Support for hundreds of participants
• Automatic recording (if enabled)
• Low connection requirements
**Creating a Google Meet Teleconference:**
1. **Access the System:**
• Go to the "Teleconferencing" subsystem
• From the available list select "Google Meet"
• Important: Administrator must have enabled Google Meet
2. **Select Google Meet:**
• Select "Google Meet" from the displayed list
3. **Go to Google Meet:**
• In the displayed form select "Go to Google Meet"
• You are redirected to the Google Meet platform
4. **Create Meeting:**
• Enter your credentials (Google account)
• Create a new meeting
• Use the settings you prefer
5. **Copy Link:**
• Copy the meeting link you created
• Click the link "Get a link you can share"
• Copy the link
6. **Paste Link in eClass:**
• Go back to the eClass form you had open
• Paste the Google Meet link
7. **Fill in Details:**
• **Title:** Name of the teleconference
• **Description:** Brief description of content
• **Start:** Start date and time
• **End:** End date and time
• **Other parameters:** Visibility, announcement, participants, etc.
8. **Save:**
• Complete the process
• The teleconference is created and ready
**Important Notes:**
**Requirements:**
• Google account (Gmail)
• Internet connection
• Camera and microphone (optional)
**Tips:**
• Test the connection in advance
• Use digital wallpaper or virtual background
• Enable hard call or wait room for security
• Share the link only with authorized participants
• Check audio and video settings before starting
• Provide clear instructions to participants
📚 For more information:
https://docs.openeclass.org/en/teacher/tc"""
}
]
#
==============================================================================
# CHUNK 30D: TELECONFERENCING - ZOOM
# Context: Zoom setup, linking meetings, features
#
==============================================================================
CHUNK_TELECONFERENCING_ZOOM = [
{
'chunk_id': 'teleconference_zoom_001',
'chunk_topic': 'Teleconferencing with Zoom',
'questions': [
"What is Zoom?",
"How do I create a Zoom meeting?",
"Zoom",
"Creating a Zoom teleconference",
"Teleconferencing with Zoom",
"How do I use Zoom?",
"Zoom features",
"Zoom setup",
"How do I connect to Zoom?",
"Connecting to a Zoom teleconference"
],
'answer': """Teleconferencing with Zoom Tool
Zoom is a software tool that allows users to conduct video conferences
with high definition clarity. This enables the organization of digital
classes and allows learners to participate in them.
**Creating a Zoom Teleconference:**
To create a new teleconference using Zoom, follow the steps below:
1. **Access the System:**
• Navigate to the "Teleconferencing" subsystem
• From the available list, select Zoom
• Important: Zoom must be enabled by your platform administrator to
appear in the available teleconferencing tools
2. **Select Zoom:**
• Choose Zoom from the displayed list
3. **Navigate to Zoom:**
• In the form that appears, select "Go to Zoom"
• You will be redirected to the Zoom platform
4. **Create Meeting:**
• Enter your credentials (Zoom account)
• Create a new meeting
• Configure the settings as desired
5. **Copy Meeting Link:**
• Copy the link of the meeting you created
• Click the link "Get a link you can share"
• Copy the link
6. **Paste Link in eClass:**
• Return to the eClass form you had open
• Paste the Zoom link
7. **Fill in Details:**
• **Title:** Name of the teleconference
• **Description:** Brief description of the content
• **Start:** Date and time of the meeting start
• **End:** Date and time of the meeting end
• **Other parameters:** Visibility, announcement, participants, etc.
8. **Save:**
• Complete the process
• The teleconference is created and ready
**Important Notes:**
**Requirements:**
• Zoom account
• Internet connection
• Camera and microphone (optional)
**Tips:**
• Test your connection beforehand
• Use a virtual background
• Enable waiting room for security
• Share the link only with authorized participants
• Check audio and video settings before starting
• Provide clear instructions to participants
📚 For more information:
https://docs.openeclass.org/en/teacher/tc/zoom"""
}
]
#
==============================================================================
# CHUNK 30E: TELECONFERENCING - JITSI
# Context: Jitsi setup, creating conferences, features
#
==============================================================================
CHUNK_TELECONFERENCING_JITSI = [
{
'chunk_id': 'teleconference_jitsi_001',
'chunk_topic': 'Teleconferencing with Jitsi',
'questions': [
"What is Jitsi?",
"How do I create a Jitsi meeting?",
"Jitsi",
"Creating a Jitsi teleconference",
"Teleconferencing with Jitsi",
"How do I use Jitsi?",
"Jitsi features",
"Jitsi setup",
"How do I connect to Jitsi?",
"Connecting to a Jitsi teleconference"
],
'answer': """Teleconferencing with Jitsi Tool
Jitsi is a collection of open-source applications for voice, video
conferencing, and instant messaging, and is compatible with most
operating systems (Windows, Linux, macOS, iOS, Android).
**Creating a Jitsi Teleconference:**
To create a new video conference using Jitsi, navigate to the
"Teleconferencing" subsystem of the e-class platform. Then select the
"New Teleconference" link using the specific software (Jitsi).
**Creation Steps:**
1. **Access the System:**
• Go to the "Teleconferencing" subsystem
• Select "New Teleconference"
• Choose Jitsi from the available options
2. **Configure Settings:**
• **Title:** Name of the teleconference
• **Start:** Start date and time
• **End:** End date and time
• **Visibility:** Specify if it will be visible or not
• **Announcement:** Choose whether it appears in announcements
• **Activation Minutes:** Set the minutes for enabling participation
before the scheduled start
• **Number of Participants:** Specify the maximum number of
participants
3. **Save:**
• Complete the creation
• The teleconference is ready
**Jitsi Features:**
Upon successfully entering the Jitsi platform, you have access to the
following features:
• **Invite Participants:** Invite participants through various
methods
• **Screen Sharing:** Share your screen with all participants
• **Chat:** Text communication with all groups
• **Camera Settings:** Enable/disable video
• **Audio Settings:** Control microphone and speakers
• **Video Quality:** Adjust video quality
• **Speaker Statistics:** View participation statistics
• **Other Functions:** Various additional collaboration tools
**Important Jitsi Features:**
• Open Source - Free to use
• Compatibility with multiple operating systems
• No registration or software installation required
• High-quality audio and video
• Recording capability (depending on settings)
• User-friendly interface
📚 For more information:
https://docs.openeclass.org/en/teacher/tc/jitsi"""
}
]
#
==============================================================================
# CHUNK 31: LEARNING ANALYTICS
# Context: Learning analytics creation, criteria configuration,
performance tracking
#
==============================================================================
CHUNK_LEARNING_ANALYTICS = [
{
'chunk_id': 'learning_analytics_001',
'chunk_topic': 'Learning Analytics - Overview',
'questions': [
"What is learning analytics?",
"Learning analytics",
"How do I use learning analytics?",
"Learning analytics subsystem",
"Data analysis for learning",
"Learning statistics",
"How do I track student progress?",
"Learning data",
"Learning metrics"
],
'answer': """Learning Analytics - Overview
**What Is Learning Analytics:**
Learning analytics is a metric which concerns the collection and
analysis of data which aim at optimizing learning from the perspective
of learners.
**Use for Instructors:**
From the perspective of instructors, it is a very important tool for:
• Collecting course data
• Reporting statistics
• Analyzing student progress
• Improving the course
• Monitoring student engagement
• Assessing performance
**Main Features:**
• Customizable measurement criteria
• Flexible time period (daily, weekly, monthly, total)
• Automatic data collection
• Historical reports
• Performance per user
• Data export
**How to Get Started:**
1. Select "Course Management" link
2. Select "Learning Analytics" link
3. Click "Add" button
4. Create new learning analytics
5. Define the criteria
**Available Criteria:**
• Blog posts
• Comments (Blog, Course, Wall)
• Grades (Exercises, Assignments)
• Assignment submissions
• Forum posts
• Wiki pages
• Time spent on course
📚 For more information:
https://docs.openeclass.org/en/teacher/learning_analytics"""
},
{
'chunk_id': 'learning_analytics_002',
'chunk_topic': 'Creating New Learning Analytics',
'questions': [
"How do I create learning analytics?",
"How do I add learning statistics?",
"Creating new analytics",
"New learning analytics",
"Setting analytics parameters",
"Enabling learning analytics",
"Start and end dates"
],
'answer': """Creating New Learning Analytics
**Creation Process:**
1. **Access:**
• Select "Course Management"
• Select "Learning Analytics"
• Click "Add"
2. **Fill in Form:**
You need to enter a series of parameters:
**Basic Parameters:**
**1. Title (Required):**
• Give a descriptive name
• Example: "Week 1-5 Analysis"
**2. Description (Optional):**
• Give brief description
• Explain the purpose
**3. Enable:**
• Select enabled or disabled
• Enabled = actively collects data
• Disabled = does not collect data
**4. Calculation (Analysis Period):**
Select the calculation frequency:
• **Daily:** New analysis each day
• **Weekly:** New analysis each week
• **Monthly:** New analysis each month
• **Total:** One summary for entire period
**5. Start Date:**
• Date when data collection will begin
• Is the date from which user actions will start to be included in the
calculation
• Example: 01/01/2024
**6. End Date:**
• Date when data collection will end
• Is the date to which user actions will be counted
• Example: 31/12/2024
**Save:**
1. Review all parameters
2. Click "Save" or "Add"
3. Analytics is created
**Next Step:**
After creation, you need to define the criteria (elements) of the
analytics.
📚 For more information:
https://docs.openeclass.org/en/teacher/learning_analytics"""
},
{
'chunk_id': 'learning_analytics_003',
'chunk_topic': 'Defining Parameters and Criteria',
'questions': [
"How do I define learning analytics criteria?",
"Edit analytics elements",
"Adding criteria",
"Selecting statistics elements",
"Available measurement criteria",
"Setting criterion weight",
"Critical and advanced level"
],
'answer': """Defining Parameters and Criteria
**Changing Analytics Elements:**
On the analytics screen next to each learning statistic are parameters.
Specifically, the options provided are:
• Changing elements
• Editing
• Enabling/Disabling
• Deleting
**Editing Elements:**
The next step involves defining the elements-criteria of the learning
analytics you created.
1. **Select "Edit Elements":**
• Click on "Edit Elements" link
• The list of available criteria appears
2. **Add Criteria:**
• Click "Add"
• A dropdown list appears
**Available Measurement Criteria:**
From the dropdown list, select the elements you want:
• **Blog Posts**
• **Blog Comments**
• **Course Comments**
• **Wall Comments**
• **Exercise Grade**
• **Assignment Grade**
• **Early Assignment Submission**
• **Forum Posts**
• **Wiki Pages**
• **Course Links**
• **Hits** (Page Views)
• **Course Duration**
• **Learning Path**
**Defining Parameters for Each Criterion:**
For each criterion you select, you must define:
**1. Critical Level:**
• **Lower Value (Required):**
- The minimum value of the criterion
- Example: 0
• **Upper Value (Required):**
- The threshold of the critical level
- Example: 5
**2. Advanced Level:**
• **Lower Value (Required):**
- The minimum value for advanced level
- Example: 6
• **Upper Value (Required):**
- The maximum value
- Example: 10
**3. Weight (Required):**
• The importance of the criterion
• Used to calculate the final percentage
• Example: 1.5 (1.0 = normal, >1.0 = greater importance)
**Example Definition:**
Criterion: "Blog Comments"
- Critical: 0-5
- Advanced: 6-10
- Weight: 1.0
**Final Percentage Calculation:**
The final percentage is calculated as:
- **Average** of all individual values
- **Considering** the weight of each criterion
- **Formula:** (Σ(value × weight)) / Σ(weights)
**Editing Criteria:**
After creating criteria, you can:
• Edit them
• Change the parameters
• This is done through the "Edit Elements" link
📚 For more information:
https://docs.openeclass.org/en/teacher/learning_analytics"""
},
{
'chunk_id': 'learning_analytics_004',
'chunk_topic': 'Viewing and Analyzing Data',
'questions': [
"How do I view learning analytics data?",
"View overall statistics",
"User details",
"Student performance",
"Detailed statistics",
"Participation percentage",
"Detailed reports",
"How do I show the results?"
],
'answer': """Viewing and Analyzing Data
**View Overall Statistics:**
1. **Select Time Period:**
• Select "Overall Statistics"
• Set time period "From-To"
• Example: 01/01/2024 - 31/01/2024
2. **Display Results:**
• First: Users who participated
• Second: Performance they achieved
**View By Criterion:**
By clicking on each criterion:
• Users who participated appear
• View per criterion
• Categorization per element
**View Details:**
1. **Click "Details":**
• Shows participating users
• Per criterion established
2. **Select Specific Criterion:**
• Example: "Blog Posts"
• List of related users appears
3. **Select Specific User:**
• Click on a user from the list
• The **participation percentage** appears
• Performance in defined criteria appears
**Displayed Data:**
For each user you can see:
• Number of posts/activities
• Participation dates
• Participation percentage (%)
• User progress
• Performance on each criterion
• Comparative analysis
**Example Data Reading:**
Criterion: "Blog Comments"
- User A: 7 comments (70%)
- User B: 5 comments (50%)
- User C: 3 comments (30%)
**Overall Analysis:**
The system calculates:
• Average value per criterion
• Total percentage per user
• User ranking
• Development trends
**Useful For:**
• Monitoring engagement
• Identifying active users
• Identifying underperforming users
• Progress reporting
• Adjusting instruction
📚 For more information:
https://docs.openeclass.org/en/teacher/learning_analytics"""
}
]
#
==============================================================================
# CHUNK 33: FLIPPED CLASSROOM
# Context: Flipped Classroom model, creating flipped courses,
activities before/during/after class
#
==============================================================================
CHUNK_FLIPPED_CLASSROOM = [
{
'chunk_id': 'flipped_001',
'chunk_topic': 'Flipped Classroom Model - Overview',
'questions': [
"What is the Flipped Classroom?",
"Flipped Classroom model",
"Flipped Classroom",
"What is the inverted classroom?",
"How does Flipped Classroom work?",
"Flipped learning",
"Inverted classroom model",
"What is flipped learning?",
"Flipped teaching method"
],
'answer': (
"Flipped Classroom Model - Overview\n\n"
"The Flipped Classroom model aims to increase learner productivity and
learning by having "
"students complete their study of course material at home and work on
live problem-solving during class. "
"This pedagogical style transfers activities, including those that
might traditionally be considered homework, into the classroom.\n\n"
"**How it works:**\n"
"With a flipped classroom, learners:\n"
"• Watch online lectures at home\n"
"• Collaborate in online discussions\n"
"• Conduct research at home\n"
"• Actively engage with concepts in class with mentor guidance\n\n"
"**Benefits:**\n"
"This approach allows learners to delve deeper into subject topics
(having acquired prior knowledge by studying at home) "
"always with the guidance of the course mentor/instructor.\n\n"
"📚 For more information:\n"
"https://docs.openeclass.org/en/teacher/course_flipped_classroom"
)
},
{
'chunk_id': 'flipped_002',
'chunk_topic': 'Creating a Flipped Classroom Course',
'questions': [
"How do I create a Flipped Classroom course?",
"Create flipped classroom",
"Enable flipped classroom model",
"How to enable flipped classroom?",
"Setting up flipped classroom",
"Activate flipped classroom",
"New flipped classroom course",
"Create inverted classroom course"
],
'answer': (
"Creating a Flipped Classroom Course\n\n"
"To create a course with the Flipped Classroom model enabled:\n\n"
"**Step 1:** Select the \"Create Course\" link.\n\n"
"**Step 2:** Fill in the required fields:\n"
"• Category\n"
"• Instructors\n"
"• Short description\n"
"• Course format (must be set to \"Course in units\")\n\n"
"**Step 3:** Enable the \"Flipped Classroom Model\" by clicking
the \"Active\" button.\n\n"
"**Important:** The course format MUST be set to \"Course in
units\" for the Flipped Classroom model to work properly.\n\n"
"**Step 4:** Set the course access type:\n"
"• Open\n"
"• Open with registration\n"
"• Closed\n\n"
"**Step 5:** Click \"Submit\" to complete the process.\n\n"
"📚 For more information:\n"
"https://docs.openeclass.org/en/teacher/course_flipped_classroom"
)
},
{
'chunk_id': 'flipped_003',
'chunk_topic': 'Flipped Classroom - Study Hours and Learning
Objectives',
'questions': [
"How do I set study hours for flipped classroom?",
"Learning objectives flipped classroom",
"Flipped classroom hours",
"Study time flipped classroom",
"Set flipped classroom objectives",
"Configure flipped classroom hours",
"Flipped classroom learning goals"
],
'answer': (
"Flipped Classroom - Study Hours and Learning Objectives\n\n"
"After enabling the Flipped Classroom model, you need to
configure:\n\n"
"**In the next form, fill in:**\n"
"• Hours of engagement with the specific course\n"
"• Learning objectives for the course\n\n"
"**Then specify:**\n"
"• Teaching method (Distance learning or Blended learning)\n"
"• Titles of thematic units\n\n"
"Click \"Next\" to continue with the setup.\n\n"
"📚 For more information:\n"
"https://docs.openeclass.org/en/teacher/course_flipped_classroom"
)
},
{
'chunk_id': 'flipped_004',
'chunk_topic': 'Flipped Classroom Activities Configuration',
'questions': [
"How do I configure flipped classroom activities?",
"Before class activities",
"In class activities",
"After class activities",
"Flipped classroom activity types",
"Set up flipped classroom activities",
"Configure activities before during after class"
],
'answer': (
"Flipped Classroom Activities Configuration\n\n"
"In the next form, check the activities that will take place:\n\n"
"**Before Class:**\n"
"• Add Document\n"
"• Add Link\n"
"• Add E-book\n"
"• Add Glossary\n"
"• Add from Course Wall\n\n"
"**In Class:**\n"
"• Add Exercise\n"
"• Add Link\n"
"• Add Wiki\n\n"
"**After Class:**\n"
"• Additional activities as needed\n\n"
"**Important:** Before adding any activity described above, you
must have created it first.\n\n"
"Click \"Final Submit\" to complete the Flipped Classroom course
creation.\n\n"
"📚 For more information:\n"
"https://docs.openeclass.org/en/teacher/course_flipped_classroom"
)
},
{
'chunk_id': 'flipped_005',
'chunk_topic': 'Flipped Classroom - Managing Units and Activities',
'questions': [
"How do I add activities to flipped classroom units?",
"Manage flipped classroom units",
"Add content to flipped units",
"Flipped classroom unit management",
"Insert activities into flipped units",
"Organize flipped classroom content"
],
'answer': (
"Flipped Classroom - Managing Units and Activities\n\n"
"After successfully completing the course creation process, you can
manage your Flipped Classroom units:\n\n"
"**Viewing Course Information:**\n"
"By clicking on course information, all data you have entered regarding
the Flipped Classroom will be displayed.\n\n"
"**Adding Activities to Units:**\n"
"The next step is to add activities per unit related to the Flipped
Classroom:\n\n"
"1. Click on each unit to see a series of activities you can
integrate\n\n"
"2. Activities are divided into:\n"
" • **Before Class** - Documents, Links, E-books, Glossary, Wall
posts\n"
" • **In Class** - Exercises, Links, Wiki\n\n"
"**Remember:** Any activity you want to add must be created before
you can include it in a unit.\n\n"
"📚 For more information:\n"
"https://docs.openeclass.org/en/teacher/course_flipped_classroom"
)
}
]
#
==============================================================================
# CHUNK 34: WALL
# Context: Posting on the wall, adding multimedia content, managing
posts
#
==============================================================================
CHUNK_WALL = [
{
'chunk_id': 'wall_001',
'chunk_topic': 'Wall - Overview',
'questions': [
"What is the Wall?",
"Wall",
"How do I use the Wall?",
"Posting to the Wall",
"Wall tool",
"Wall feature",
"Publishing announcements",
"Posting system",
"How do I post announcements?"
],
'answer': """Wall - Overview
**What Is The Wall:**
The "Wall" subsystem allows the instructor to apply a set of posts
with multiple content in chronological order.
**Use of Wall:**
The Wall is used for:
• Course announcements and updates
• Sharing multimedia (videos, images)
• Publishing documents and resources
• Interaction with students
• Creating discussions and information exchange
• Archiving important information
**Main Features:**
• Chronological order of posting
• Multiple content support (text, images, videos, documents)
• Ability to attach resources from the course
• Easy information presentation
• Available in both languages
**How to Get Started:**
1. Navigate to the "Wall" subsystem
2. Click "Add Post" or "New Post" button
3. Enter the post content
4. Add attached resources (optional)
5. Publish the post
📚 For more information:
https://docs.openeclass.org/en/teacher/wall"""
},
{
'chunk_id': 'wall_002',
'chunk_topic': 'Adding Post to Wall',
'questions': [
"How do I add a post?",
"How do I write on the Wall?",
"Creating a new post",
"New post on the Wall",
"How do I announce something?",
"Entering a message",
"Publishing text"
],
'answer': """Adding Post to Wall
**Process of Adding a Post:**
1. **Navigate to Wall:**
• Open the course
• Select the "Wall" subsystem from available tools
2. **Create Post:**
• Look for the "Add Post" or "New Post" button
• Click to open the input form
3. **Enter Content:**
• Type the content of the message you want displayed in your post
• Use the text editor for formatting
• Add title (optional) for better organization
4. **Attach Resources (Optional):**
• Select the resources you want to attach to your post
5. **Publish:**
• Click "Publish" or "Save" button
• The post appears at the top of the list (newest first)
**Important Notes:**
• Posts are displayed in chronological order (newest first)
• You can edit or delete your own posts
• Text can contain formatting (bold, italic, etc)
• Add attachments for richer content
📚 For more information:
https://docs.openeclass.org/en/teacher/wall"""
},
{
'chunk_id': 'wall_003',
'chunk_topic': 'Attached Resources in Wall',
'questions': [
"How do I add a video to the Wall?",
"How do I add an image to the Wall?",
"How do I add a document?",
"Adding YouTube video",
"YouTube link",
"Multimedia on the Wall",
"Documents on the Wall",
"Content insertion",
"Attached resources",
"Attaching a file"
],
'answer': """Attached Resources in Wall
**Attaching Content:**
The selection of attached resources for a post includes elements from 3
sections:
1. **Videos from YouTube**
2. **Multimedia from the course \"Multimedia\" subsystem**
3. **Documents from the course \"Documents\" subsystem**
**Adding Videos from YouTube:**
**Steps:**
1. First, enter the message content
2. Look for the field or button "Add YouTube Video"
3. Enter the URL (web address) of the video on YouTube
4. The video will be embedded in the post
5. Publish the post
**Example URL:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
**Adding Multimedia from "Multimedia" Subsystem:**
**Steps:**
1. In the post, click the "Multimedia" link
2. A list of available multimedia files appears
3. Select the files you want included in your post
4. Click "Select" or "Add" button
5. Selected files are added to the post
**Available Multimedia Types:**
• Images (JPG, PNG, GIF, etc)
• Audio (MP3, WAV, etc)
• Video (MP4, WebM, etc)
• Other multimedia files
**Adding Documents from "Documents" Subsystem:**
**Steps:**
1. In the post, click the "Documents" link
2. A list of available documents appears
3. Select the documents you want included
4. Click "Select" or "Add" button
5. Selected documents are added to the post
**Available Document Types:**
• PDF (Portable Document Format)
• Word Documents (DOCX, DOC)
• PowerPoint (PPTX, PPT)
• Excel (XLSX, XLS)
• Text (TXT)
• Other files
**Best Practices:**
• Use relevant multimedia for interest
• Add reference documents or study resources
• Check that URLs are correct before publishing
• Organize posts with clear topics
• Use descriptions for easier understanding
📚 For more information:
https://docs.openeclass.org/en/teacher/wall"""
}
]
#
==============================================================================
# FINAL: Combine all chunks into one knowledge base list (english
version)
#
==============================================================================
KNOWLEDGE_BASE_EN = (
CHUNK_GREETINGS +
CHUNK_AUTHENTICATION +
CHUNK_STUDENT_PORTFOLIO +
CHUNK_ASSIGNMENTS +
CHUNK_COURSE_CONTENT +
CHUNK_USER_GROUPS +
CHUNK_COURSE_MANAGEMENT +
CHUNK_COMMUNICATION +
CHUNK_ASSESSMENTS +
CHUNK_MULTIMEDIA +
CHUNK_CALENDAR +
CHUNK_PROFILE +
CHUNK_ENROLLMENT +
CHUNK_TECHNICAL +
CHUNK_ADVANCED +
CHUNK_GLOSSARY +
CHUNK_WIKI +
CHUNK_COURSE_GLOSSARY +
CHUNK_EPORTFOLIO +
CHUNK_LEARNING_PATH +
CHUNK_ATTENDANCE +
CHUNK_MOBILE +
CHUNK_INTERACTIVE_CONTENT +
CHUNK_PERSONAL_STATISTICS +
CHUNK_QUESTIONNAIRES +
CHUNK_LIVE_MESSAGING +
CHUNK_RECORDING +
CHUNK_RUBRICS +
CHUNK_PEER_REVIEW +
CHUNK_ATTENDANCE_TRACKING +
CHUNK_TELECONFERENCING +
CHUNK_TELECONFERENCING_BBB +
CHUNK_TELECONFERENCING_GOOGLEMEET +
CHUNK_TELECONFERENCING_ZOOM +
CHUNK_TELECONFERENCING_JITSI +
CHUNK_LEARNING_ANALYTICS +
CHUNK_FLIPPED_CLASSROOM +
CHUNK_WALL
)
