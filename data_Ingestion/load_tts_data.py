import csv

import psycopg2

mydb = psycopg2.connect(host='', dbname='', user='', password='')
cursor = mydb.cursor()
print ("Start")
i = 0

with open('TTS_LBNL_OpenPV_public_file_06-Jan-2017.csv','rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sql_input = '' 
        for k,v in row.iteritems():
            if(k == 'City' or k == 'State' or k == 'County' or k == 'Utility Service Territory'
                 or  k == 'Street Address' or k == 'System Id From Data Provider'):
                sql_input += "'" + v + "',"
            elif(k == 'System Size'):
                sql_input +=  v 
            else:
                sql_input +=  v + ','
        print(sql_input)
        cursor.execute("""INSERT INTO tts (performance_based_incentives_duration,city,azimuth_1,module_manufacturer_2,module_manufacturer_3,azimuth_3,azimuth_2,
         	 	   inverter_cost,battery_system,insolation_rate,estimated_annual_pv_generation,state,permitting_cost,tilt_1,tilt_3,tilt_2,module_model_3,
			   module_model_2,feed_in_tariff_duration,sales_tax_cost,new_construction,module_efficiency_2,module_efficiency_3,county,utility_service_territory,
			   street_address,system_id_from_data_provider,module_manufacturer_1,zip_code,feed_in_tariff_annual_payment,total_installed_price,module_efficiency_1,
		           self_installed,customer_segment,module_cost,rebate_or_grant,dc_optimizer,bipv_module_2,bipv_module_3,installer_name,tracking,
			   installation_labor_cost,inverter_manufacturer,data_provider,performance_based_incentive_annual_payment,third_party_owned,module_technology_3,
 	    	           system_id_tracking_the_sun,reported_annual_pv_generation,module_technology_1,ground_mounted,tracking_type,installation_date,appraised_value_flag,
                           module_technology_2,module_model_1,inverter_model,microinverter,balance_of_systems_cost,bipv_module_1,system_size) 
                           VALUES ({})""".format(sql_input)) 
        print("Inserting record no " + str(i))
        mydb.commit()
        i += 1

print('Done')

