

CREATE TABLE open_pv_2010 as
(SELECT state, county,count(*), sum(size_kw) as total_size, avg(cost_per_watt) as average_cost_per_watt,sum(cost) as sum_cost FROM open_pv_county_updated
WHERE date_installed BETWEEN '2010-01-01' AND '2011-01-01'
GROUP BY state,county)

UPDATE open_pv_county_updated
SET year=date_part('year'::text, date_installed);

CREATE TABLE open_pv_byyear_bycounty_bystate as
(SELECT state,county,year,count(*),zip sum(size_kw) as total_size, avg(cost_per_watt) as average_cost_per_watt,sum(cost) as sum_cost FROM open_pv_county_year_updated
GROUP BY state,county,year);

SELECT count(*) from open_pv_byyear_bycounty_bystate where year='2010';

UPDATE open_pv_byyear_bycounty_bystate
SET county_code=county_fips_code
FROM concat_countycode
WHERE open_pv_byyear_bycounty_bystate.county = concat_countycode.county;

select * from open_pv_byyear_bycounty_bystate where state ='LA';
select * from concat_countycode where state ='LA';

UPDATE open_pv_byyear_bycounty_bystate SET concat_code = concat (state_code,county_code);

CREATE TABLE open_pv_2006 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2006');

CREATE TABLE open_pv_2007 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2007');

CREATE TABLE open_pv_2008 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2008');

CREATE TABLE open_pv_2009 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2009');

CREATE TABLE open_pv_2010 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2010');

CREATE TABLE open_pv_2011 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2011');

CREATE TABLE open_pv_2012 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2012');

CREATE TABLE open_pv_2013 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2013');

CREATE TABLE open_pv_2014 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2014');

CREATE TABLE open_pv_2015 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2015');

CREATE TABLE open_pv_2016 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2016');

CREATE TABLE open_pv_2017 as
(SELECT * FROM open_pv_byyear_bycounty_bystate where year='2017');


update open_pv_byyear_bycounty_bystate SET state_code=44 where state='RI';

update open_pv_byyear_bycounty_bystate SET state_code=72 where state='PR';

update open_pv_byyear_bycounty_bystate SET state_code=22 where state='LA';

update open_pv_byyear_bycounty_bystate SET state_code='09' where state='CT';

update open_pv_byyear_bycounty_bystate SET state_code=11 where state='DC';

update open_pv_byyear_bycounty_bystate SET county_code='001' where state='DC';

update open_pv_byyear_bycounty_bystate SET county_code='013' where state='CT' and county='Tolland';

update open_pv_byyear_bycounty_bystate SET county_code='011' where state='CT' and county='New London';

update open_pv_byyear_bycounty_bystate SET county_code='009' where state='CT' and county='New Haven';

update open_pv_byyear_bycounty_bystate SET county_code='005' where state='CT' and county='Litchfield';

update open_pv_byyear_bycounty_bystate SET county_code='005' where state='CT' and county='Hartford';

update open_pv_byyear_bycounty_bystate SET county_code='007' where state='RI' and county='Providence';

update open_pv_byyear_bycounty_bystate SET county_code='005' where state='RI' and county='Newport';


SELECT SUM(COUNT) FROM OPEN_PV_2016;

SELECT SUM(count) FROM open_pv_2017;


Create Table residential_instances_feature_set6.b as 
SELECT * FROM residential_instances_feature_set6;

UPDATE residential_instances_feature_set6 SET interconn_grade = '1' WHERE interconn.grade='A';

SELECT * INTO residential_instances_feature_set6.c From residential_instances_feature_set6;


CREATE TABLE feeding_the_grid_state_grades_numerical as 
(SELECT * from feeding_the_grid_state_grades);

UPDATE feeding_the_grid_state_grades_numerical SET interconn=1 WHERE interconn.grade='A';

"""
Tried to create table from view, but the following syntax did work

SELECT *
INTO x_predict02
FROM view x_predict00;wrong;

"""

""" Solution to the question above: create a table first, then use the following syntax"""
INSERT INTO x_predict01
SELECT * FROM x_predict00;

update x_predict01
set year=2017;

update x_predict01
set year_since_1990=28;

update x_predict01
set rounded_price_per_watt=4.21;

"""create table from view"""
INSERT INTO installation_price_per_watt
SELECT year,quarter,year_since_1990, residential_instances_feature_set7.rounded_price_per_watt FROM residential_instances_feature_set7;

create table intallation as
(select year_since_1990, avg(installation_price) from installation_price_per_watt group by year_since_1990);