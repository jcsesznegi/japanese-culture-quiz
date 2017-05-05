


drop table if exists users;
create table users (
  id integer primary key auto_increment,
  email varchar(255) not null,
  user_agent text not null,
  insert_date datetime not null,
  name varchar(255) not null,
  last_login datetime
);


insert into users (email,user_agent,insert_date,name) values ("test@test.com","test user agent", CURDATE(), "Test McTesterson");



