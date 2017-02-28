# 291project1

**Database Specification

You are given the following relational schema.

users(usr,pwd, name,email,city,timezone)<br>
follows(flwer,flwee,start_date)<br>
tweets(tid,writer,tdate,text,replyto)<br>
hashtags(term)<br>
mentions(tid,term)<br>
retweets(usr,tid,rdate)<br>
lists(lname,owner)<br>
includes(lname,member)<br>
Tables are derived from the Assignment 1 spec and are identical to those in Assignment 2 except the field pwd which is added to users, and the change in the key of table tweets and in the definition of tables that reference the table tweets. The SQL commands to create the tables of the system are given here. Use the given schema in your project and do not change any table/column names as we will be testing your project with the given schema.

**Login Screen

The first screen should provide options for both registered and unregistered users. There must be also an option to exit the program. Registered users should be able to login using a valid user id and password, respectively referred to as usr and pwd in table users. After a registered user signs in, the system should list all tweets or retweets from users who are being followed; the tweets should be ordered based on date from the latest to the oldest. If there are more than 5 such tweets, only 5 would be shown and the user would be given an option to see more but again 5 at a time. The user should be able to select a tweet and see some statistics about the tweet including the number of retweets and the number of replies. Also the user should be able to compose a reply to it (see the section on composing a tweet), or retweet it (i.e. repost it to all people who follow the user).

Unregistered users should be able to sign up by providing a name, email, city, timezone and password. The user id (i.e. the field usr in table users) should be provided by the system and be unique. After a successful login or signup, users should be able to perform the subsequent operations (possibly chosen from a menu) as discussed next.

**System Functionalities

Users should be able to perform all of the following tasks:

**1. Search for tweets.** The user should be able to enter one or more keywords and the system should retrieve every tweet that match at least one of the keywords. A tweet matches a keyword if (1) the keyword has the prefix # and it is mentioned by the tweet as a hashtag, or (2) the keyword doesn't have the prefix # and it appears in the tweet text. (The symbol # is not part of any keyword and only indicates that the keyword that follows is expected to appear as a hashtag. Also tweets can have hashtags which do not explicitly appear in the tweet text.) The tweets should be ordered based on date from the latest to the oldest. If there are more than 5 matching tweets, only 5 would be shown and the user would be given an option to see more but again 5 at a time. The user should be able to select a tweet and see some statistics about the tweet including the number of retweets and the number of replies. Also the user should be able to compose a reply to a tweet (see the section on composing a tweet), or retweet it (i.e. repost it to all people who follow the user).<br>
**2. Search for users.** The user should be able to enter a keyword and the system should retrieve all users whose names or cities contain the keyword. The result would be sorted as follows: first, all users whose name match the keyword would be listed and these users would be sorted in an ascending order of name length. This would be followed by the list of users whose city but not name match the keyword and this result would be sorted in an ascending order of city length. If there are more than 5 matching users, only 5 would be shown and the user would be given an option to see more but again 5 at a time. The user should be able to select a user and see more information about him/her including the number of tweets, the number of users being followed, the number of followers and up to 3 most recent tweets. The user should be given the option to follow the user or see more tweets.<br>
**3. Compose a tweet.** The user should be able to compose a tweet. A tweet can have hashtags which are marked with a # before each hashtag. Information about hashtags must be stored in tables mentions and if needed in hashtags.<br>
**4. List followers.** The user should be able to list all users who follow him/her. From the list, the user should be able to select a follower and see more information about the follower including the number of tweets, the number of users being followed, the number of followers and up to 3 most recent tweets. The user should be given the option to follow the selected user or see more tweets.<br>
**5. Manage lists.** The user should be able (a) to get a listing of his lists, (b) to see the lists that he is on, (c) to create a list, and (d) to add or delete members to hist lists.
**6. Logout.** There must be an option to log out of the system.
Task 5 is required for groups of size 3 only.

**Testing

At development time you will be testing your programs with your own data sets (make sure that it conforms to the project specification). At demo time we will be creating the database using these SQL statements and will be populating it with our own test data set. Your application will be tested under a demo account (and not under your account).
The demo will be run using the source code submitted and nothing else. Therefore, it is essential to include every file that is needed to compile and run your code including all source code and any makefile or script that you may use to compile or run your code. You will neither be able to change your code, nor use any file other than those submitted. This policy can be altered only in exceptional cases at the instructor's discretion and for a hefty penalty. The code will be executed under a TA account. Do not hard-code username, password or table prefixes (such as username or group name) in your code. As a test drill, you should be able to set up your application under someone else's account (in case of testing, this would be under a TA account) within 3 minutes at most.

Every group will book a time slot convenient to all group members to demo their projects. At demo time, all group members must be present. The TA will be using a script to both create and populate the tables. The TA will be asking you to perform various tasks and show how your application is handling each task. A mark will be assigned to your demo immediately after the testing
