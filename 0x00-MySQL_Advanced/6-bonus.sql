-- implementing stored procedues
-- updating students score
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score FLOAT
)
BEGIN
    -- Declare a variable to store the project ID
    DECLARE project_id INT;

    -- Check if the project already exists in the projects table
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If no project found, insert it and retrieve the generated ID
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
    -- Insert the correction record
    INSERT INTO corrections (user_id, project_name, score) VALUES (user_id, project_name, score);
END;
//
DELIMITER ;
