DROP PROCEDURE IF EXISTS AddBonus;
-- Let us define the delimiter thereafter
DELIMITER $$
-- Let us define the stored procedure
CREATE PROCEDURE AddBonus(
        IN user_id INT,
        IN project_name VARCHAR(225),
        IN score DECIMAL(5, 2)
)
-- Here we begin the stored procedure
BEGIN
        DECLARE project_id INT;
        -- Let us then check if the project is already registered
        SELECT id INTO project_id FROM projects where projects.name = project_name;

        -- register the project if it is not registered yet
        IF project_id IS NULL THEN
                INSERT INTO projects(name) VALUES (project_name);
                -- SET project_id = LAST_INSERT_ID();
        END IF;
        SET project_id = (SELECT id FROM projects WHERE name = project_name);

        INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, project_id, score);
END;
$$
DELIMITER $$
