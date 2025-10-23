DROP TABLE IF EXISTS students;

CREATE TABLE students(
  id                serial PRIMARY KEY,
  first_name        varchar (50) NOT NULL,
  last_name         varchar (50) NOT NULL,
  age               integer NOT NULL,
  grade             varchar (15) NOT NULL
);

\COPY students FROM 'seed.csv' DELIMITER ',' CSV HEADER;