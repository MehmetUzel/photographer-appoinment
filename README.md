# Made it Public !!!

# photographer-appoinment
Newborn Photography shooting planner and appointment system for customers

Made with Django 4.0.3 and really bad vanilla JS please don't look JS codes without protective glasses or you would definetely be blind

Also sorry for misspelling some words like "appoinment" when i figured out that i spelled that wrong it was too late and i use that word a lot and it wont worth the correction :s

This project was for my friend who lives in Turkey so this project mixed with Turkish and English

Projects core features are completed but it has potential improvements as i listed below

# Current Features

Register, Login and Logout for User

Adding Address 

Creating Appointment for user in admin-edit page

Exporting appointments from django-admin panel

Filtering appointments from django-admin panel and sorting them by date.

Only letting one appointment for one user

Creating Off Days

Off days are display as booked to users because customer dont want users be able to see they are not working at that time

Calendar view for users to see which days are available

Displaying appointment details in admin-edit page

Creating Shoot Plan for user. (Shoot-plan includes shoot-type, album, num-of-concept and payment_choice)

Total Amount can be calculated from album_type and concept price dynamically but customer makes their operations in Turkey. Turkey is well known by inflation so prices can be changed regularly. This price change should not effect current customers it should only effect new appointments. So Total amount is stored on Shoot_Plan table.

Selecting Concepts

If num-of-concepts decreased after selecting concepts. Concept selection screen shows cute message to user "You decreased number of concepts so you should leave some of them, We are sorry 🥲"

Compressing Concepts photos when admin uploads them so page speed does not suffer from huge files.

All delevelopment made in English but due to customer frontend translated to Turkish.

Flow of the usage of website forced to user for example they cannot create shoot_plan before they add address information and so on. They have to select everything correctly before accessing appointment selection screen.

Asking Childs age when creating shoot_plan

# Known Issues and Planned Feature
"S" Login user automatically when they register.

"S" Adding All of the cities and districts for Turkey

"S" Smtp Configuration

"S" Email address confirmation

"S" Password Reset Strategy

"S" Handling Returning Customers Right now not supported because More than one shoot_plan and appointment is not available for same user

"S" Changing Shoot_type when creating Shoot_plan causes errors if user selected concepts before changing shoot_type old selected concepts is
not displayed because concepts screen only displays selected shoot_type concepts.

"S" When admin changes any users appointment from djangos admin panel they can accidentally make new date overlap with off_day and due to this 
overlap they cannot see appointment in admin-edit screen. Don't let admin make overlaps control it in backend and throw error.

"S" Shoot_Appointment table is currently not using but it added to model class when you decide to implement more than one appointments for same user.(This feature is not urgent because customer can have returning customer after one year "Because they only shoot newborns and 1 year old babies")We dont want user to create multiple shoots and appointments at the same time and matching them manually. This should be done automatically.First thing that i came up with is only selecting future appointment and shoot_plan. If an appointment and shoot plan is not in future they can create new one and so on. You can also use is_active field if you want. If you use that strategy maybe you dont need to create shoot_appointment table but its your choice. Think wisely.

"!" Mobile navigation bar display problem its because of fixing scrool you should also solve it somehow

"S" Exporting appointments "Currently its only exporting e-mails of users who created appointment. You should add details for appointment maybe you should also add shoot_details."

"S" You can also add changing num_of_concepts form concept selection screen maybe it would increase selected concepts because in that screen they will see how beautiful the concepts are.

"S" You can implement shoot_times and Create calendar dynamically by looking how many time fields exist.

"S" You can also add create your own concepts by showing different concept items to user but maybe customer don't want this feature.


