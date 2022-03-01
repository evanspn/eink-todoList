# eink-todoList
Code to use a Raspberry Pi Zero as an automatically updating to do list that gathers information from a google sheets worksheet.

If you plan to use this yourself the file contents of "eink-todoList/v1/credential_key_file_pomodoro.json" will need to be populated with your own private api key from google.
Instructions on how to obtain this key can be found here: https://cloud.google.com/iam/docs/creating-managing-service-account-keys

This project used a waveshare display and includes the driver files for waveshare displays. It is necessary to use the correct driver file otherwise the display will not respond. Any type of display could be used but an eink display is preferable since they can display information without using power after they are updated.
