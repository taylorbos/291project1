-- Data prepared by Derrick Wai, dwai@ualberta.ca
-- Published on Feb 4, 2017
-- Meme DLC Pack

insert into users values (1,'ryan','Ryan Nugent-Hopkins','rnh@nhl.com','Edmonton',-7);
insert into users values (2,'jord','Jordan Eberle','jeb@nhl.com','Edmonton',-7);
insert into users values (3,'davo','Davood Rafiei','dr@UAwiter.com','Edmonton',-7);
insert into users values (4,'john','john doe','john@gmail.com','Toronto',-5);
insert into users values (6,'doe','John Doe','doe@gmail.com','Edmonton',-7);
insert into users values (14,'jade','Jaden Smith','jaden@twit.com','Malibu',-8);
insert into users values (15,'kevi','Kevin Chan','kchn@gmail.com','Edmonton',-7);
insert into users values (22,'don','Don Iveson','don@don.ca','Edmonton',-7);
insert into users values (25,'jim','Jim Wu','jim@gmail.com','Calgary',-7);
insert into users values (29,'bush','George Bush','bush@twit.com','Washington',-5);
insert into users values (41,'wai','Derrick Wai','dwai@dwai.ca','Edmonton',-7);
insert into users values (67,'tay','Taylor Swift','tswift@twit.com','Nashville',-6);
insert into users values (77,'joff','Joffrey Lupul','jlu@nhl.com','Toronto',-5);
insert into users values (83,'cage','Nicolas Cage','nic@twit.com','Sacramento',-7);
insert into users values (99,'sad','Donald Trump','potus@u.gov','Washington',-5);

insert into follows values (2,1,'01-SEP-2015');
insert into follows values (3,1,'26-AUG-2016');
insert into follows values (6,1,'28-AUG-2015');
insert into follows values (77,1,'5-JUN-2014');
insert into follows values (1,2,'17-SEP-2016');
insert into follows values (3,2,'10-JAN-2015');
insert into follows values (6,2,'02-SEP-2016');
insert into follows values (77,2,'16-OCT-2016');
insert into follows values (15,3,'17-MAR-2015');
insert into follows values (41,3,'15-JUL-2016');
insert into follows values (3,4,'10-OCT-2016');
insert into follows values (15,4,'28-MAR-2016');
insert into follows values (22,4,'20-APR-2015');
insert into follows values (25,4,'01-JUN-2016');
insert into follows values (29,4,'17-SEP-2016');
insert into follows values (41,4,'05-AUG-2015');
insert into follows values (3,14,'06-FEB-2016');
insert into follows values (4,14,'15-MAY-2016');
insert into follows values (6,14,'17-DEC-2016');
insert into follows values (15,14,'17-AUG-2016');
insert into follows values (25,14,'26-MAY-2015');
insert into follows values (29,14,'10-FEB-2014');
insert into follows values (15,25,'15-DEC-2016');
insert into follows values (41,25,'28-DEC-2016');
insert into follows values (1,67,'03-JUN-2016');
insert into follows values (2,67,'24-MAY-2016');
insert into follows values (4,67,'16-JUN-2016');
insert into follows values (6,67,'11-MAY-2016');
insert into follows values (14,67,'07-MAR-2016');
insert into follows values (15,67,'13-FEB-2016');
insert into follows values (77,67,'21-MAR-2016');
insert into follows values (83,67,'31-JAN-2016');
insert into follows values (1,77,'17-DEC-2016');
insert into follows values (2,77,'30-DEC-2016');
insert into follows values (4,77,'26-OCT-2016');
insert into follows values (1,83,'30-SEP-2016');
insert into follows values (2,83,'07-JUL-2016');
insert into follows values (3,83,'11-DEC-2016');
insert into follows values (4,83,'15-AUG-2016');
insert into follows values (6,83,'23-SEP-2016');
insert into follows values (14,83,'19-APR-2016');
insert into follows values (15,83,'08-SEP-2016');
insert into follows values (22,83,'26-FEB-2016');
insert into follows values (67,83,'10-OCT-2016');
insert into follows values (99,83,'28-AUG-2016');
insert into follows values (14,99,'07-MAR-2016');
insert into follows values (29,99,'25-JAN-2016');
insert into follows values (67,99,'18-JAN-2016');
insert into follows values (83,99,'22-APR-2016');

insert into tweets values (1,1,'01-JUL-2014','Roses are red, politics are gory, I fear my cat is a Tory #rosesarered', null);
insert into tweets values (2,1,'01-JAN-2017','Looking for a good book to read. Just finished lone #survivor', null);
insert into tweets values (3,2,'12-JAN-2017','#Edmonton #Oilers had a good game last night.',null);
insert into tweets values (4,3,'03-DEC-2016','A big thanks to all the wonderful TAs that made teaching CMPUT 291 possible #UoA #edmonton',null);
insert into tweets values (5,4,'19-MAR-2016','Shoutout to all the average joes out there!',null);
insert into tweets values (6,4,'30-JAN-2016','Super confused about the music video for Taylors new song #taylorswift',23);
insert into tweets values (7,4,'22-JAN-2016','Good effort against the #Edmonton #Oilers last night #Toronto Maple #Leafs',null);
insert into tweets values (8,6,'15-FEB-2016','First tweet! Hello world! Hello #Edmonton!',null);
insert into tweets values (9,6,'29-NOV-2016','Is anyone else in #edmonton super excited to get their hands on Jim Wus new mixtape? #jimismoving',17);
insert into tweets values (10,14,'11-MAY-2016','Most Trees Are Blue #juvenilephilosophy',null);
insert into tweets values (11,14,'28-MAY-2016','How Can Mirrors Be Real If Our Eyes Arent Real #juvenilephilosophy',null);
insert into tweets values (12,14,'04-SEP-2016','Water In The Eyes And Alcohol In The Eyes Are Pretty Much The Same I Know This From First Hand Experience. #juvenilephilosophy',null);
insert into tweets values (13,14,'20-NOV-2016','If Newborn Babies Could Speak They Would Be The Most Intelligent Beings On Planet Earth #juvenilephilosophy',null);
insert into tweets values (14,15,'28-MAY-2016','Glad that todays youth have Jaden to spread #juvenilephilosophy',11);
insert into tweets values (15,22,'27-MAR-2015','Hope everyone in #edmonton is enjoying the Tallus Dome as much as I am!',null);
insert into tweets values (16,22,'03-MAY-2016','My apologies #edmonton, the Metro line has been delayed to 2018',null);
insert into tweets values (17,25,'25-JUL-2016','hey girl, feel my sweater, know what its made of? boyfriend material',null);
insert into tweets values (18,25,'25-NOV-2016','bout to drop the hottest mixtape of 2016!!!! its gonna be lit #jimismoving',null);
insert into tweets values (19,29,'15-FEB-2016','Roses are red, I love my wife, marrying her was the biggest mistake of my life #rosesarered',25);
insert into tweets values (20,29,'13-JUL-2016','Roses are red, rice is plain, please vote me into office again #america #rosesarered',28);
insert into tweets values (21,29,'16-DEC-2016','#America, this isnt what we meant when we said orange is the new black..',28);
insert into tweets values (22,41,'13-JUL-2016','Roses are red, deers eat flowers, creating this database took 10 hours #rosesarered',null);
insert into tweets values (23,67,'29-JAN-2016','The music video for Bad Blood is out now! #taylorswift',null);
insert into tweets values (24,67,'18-NOV-2014','Were breaking up? Guess Ill write a song and make another million bucks! #taylorswift',null);
insert into tweets values (25,77,'14-FEB-2016','Roses are red, chocolates are brown, I expect nothing and Im still let down #rosesarered',null);
insert into tweets values (26,83,'14-FEB-2014','Tell me Im your national treasure',null);
insert into tweets values (27,83,'16-DEC-2016','Now that the government is shut down, Im gonna steal the declaration of independence',30)
insert into tweets values (28,99,'15-DEC-2016','Cant stump the #trump! #america',null);
insert into tweets values (29,99,'17-DEC-2016','Dont talk to me or my son or my grandson ever again',19);
insert into tweets values (30,99,'18-DEC-2016','WE MUST MAKE #AMERICA GREAT AGAIN!',null);

insert into hashtags values ('survivor');
insert into hashtags values ('oilers');
insert into hashtags values ('edmonton');
insert into hashtags values ('trump');
insert into hashtags values ('juvenilephilosophy');
insert into hashtags values ('jimismoving');
insert into hashtags values ('rosesarered');
insert into hashtags values ('leafs');
insert into hashtags values ('toronto');
insert into hashtags values ('UoA');
insert into hashtags values ('america');
insert into hashtags values ('taylorswift');

insert into mentions values (1, 'rosesarered');
insert into mentions values (2, 'survivor');
insert into mentions values (3, 'edmonton');
insert into mentions values (3, 'oilers');
insert into mentions values (3, 'edmonton');
insert into mentions values (4, 'UoA');
insert into mentions values (4, 'edmonton');
insert into mentions values (6, 'taylorswift');
insert into mentions values (7, 'edmonton');
insert into mentions values (7, 'oilers');
insert into mentions values (7, 'toronto');
insert into mentions values (7, 'leafs');
insert into mentions values (8, 'edmonton');
insert into mentions values (9, 'edmonton');
insert into mentions values (9, 'jimismoving');
insert into mentions values (10, 'juvenilephilosophy');
insert into mentions values (11, 'juvenilephilosophy');
insert into mentions values (12, 'juvenilephilosophy');
insert into mentions values (13, 'juvenilephilosophy');
insert into mentions values (14, 'juvenilephilosophy');
insert into mentions values (15, 'edmonton');
insert into mentions values (16, 'edmonton');
insert into mentions values (18, 'jimismoving');
insert into mentions values (19, 'rosesarered');
insert into mentions values (20, 'america');
insert into mentions values (20, 'rosesarered');
insert into mentions values (21, 'america');
insert into mentions values (22, 'rosesarered');
insert into mentions values (23, 'taylorswift');
insert into mentions values (24, 'taylorswift');
insert into mentions values (25, 'rosesarered');
insert into mentions values (28, 'trump');
insert into mentions values (28, 'america');
insert into mentions values (30, 'america');

insert into retweets values (1,3,'12-JAN-2017');
insert into retweets values (5,3,'14-JAN-2017');
insert into retweets values (41,4,'04-DEC-2016');
insert into retweets values (6,5,'21-MAR-2016');
insert into retweets values (1,7,'22-JAN-2016');
insert into retweets values (2,7,'22-JAN-2016');
insert into retweets values (3,7,'22-JAN-2016');
insert into retweets values (6,7,'22-JAN-2016');
insert into retweets values (15,7,'22-JAN-2016');
insert into retweets values (41,7,'22-JAN-2016');
insert into retweets values (15,10,'11-MAY-2016');
insert into retweets values (15,10,'28-MAY-2016');
insert into retweets values (15,12,'04-SEP-2016');
insert into retweets values (15,10,'20-NOV-2016');
insert into retweets values (25,10,'11-MAY-2016');
insert into retweets values (25,11,'28-MAY-2016');
insert into retweets values (29,10,'11-MAY-2016');
insert into retweets values (29,11,'28-MAY-2016');
insert into retweets values (29,12,'04-SEP-2016');
insert into retweets values (29,13,'20-NOV-2016');
insert into retweets values (67,10,'28-MAY-2016');
insert into retweets values (99,11,'28-MAY-2016');
insert into retweets values (15,17,'25-NOV-2016');
insert into retweets values (1,22,'13-JUL-2016');
insert into retweets values (2,22,'13-JUL-2016');
insert into retweets values (3,22,'13-JUL-2016');
insert into retweets values (4,22,'13-JUL-2016');
insert into retweets values (6,22,'13-JUL-2016');
insert into retweets values (14,22,'13-JUL-2016');
insert into retweets values (15,22,'13-JUL-2016');
insert into retweets values (22,22,'13-JUL-2016');
insert into retweets values (25,22,'13-JUL-2016');
insert into retweets values (29,22,'13-JUL-2016');
insert into retweets values (41,22,'13-JUL-2016');
insert into retweets values (67,22,'13-JUL-2016');
insert into retweets values (77,22,'13-JUL-2016');
insert into retweets values (83,22,'13-JUL-2016');
insert into retweets values (99,22,'13-JUL-2016');
insert into retweets values (1,23,'29-JAN-2016');
insert into retweets values (2,23,'29-JAN-2016');
insert into retweets values (4,23,'29-JAN-2016');
insert into retweets values (15,23,'29-JAN-2016');
insert into retweets values (1,26,'14-FEB-2014');
insert into retweets values (2,26,'14-FEB-2014');
insert into retweets values (3,26,'14-FEB-2014');
insert into retweets values (4,26,'14-FEB-2014');
insert into retweets values (6,26,'14-FEB-2014');
insert into retweets values (14,26,'14-FEB-2014');
insert into retweets values (15,26,'14-FEB-2014');
insert into retweets values (22,26,'14-FEB-2014');
insert into retweets values (25,26,'14-FEB-2014');
insert into retweets values (29,26,'14-FEB-2014');
insert into retweets values (67,26,'14-FEB-2014');
insert into retweets values (77,26,'14-FEB-2014');
insert into retweets values (3,29,'17-DEC-2014');
insert into retweets values (14,29,'17-DEC-2014');
insert into retweets values (67,29,'17-DEC-2014');


insert into lists values ('american',4);
insert into lists values ('canadian',4);
insert into lists values ('celebrity',4);
insert into lists values ('music',15);
insert into lists values ('nhl players',3);
insert into lists values ('politics',22);

insert into includes values ('american',14);
insert into includes values ('american',29;
insert into includes values ('american',67);
insert into includes values ('american',83);
insert into includes values ('american',99);
insert into includes values ('canadian',1);
insert into includes values ('canadian',2);
insert into includes values ('canadian',3);
insert into includes values ('canadian',4);
insert into includes values ('canadian',6);
insert into includes values ('canadian',15);
insert into includes values ('canadian',22);
insert into includes values ('canadian',25);
insert into includes values ('canadian',41);
insert into includes values ('canadian',77);
insert into includes values ('celebrity',1);
insert into includes values ('celebrity',2);
insert into includes values ('celebrity',14);
insert into includes values ('celebrity',29);
insert into includes values ('celebrity',67);
insert into includes values ('celebrity',77);
insert into includes values ('celebrity',83);
insert into includes values ('celebrity',99);
insert into includes values ('music',14);
insert into includes values ('music',25);
insert into includes values ('music',67);
insert into includes values ('nhl players',1);
insert into includes values ('nhl players',2);
insert into includes values ('nhl players',77);
insert into includes values ('politics',22);
insert into includes values ('politics',29);
insert into includes values ('politics',99);
