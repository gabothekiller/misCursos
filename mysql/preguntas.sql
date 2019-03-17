-- ¿ Que nacionalidades hay?
SELECT nationality FROM authors
GROUP BY nationality;

SELECT DISTINCT nationality FROM authors
-- ¿ Cuantos escritores hay de cada nacionalidad ?
SELECT nationality, COUNT(*) as `numero escritores` 
FROM authors
GROUP BY nationality
ORDER BY nationality;
-- ¿ cuantos libros hay de cada nacionalidad ?
SELECT a.nationality, COUNT(b.book_id)
FROM authors AS a
JOIN books AS b
ON b.author_id = a.author_id
GROUP BY nationality;
-- ¿ cual es el promedio / desviacion estandar del precio de libros?
SELECT AVG(price) as media, STDDEV(price) as `std dev` FROM books;
-- ¿ idem, pero por nacionalidad ?

-- ¿ cual es el precio maximo minimo de un libro?
SELECT MAX(price) as `max`, MIN(price) as `min` FROM books;