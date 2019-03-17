SELECT name, YEAR(NOW()) - YEAR(birthdate) FROM clients
WHERE gender = 'M' AND name LIKE '%fran%';

-- transactions

SELECT b.title , c.name, t.type
FROM transactions AS t
JOIN books AS b
ON t.book_id = b.book_id
JOIN clients AS c
ON t.client_id = c.client_id;
WHERE c.gender = 'F'


-- con author


SELECT b.title , c.name, t.type
FROM transactions AS t
JOIN books AS b
ON t.book_id = b.book_id
JOIN clients AS c
ON t.client_id = c.client_id;
JOIN authors AS a
ON a.author_id = b.author_id;
WHERE c.gender = 'F'

--- INNNER JOIN 

SELECT a.author_id, a.name, b.title
FROM authors AS a
JOIN books AS b
ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id DESC;

-- LEFT JOIN

SELECT a.author_id, a.name, b.title
FROM authors AS a
LEFT JOIN books AS b
ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id DESC;



--- GRUOP BY


SELECT a.author_id, a.name, b.title, COUNT(b.book_id)
FROM authors AS a
LEFT JOIN books AS b
ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5
GROUP BY a.author_id
ORDER BY a.author_id DESC;



SELECT a.author_id, a.name, b.title, b.book_id
FROM authors AS a
LEFT JOIN books AS b
ON a.author_id = b.author_id
WHERE a.author_id BETWEEN 1 AND 5
ORDER BY a.author_id DESC;



INSERT INTO empresas(nombre, direccion) VALUES ("Insumos S.A", "calle 44d no 67 - 98");

INSERT INTO trabajadores(empresa_id, nombre, celular) VALUES (1, "Gabriel Avendaño", "57+3154801320");