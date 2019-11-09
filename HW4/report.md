# Overview
This dataset is about the consumer service complaint. 
The link is: https://data.cityofnewyork.us/Business/Consumer-Services-Mediated-Complaints/nre2-6m2s

The cleaned csv contains following information:

Industry: The business category that a complaint has been made.
Complaint Type: the type of complaint that customer made.
Mediation Start Date: The date that mediation started.
Mediation Close Date: The date that mediation closed. 
Complaint Result: Outcome of mediation efforts. Data type: String.
Satisfaction: Customer is satisfied or not. Data type: Boolean(represented as Yes or No String).
Business City: The city name where the business is located. Data type: String.
Business State: The state name where the business is located. Data type: String.

# Table Design
Since I think there is no good candidate for primary key, I created a serial as artifical primary key.
for complaint_type, I made it varchar(255)
for mediation_start_date, I made it varchar(255)
for mediation_close_date, I made it varchar(255)
for complaint_result, I made it varchar(255)
for satisfaction, I made it boolean. This column allows null since in the satisfaction could be unknown.
for business_city, I made it varchar(255)
for business_state, I made it varchar(255)


# Import
import succeeded without any error. 

# Database Information
(the lanugage of my operating system is chinese and for some reason this can't be changed.)
(Therefore, there might be chinese characters appear below.)

Show all the database:
homework04=# \l
                                                             数据库列表
        名称        |  拥有者  | 字元编码 |            校对规则            |             Ctype              |       存取权限
--------------------+----------+----------+--------------------------------+--------------------------------+-----------------------
 Consumer_Complaint | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |
 homework04         | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |
 postgres           | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 |
 template0          | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 | =c/postgres          +
                    |          |          |                                |                                | postgres=CTc/postgres
 template1          | postgres | UTF8     | Chinese (Simplified)_China.936 | Chinese (Simplified)_China.936 | =c/postgres          +
                    |          |          |                                |                                | postgres=CTc/postgres
(5 行记录)

Show all the table:
homework04=# \dt
                   关联列表
 架构模式 |      名称      |  类型  |  拥有者
----------+----------------+--------+----------
 public   | complaint_data | 数据表 | postgres
(1 行记录)

Describe table:
homework04=# \d complaint_data
                                          数据表 "public.complaint_data"
         栏位         |          类型          | Collation | Nullable |                  Default
----------------------+------------------------+-----------+----------+--------------------------------------------
 industry             | character varying(255) |           |          |
 complaint_type       | character varying(255) |           |          |
 mediation_start_date | character varying(255) |           |          |
 mediation_close_date | character varying(255) |           |          |
 complaint_result     | character varying(255) |           |          |
 satisfaction         | boolean                |           |          |
 business_city        | character varying(255) |           |          |
 business_state       | character varying(255) |           |          |
 id                   | integer                |           | not null | nextval('complaint_data_id_seq'::regclass)
索引：
    "complaint_data_pkey" PRIMARY KEY, btree (id)

# Query Results
```
### 1. number of rows
 exact_count
-------------
        4436
```

```
###2. first 15 rows with 3 columns
             industry              |           complaint_result            | business_city
-----------------------------------+---------------------------------------+---------------
 Travel Agency - 440               | Resolved and Consumer Satisfied - SPF | BROOKLYN
 Furniture Sales - 242             | Goods Received - GDR                  | BRONX
 Garage - 049                      | Cash Amount - AMT                     | NEW YORK
 Secondhand Dealer Auto - 005      | Goods Repaired - GRS                  | WYCLOFF
 Jewelry Store-Retail - 823        | Resolved and Consumer Satisfied - SPF | NEW YORK
 Laundry - 064                     | Resolved and Consumer Satisfied - SPF | FLUSHING
 Furniture Sales - 242             | Cash Amount - AMT                     | LIVERPOOL
 Home Improvement Contractor - 100 | Referred to Outside - RTO             | BROOKLYN
 Tow Truck Company - 124           | Cash Amount - AMT                     | BROOKLYN
 Jewelry Store-Retail - 823        | Advised to Sue - ATS                  | SCOTTSDALE
 Tow Truck Company - 124           | Cash Amount - AMT                     | STATEN ISLAND
 Tow Truck Company - 124           | Referred to Outside - RTO             | BROOKLYN
 Garage - 049                      | Advised to Sue - ATS                  | NEW YORK
 Supermarket - 819                 | Complaint Invalid - CIN               | AUSTIN
 Misc Non-Food Retail - 817        | No Business Response - NVR            | FRESH MEADOWS
```

```
###3. first 15 rows with 3 columns, sort by one column descending.
       industry        |                  complaint_result                  | business_city
-----------------------+----------------------------------------------------+---------------
 Wearing Apparel - 450 | Resolved and Consumer Satisfied - SPF              | EAST ELMHURST
 Wearing Apparel - 450 | Advised to Sue - ATS                               | BROOKLYN
 Wearing Apparel - 450 | Resolved and Consumer Satisfied - SPF              | NEW YORK
 Wearing Apparel - 450 | Advised to Sue - ATS                               | NEW YORK
 Wearing Apparel - 450 | Advised to Sue - ATS                               | GREAT NECK
 Wearing Apparel - 450 | No Satisfactory Agreement - NSA                    | BROOKLYN
 Wearing Apparel - 450 | Credit Card Refund and/or Contract Cancelled - CRC | STATEN ISLAND
 Wearing Apparel - 450 | Out of Business - OOB                              | JAMAICA
 Wearing Apparel - 450 | Advised to Sue - ATS                               | FOREST HILLS
 Wearing Apparel - 450 | Resolved and Consumer Satisfied - SPF              | NEW YORK
 Wearing Apparel - 450 | Referred to Outside - RTO                          | NEW YORK
 Wearing Apparel - 450 | Resolved and Consumer Satisfied - SPF              | NEW YORK
 Wearing Apparel - 450 | Cash Amount - AMT                                  | FOREST HILLS
 Wearing Apparel - 450 | Advised to Sue - ATS                               | NEW YORK
 Wearing Apparel - 450 | No Satisfactory Preempted - NSP                    | NEW YORK
```

```
###4. add a new column with no default value
ALTER TABLE
homework04=# select industry, new_col from complaint_data limit 5;
        industry        | new_col
------------------------+-----
 Dry Cleaners - 230     |
 Garage - 049           |
 Retail Store - 820     |
 Electronic Store - 001 |
 Garage - 049           |
```

```
###5. set value to this column
UPDATE 4436
homework04=# select new_col from complaint_data limit 5;
   new_col
-------------
 set values!
 set values!
 set values!
 set values!
 set values!
```

```
###6. show distinct value of a column
                     industry
--------------------------------------------------
 Travel Agency - 440
 Locksmith - 062
 Sightseeing Bus - 078
 Laundry - 064
 Pawnbroker - 080
 Gas Station-Retail - 815
 Other
 Electronic & Home Appliance Service Dealer - 115
 Misc Non-Food Retail - 817
 Dry Cleaners - 230
 Health Spa - 839
 Employment Agency - 034
 Fuel Oil Dealer - 814
 Home Improvement Contractor - 100
 Electronic Store - 001
 Mailorder Misc - 319
 Debt Settlement - 248
 Tax Preparers - 891
 Secondhand Dealer [General] - 006
 Car Wash
 Laundries
 Garage & Parking Lot - 098
 Photography Services - 415
 Horse Drawn Cab Driver - 086
 Tow Truck Driver - 125
 Ticket Seller Business
 Auctioneer - 036
 Tow Truck Company - 124
 Immigration Svc Prv - 893
 Funeral Homes - 888
 Garage - 049
 Auto Rental - 213
 Debt Collection Agency - 122
 Salons And Barbershop - 841
 Storage Warehouse - 120
 Laundry Jobber - 066
 Floor Coverings - 241
 Drug Store Retail - 810
 Mobile Food Vendor - 881
 Parking Lot - 050
 Auction House - 128
 Restaurant - 818
 Furniture Sales - 242
 Mini-Storage Company - 830
 Pedicab Driver - 131
 Hotel/Motel - 460
 Amusement Device (Portable) - 018
 Retail Store - 820
 Gift Certificate - 895
 Internet Complaints - 443
 Grocery-Retail - 808
 Hardware-Retail - 811
 Dealer In Products For The Disabled - 119
 Ticket Seller
 Booting Company - 126
 Supermarket - 819
 Tickets-Live Perf - 260
 Special Sale - 102
 Catering Establishment - 075
 Wearing Apparel - 450
 Appliances - 244
 Jewelry Store-Retail - 823
 Secondhand Dealer Auto - 005
```

```
###7. group rows together and calculate
                  complaint_result                  | count
----------------------------------------------------+-------
 Resolved and Consumer Satisfied - SPF              |   715
 No Satisfactory Agreement - NSA                    |   164
 Unable to Locate Business - ULV                    |   122
 Goods Exchanged - GEX                              |   117
 Referred to Outside - RTO                          |   339
 Consumer Withdrew Complaint - CWC                  |    22
 Referred to Hearing - RTH                          |   140
 Out of Business - OOB                              |    31
 Consumer Took Action - CTA                         |   103
 No Business Response - NVR                         |   119
 Credit Card Refund and/or Contract Cancelled - CRC |   147
 Unable to Locate Consumer - ULC                    |     3
 Referred to Manufacturer - RMF                     |    22
 No Consumer Response - NCR                         |   148
 Goods Received - GDR                               |    75
 Bill Reduced - BLR                                 |   199
 Complaint Invalid - CIN                            |   147
 Agency Collected Judgement - ACJ                   |     9
 Store Credit - SCR                                 |    99
 Goods Repaired - GRS                               |   105
 Advised to Sue - ATS                               |   725
 No Satisfactory Preempted - NSP                    |    50
 Cash Amount - AMT                                  |   835
```

```
###8. apply filter to grop query
           complaint_result            | count
---------------------------------------+-------
 Resolved and Consumer Satisfied - SPF |   715
 Referred to Outside - RTO             |   339
 Advised to Sue - ATS                  |   725
 Cash Amount - AMT                     |   835
```

```
###9. find numbers of satisfied complaint in NY area.
 satisfaction | count
--------------+-------
              |   765
 f            |  1167
 t            |  1794
```

```
###10. show first five states which receive most complaints. 
 business_state | count
----------------+-------
 NY             |  3726
 IL             |    70
 NJ             |    68
 GA             |    67
 TX             |    62
```

```
###11. find the least 10 complainted industry in NY state.
             industry              | count
-----------------------------------+-------
 Amusement Device (Portable) - 018 |     1
 Laundries                         |     1
 Mobile Food Vendor - 881          |     1
 Mini-Storage Company - 830        |     1
 Auctioneer - 036                  |     1
 Gift Certificate - 895            |     1
 Tow Truck Driver - 125            |     1
 Salons And Barbershop - 841       |     1
 Horse Drawn Cab Driver - 086      |     2
 Laundry Jobber - 066              |     2
```

```
###12. what are the first 5 complaint result in industry "Home Improvement Contractor - 100"
           complaint_result            | count
---------------------------------------+-------
 Advised to Sue - ATS                  |   215
 Referred to Hearing - RTH             |   103
 Resolved and Consumer Satisfied - SPF |    72
 Referred to Outside - RTO             |    64
 Cash Amount - AMT                     |    60
```