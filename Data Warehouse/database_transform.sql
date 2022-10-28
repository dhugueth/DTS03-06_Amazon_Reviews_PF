USE skaivuinsights_db;

-- users_table
ALTER TABLE [dbo].[users_table] ALTER COLUMN reviewerID NVARCHAR(100) NOT NULL;
ALTER TABLE [dbo].[users_table] ADD CONSTRAINT PK_reviewerID PRIMARY KEY (reviewerID);

-- product table
ALTER TABLE facts_product_table ALTER COLUMN asinID VARCHAR(100) NOT NULL;
ALTER TABLE facts_product_table ADD CONSTRAINT PK_facts_product_table PRIMARY KEY (asinID);

-- facts_reviews
ALTER TABLE facts_reviews ADD CONSTRAINT PK_reviewID PRIMARY KEY (reviewID);
ALTER TABLE facts_reviews ADD CONSTRAINT FK_reviewerID FOREIGN KEY (reviewerID) REFERENCES users_table (reviewerID);
ALTER TABLE facts_reviews ADD CONSTRAINT FK_asinID FOREIGN KEY (asinID) REFERENCES facts_product_table (asinID);

-- facts_average_product
ALTER TABLE facts_average_product ALTER COLUMN asinID VARCHAR(100) NOT NULL;
ALTER TABLE facts_average_product ADD CONSTRAINT FK_asinID FOREIGN KEY (asinID) REFERENCES facts_product_table (asinID);

-- Analytics: helpfulness view
CREATE VIEW reviews_helpfulness AS
SELECT reviewID, helpfulness, date, 
CASE  
	WHEN (r.helpfulness >= 0.9) THEN 'Very Useful'
	WHEN (r.helpfulness >= 0.6) THEN 'Useful'
	WHEN (r.helpfulness >= 0.4) THEN 'A bit Useful'
	ELSE 'Unuseful' 
	END AS Utility
FROM facts_reviews r
WHERE YEAR(date) BETWEEN 2000 AND 2014;

-- Analytics overall view (star diagram)
CREATE VIEW reviews_overall AS 
SELECT reviewID, overall, date
FROM facts_reviews
WHERE YEAR(date) BETWEEN 2000 and 2014;

-- AsinID count
CREATE VIEW asinID_count_v2 AS 
SELECT asinID, date FROM [dbo].[facts_reviews]

-- Creating INDEX for DATE column
CREATE NONCLUSTERED INDEX [index_date] ON [dbo].[facts_reviews] ([date]) INCLUDE ([helpfulness], [overall]) 
WITH (ONLINE = ON)


