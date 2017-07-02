UPDATE open_pv SET date_installed = NULL WHERE date_installed = '';
UPDATE open_pv SET appraised = NULL WHERE appraised = '';
UPDATE open_pv SET size_kw = NULL WHERE size_kw = '';
UPDATE open_pv SET cost_per_watt = NULL WHERE cost_per_watt = '';
UPDATE open_pv SET zipcode = NULL WHERE zipcode='';
UPDATE open_pv SET cost_per_watt = NULL WHERE cost_per_watt = '';
UPDATE open_pv SET cost = NULL WHERE cost = '';
UPDATE open_pv SET lbnl_tts_version_year = NULL WHERE lbnl_tts_version_year = '';
UPDATE open_pv SET lbnl_tts = NULL WHERE lbnl_tts = '';
UPDATE open_pv SET annual_pv_prod = NULL WHERE annual_pv_prod = '';
UPDATE open_pv SET annual_insolation = NULL WHERE annual_insolation = '';
UPDATE open_pv SET rebate = NULL WHERE rebate = '';
UPDATE open_pv SET sales_tax_cost = NULL WHERE sales_tax_cost = '';
UPDATE open_pv SET tilt1 = NULL WHERE tilt1 = '';
UPDATE open_pv SET azimuth1 = NULL WHERE azimuth1 = '';
UPDATE open_pv SET reported_annual_energy_prod = NULL WHERE reported_annual_energy_prod = '';
UPDATE open_pv SET cost = NULL WHERE cost = 'n/a';
UPDATE open_pv SET rebate = NULL WHERE rebate = 'null';
UPDATE open_pv SET rebate = trim(leading '$' from rebate) WHERE rebate LIKE '$%';
UPDATE open_pv SET rebate = replace(rebate, ',', '') WHERE rebate LIKE '%,%';



ALTER TABLE open_pv
    ALTER COLUMN date_installed TYPE DATE USING date_installed::date,
    ALTER COLUMN size_kw TYPE DECIMAL USING size_kw::numeric,
    ALTER COLUMN appraised TYPE BOOLEAN USING appraised::boolean,
    ALTER COLUMN zipcode TYPE INTEGER USING zipcode::integer,
    ALTER COLUMN cost_per_watt TYPE DECIMAL USING cost_per_watt::numeric,
    ALTER COLUMN cost TYPE DECIMAL USING cost::numeric,
    ALTER COLUMN lbnl_tts_version_year TYPE INTEGER USING lbnl_tts_version_year::integer,
    ALTER COLUMN lbnl_tts TYPE BOOLEAN USING lbnl_tts::boolean,
    ALTER COLUMN annual_pv_prod TYPE DECIMAL USING annual_pv_prod::numeric,
    ALTER COLUMN annual_insolation TYPE DECIMAL USING annual_insolation::numeric,
    ALTER COLUMN rebate TYPE DECIMAL USING rebate::numeric,
    ALTER COLUMN sales_tax_cost TYPE DECIMAL USING sales_tax_cost::numeric,
    ALTER COLUMN tilt1 TYPE DECIMAL USING tilt1::numeric,
    ALTER COLUMN azimuth1 TYPE DECIMAL USING azimuth1::numeric,
    ALTER COLUMN reported_annual_energy_prod TYPE DECIMAL USING reported_annual_energy_prod::numeric;
