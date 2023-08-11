-- Compute average to score
-- This is how we find weighted avarage in general
-- ===> Weighted Average Score = (Score1 * Weight1 + Score2 * Weight2 + ... + ScoreN * WeightN) / (Weight1 + Weight2 + ... + WeightN)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE weight_avg_score FLOAT;
    (SELECT SUM(score * weight) / SUM(weight) INTO weight_avg_score
	FROM users
        JOIN corrections ON users.id=corrections.user_id
        JOIN projects AS projects ON corrections.project_id=projects.id
        WHERE users.id=user_id);
    UPDATE users SET average_score = weight_avg_score WHERE id=user_id;
END
//
DELIMITER ;
