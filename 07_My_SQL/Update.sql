USE schoolDB;
UPDATE students SET age = age + 1 WHERE age < 18;
SELECT * from students;