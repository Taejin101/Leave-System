![image](https://github.com/Taejin101/Leave-System/assets/91075527/5c9a7e1e-5abe-44bd-8359-c647f9345b3e)

# Project Overview:-
The main idea is managing the leave records for staff and students. The Admin is responsible for
the details of staff and student. In the staff module the staff can apply for leave and the HoD and Warden can
approve/reject the leave through the application and then Wardens will look after the request and they may
accept or reject, seeing the students parents approval and the students attendance details in case of working
days. The features of the application are registering staff and student, application of leave, approval/rejection
of leave, view leave balance, view leave history. For logging into the system and sending leave requests, each
student is given a unique user id and password . The status of the leave and the leave requests to the higher
authority will be sent through Mail. The main objective of Leave Management system is to decrease the
paper work to the maximum and easier record maintenance by having a separate system for leaves
maintenance.The web application aims to automate the entire leave management process, from requesting
and approving leave to tracking and reporting. By implementing this web-based leave Applications,
organizations can reduce administrative overhead, minimize leave conflicts, and improve overall efficiency.

# Installation Instructions:-
### Step 1:- Clone the repository.
### Step 2:- Create a virtual environment.
### Step 3:- Execute the command pip install -r requirements.txt in command prompt.
### Step 4:- Create a .env file with two variables EMAIL_HOST_USER and EMAIL_HOST_PASSWORD for system mail id to send application update email.
### Step 5:- Create an admin user using command python manage.py createsuperuser.
### Step 6:- Execute the command python manage.py runserver in command prompt.

# Usage:-
There are three roles of users - admin, staff and student

## Admin user:-
1. Can approve/reject application request of staff user.
2. Have full access to django admin to add more users.
   
   ![image](https://github.com/Taejin101/Leave-System/assets/91075527/84431e1b-045e-4d53-9b78-44e851a10369)

## Staff user:-
1. Can file a leave application.
2. Can approve/reject application of student role users.
3. Can view history of applications.

   ![image](https://github.com/Taejin101/Leave-System/assets/91075527/9325efae-d635-4196-a0e3-588282c6d947)

## Student user
1. Can file a leave application.
2. Can view history of applications

   ![image](https://github.com/Taejin101/Leave-System/assets/91075527/5f355e06-4b24-4eee-96b7-4ab391e84217)



  
