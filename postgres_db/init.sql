CREATE TABLE public.users (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    password varchar(255)
);