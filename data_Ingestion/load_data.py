import csv
import psycopg2

mydb = psycopg2.connect(host='',
                        dbname='', user='', password='')
cursor = mydb.cursor()
print ("Start")
csv_data = csv.reader(file('openpv_all.csv'))
i = 0;
for row in csv_data:
    if (len(row) > 0):
        treated_row = "','".join([row[0],row[1],row[2],row[3],row[4],row[5],
                        row[6],row[7].replace("'","''"),row[8].replace("'","''"),row[9],row[10],row[11],row[12],row[13].replace("'","''"),
                        row[14].replace("'","''"),row[15],row[16],row[17].replace("'","''"),
                        row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[29]])
        print(treated_row)
        #print ', '.join(row)
        print("Inserting record no " + str(i))
        cursor.execute("""INSERT INTO open_pv (state,date_installed,incentive_prog_names,type,size_kw,appraised,
                          zipcode,install_type,installer,cost_per_watt,cost,lbnl_tts_version_year,lbnl_tts,city,
                          utility_clean,tech_1,model1_clean,county,annual_PV_prod,annual_insolation,rebate,
                          sales_tax_cost,tilt1,tracking_type,azimuth1,reported_annual_energy_prod)
                          VALUES ('{}')""".format(treated_row))
        mydb.commit()
        i += 1
cursor.close()
print ("Done")
