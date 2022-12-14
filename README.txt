# AvoidOnePieceSpoilers
This is a simple python script that uses PRAW to unsubscribe from a list of subreddits when the One Piece spoilers come out on Tuesday, and then resubscribe on Friday in time for the scans.


Setup:
- To get set up, simply move the folder into the directory you would like. 
- Then go in with notepad or any code editor if you have one installed, and enter your user agent information for PRAW into the file labeled 'example_config.ini'. You can get this information directly from your reddit account. You just go to https://www.reddit.com/prefs/apps/ and register your bot.
- It should look like this:
```
[reddit]                                                                                                                                                                                                                                                        
user_agent = Bot_Name_Here
client_id = Id_Here
client_secret = Secret_here
username = Username_here
password = Password_here
```
- You will want to then save the '.ini' file as 'config.ini'. This will allow the program to recognize it as the copy you provide.
- Then start the task scheduler that comes installed (it's just called 'task scheduler' in windows). Add the file labled 'OnePiece_Spoiler_Blocker.exe' to the scheduled time you would like to have the program check if it is the day you would like to unsubscribe to the subreddits you have listed. I reccomend scheduling it sometime early like 1 or 2 am so you dont wake up early one day and get spoiled by accident. I scheduled mine to run every day at 2am.
- To set up the time period you would like to be unsubscribed for you can start the file called 'Set_unsub_times.exe'. This will allow you to mark on a callendar what day you would like to unsubscribe next, and then when you would like to re-subscribe back to the subreddits you have listed.
- This is what it should look like:


![example1](/images/Example_Photo.png)
##
Usage:
- To use the program to set the dates you would like to be unsubscribed for, it's pretty simple. You just click the day you would like to unsubscribe, then click to set the beginning of the time period.

![example2](/images/example_photo2.png)
- Then you click the end date, and click to submit.
- Click To get the timeframe, to make sure your dates are correct.
- Then click to confirm.
