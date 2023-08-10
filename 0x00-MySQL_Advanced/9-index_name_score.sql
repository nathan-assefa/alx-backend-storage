-- Creating index for name and score column
CREATE INDEX idx_name_first_score on names(name(1), score)
