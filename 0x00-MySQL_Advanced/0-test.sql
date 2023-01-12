-- test task-0
SELECT * FROM users;
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");
INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");
SELECT * FROM users;
