# photographer-appoinment
Photograph shooting planner and appoinment system for customers

# Known Issues and Planned Feature
Is down_payment paid or not ? because price field is currently not implemented.

Smtp Configuration

Email address confirmation

Password Reset Strategy

Handling Returning Customers Right now not supported because More than one shoot_plan and appointment is not available for same user

Asking Childs age when creating shoot_plan

Changing Shoot_type when creating Shoot_plan causes errors if user selected concepts before changing shoot_type old selected concepts is
not displayed because concepts screen only displays selected shoot_type concepts.

Current customer for this project does their operations in Turkey ( Turkey is well known by inflation. ) So prices can change regularly.
If prices updated old appointments total price would change also but customer don't want to updates current customers they just want to update
prices for new customers. So Total price should be saved when user creates appointment.

When admin changes any users appointment from djangos admin panel they can accidentally make new date overlap with off_day and due to this 
overlap they cannot see appointment in admin-edit screen. Don't let admin make overlaps control it in backend and throw error.

Shoot_Appointment table is currently not using but it added to model class when you decide to implement more than one appointments for same user.
(This feature is not urgent because customer can have returning customer after one year "Because they only shoot newborns and 1 year old babies")
We dont want user to create multiple shoots and appointments at the same time and matching them manually. This should be done automatically.
First thing that i came up with is only selecting future appointment and shoot_plan. If an appointment and shoot plan is not in future they can create new one and so on. You can also use is_active field if you want. If you use that strategy maybe you dont need to create shoot_appointment table but its your choice. Think wisely.


Mobile navigation bar display problem its because of fixing scrool you should also solve it somehow

Exporting appointments "Currently its only exporting e-mails of users who created appointment. You should add details for appointment maybe you should also add shoot_details."

You can also add changing num_of_concepts form concept selection screen maybe it would increase selected concepts because in that screen they will see how beautiful the concepts are.

You can implement shoot_times and Create calendar dynamically by lookin how many time fields exist.

You can also add create your own concepts by showing different concept items to user but maybe customer don't want this feature.


