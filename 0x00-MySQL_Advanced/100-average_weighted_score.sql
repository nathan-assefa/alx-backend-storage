-- Compute average to score
-- This is how we find weighted avarage in general
-- ===> Weighted Average Score = (Score1 * Weight1 + Score2 * Weight2 + ... + ScoreN * WeightN) / (Weight1 + Weight2 + ... + WeightN)
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE w_avg_score FLOAT;
    (SELECT SUM(score * weight) / SUM(weight) INTO w_avg_score
	FROM users AS U
        JOIN corrections as C ON U.id=C.user_id
        JOIN projects AS P ON C.project_id=P.id
        WHERE U.id=user_id);
    UPDATE users SET average_score = w_avg_score WHERE id=user_id;
END
//
DELIMITER ;
