# recurring-task-reminder
Send emails on specified dates to remind people of recurring tasks that need doing.


## Setup

1. Clone this repository
2. Copy `config.json.template` to `config.json` and edit it to contain proper values
3. Set up a cronjob that runs `recurring-task-reminder.py` once a day


## Adding, Modifying, and Removing Recipients

Each recipient of reminders consists of a subfolder within `taks` and an entry in `config.json` that links the name of the subfolder to an email address.

To add a recipient, add a subfolder within `tasks` and add a corresponding entry in `config.json`.

To edit the email address for a recipient, edit the corresponding entry in `config.json`.

To remove a recipient, delete the subfolder within `tasks` and remove the entry in `config.json`.


## Adding, Modifying, and Removing Reminders

Each reminder consists of a text file in a recipient subdirectory within `taks`.
The date on which the reminder is supposed to be sent is given at the start of the file name in the format `mm-dd-`.
The contents of the file are structured as follows:

1. The first line is the email subject
2. The second line is empty
3. The third line and onwards is the body of the email

For example: A file called `02-29-hey-its-a-leap-year.txt` would contain an email that is being sent each February 29th.

To add a reminder, create and fill a new file in the recipient subfolder of your choice.

To modify the subject or content of a reminder, edit the corresponding text file.

To remove a reminder, delete the corresponding text file.

