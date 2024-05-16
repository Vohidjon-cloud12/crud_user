create table crudtable(
    id serial primary key ,
    username varchar(80) not null ,
    email varchar(255) not null unique,
    password varchar(80),
    phone varchar(25)

);