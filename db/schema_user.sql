drop table if exists users;
create table users(
	uid integer primary key autoincrement,
	username text not null unique,
	passwd_hash text not null,
	nickname text not null,
	email text not null
);