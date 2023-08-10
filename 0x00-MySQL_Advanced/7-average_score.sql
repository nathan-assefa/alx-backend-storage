-- Writing a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
-- The first thing is setting the delimiter
DELIMITER //
-- We then create the PROCEDURE if not exist
CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE user_score DECIMAL(5, 2);

    -- Calculate the average score and count of user's corrections
    SELECT AVG(score) INTO user_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = user_score
    WHERE id = user_id;
END;
//
DELIMITER ;
