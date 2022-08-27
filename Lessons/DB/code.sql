show databases

select *
from 
steve.ineuron

use steve

select *
from ineuron

create table if not exists bank_details 
(
age int,
job varchar(30),
marital varchar(30),
education varchar(30),
`default` varchar(30),
balance int,
housing varchar(30),
loan varchar(30),
contact varchar(30),
`day` int,
`month` varchar(30),
duration int,
campaign int,
pdays int,
previous int,
poutcome varchar(30),
y varchar(30)
)

show tables

describe bank_details

insert into bank_details values 
(58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no")

select * from bank_details

insert into bank_details values
(44,"technician","single","secondary","no",29,"yes","no","unknown",5,"may",151,1,-1,0,"unknown","no"),
(33,"entrepreneur","married","secondary","no",2,"yes","yes","unknown",5,"may",76,1,-1,0,"unknown","no"),
(47,"blue-collar","married","unknown","no",1506,"yes","no","unknown",5,"may",92,1,-1,0,"unknown","no"),
(33,"unknown","single","unknown","no",1,"no","no","unknown",5,"may",198,1,-1,0,"unknown","no"),
(35,"management","married","tertiary","no",231,"yes","no","unknown",5,"may",139,1,-1,0,"unknown","no"),
(28,"management","single","tertiary","no",447,"yes","yes","unknown",5,"may",217,1,-1,0,"unknown","no"),
(42,"entrepreneur","divorced","tertiary","yes",2,"yes","no","unknown",5,"may",380,1,-1,0,"unknown","no"),
(58,"retired","married","primary","no",121,"yes","no","unknown",5,"may",50,1,-1,0,"unknown","no"),
(43,"technician","single","secondary","no",593,"yes","no","unknown",5,"may",55,1,-1,0,"unknown","no"),
(41,"admin.","divorced","secondary","no",270,"yes","no","unknown",5,"may",222,1,-1,0,"unknown","no"),
(29,"admin.","single","secondary","no",390,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),
(53,"technician","married","secondary","no",6,"yes","no","unknown",5,"may",517,1,-1,0,"unknown","no"),
(58,"technician","married","unknown","no",71,"yes","no","unknown",5,"may",71,1,-1,0,"unknown","no"),
(57,"services","married","secondary","no",162,"yes","no","unknown",5,"may",174,1,-1,0,"unknown","no"),
(51,"retired","married","primary","no",229,"yes","no","unknown",5,"may",353,1,-1,0,"unknown","no"),
(45,"admin.","single","unknown","no",13,"yes","no","unknown",5,"may",98,1,-1,0,"unknown","no"),
(57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),
(60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no"),
(33,"services","married","secondary","no",0,"yes","no","unknown",5,"may",54,1,-1,0,"unknown","no"),
(28,"blue-collar","married","secondary","no",723,"yes","yes","unknown",5,"may",262,1,-1,0,"unknown","no"),
(56,"management","married","tertiary","no",779,"yes","no","unknown",5,"may",164,1,-1,0,"unknown","no")

select * 
from steve.bank_details

select distinct job
from steve.bank_details

use steve

select *
from bank_details 
where balance = (select min(balance) 
				from bank_details)

select count(*), marital
from bank_details
group by marital

set sql_safe_updates = 0 
update bank_details set balance=0 where job='unknown'
update bank_details set `default` = 'NULL' where `default` = 'no'

delete from bank_details
where job='unknown'

DELIMITER &&

create procedure select_pre()
BEGIN
	select * from bank_details;
END &&

call select_pre()


DELIMITER &&

create procedure select_pre2(IN var1 int)
BEGIN
	select * from bank_details where job='retired' and balance>var1;
END &&

call select_pre2(100)


DELIMITER &&

create procedure select_pre3(IN var1 int, IN var2 varchar(30))
BEGIN
	select * from bank_details where job=var2 and balance>var1;
END &&

call select_pre3(100,'services')

select *
from
(select job, age, education, y
from bank_details) as a 
where a.age=58

create view bank_view
as
select job, age, education, y 
from bank_details

select *
from bank_view 
where age=58



create table if not exists bank_details1 
(
age int,
job varchar(30),
marital varchar(30),
education varchar(30),
`default` varchar(30),
balance int,
housing varchar(30),
loan varchar(30),
contact varchar(30),
`day` int,
`month` varchar(30),
duration int,
campaign int,
pdays int,
previous int,
poutcome varchar(30),
y varchar(30)
)


insert into bank_details1 select * from bank_details

select bank_details1.age, bank_details1.job, bank_details1.marital 
from bank_details
inner join bank_details1 on bank_details.age = bank_details1.age


select *
from bank_details1

insert into bank_details1 values (
37, 
'product manager',	
'single', 
'tertiary',
NULL,
2,
'yes',
'yes',
'unknown',
5,
'may',
76,	
1,
-1,
0,	
'unknown',
'no'
)


insert into steve.bank_details1 values (37,'product manager','single','tertiary','NULL',2,'yes','yes','unknown',5,'may',76,1,-1,0,'unknown','no')


select *
from steve.bank_details1
where age = 37