-- 1.1. Создайте студента (student)
INSERT INTO students (name, second_name) VALUES ('Kate', 'Goncharova')

-- 1.2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('Алиса в Стране чудес', 1654)
INSERT INTO books (title, taken_by_student_id) VALUES ('Евгений Онегин', 1654)

-- 1.3. Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) VALUES ('AutoQA Python', 'июнь 2024', 'сентябрь 2024')
UPDATE students SET group_id = 1590 WHERE id = 1654

-- 1.4. Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES ('Test design')
INSERT INTO subjets (title) VALUES ('API')

-- 1.5. Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES ('HTTP', 2116)
INSERT INTO lessons (title, subject_id) VALUES ('REST', 2116)
INSERT INTO lessons (title, subject_id) VALUES ('Equivalence Class Testing', 2115)
INSERT INTO lessons (title, subject_id) VALUES ('Pairwise test design', 2115)

-- 1.6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 4711, 1654)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 4710, 1654)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 4708, 1654)
INSERT INTO marks (value, lesson_id, student_id) VALUES ('5', 4709, 1654)

-- 2.1. Все оценки студента 
SELECT title, value FROM marks m JOIN lessons l ON m.lesson_id = l.id WHERE m.student_id = 1654

-- 2.2. Все книги, которые находятся у студента
SELECT title FROM books b WHERE taken_by_student_id = 1654

-- 2.3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)
SELECT g.title as 'Название группы', b.title as 'Книга', m.value as 'Оценка', l.title as 'Занятие', s2.title as 'Предмет'
FROM students s
JOIN `groups` g ON s.group_id = g.id 
JOIN books b ON s.id = b.taken_by_student_id 
JOIN marks m ON m.student_id = s.id 
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id 
WHERE s.id = 1654