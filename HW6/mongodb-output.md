## 1 find all retired scooters limit to 10 records
{{{>  db.scooters.find({"retired": false}).limit(10)
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9e"), "acquire_date" : "2014-07-07", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9f"), "acquire_date" : "2018-06-26", "retired" : false, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda2"), "acquire_date" : "2015-12-19", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda3"), "acquire_date" : "2017-11-06", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda5"), "acquire_date" : "2015-08-09", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda8"), "acquire_date" : "2015-05-24", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda9"), "acquire_date" : "2015-08-17", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdaa"), "acquire_date" : "2018-03-23", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdac"), "acquire_date" : "2017-03-24", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdad"), "acquire_date" : "2017-05-17", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }}}}

## 2 show the acquire_date, scooter_type and max_speed properties of first 10 scooter records
{{{> db.scooters.find({}, {"acquire_date": 1, "scooter_type": 1, "max_speed": 1}).limit(10)
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9e"), "acquire_date" : "2014-07-07", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9f"), "acquire_date" : "2018-06-26", "scooter_type" : "Scoot V2", "max_speed" : 40 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda0"), "acquire_date" : "2015-11-25", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda1"), "acquire_date" : "2015-12-21", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda2"), "acquire_date" : "2015-12-19", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda3"), "acquire_date" : "2017-11-06", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda4"), "acquire_date" : "2017-09-28", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda5"), "acquire_date" : "2015-08-09", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda6"), "acquire_date" : "2015-01-09", "scooter_type" : "SuperStar v1", "max_speed" : 35 }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda7"), "acquire_date" : "2015-12-12", "scooter_type" : "SuperStar v1", "max_speed" : 35 }}}}

## 3 find all the scooters which is produced by Not Slow Co and is retired and shows a subset of all properties and ensure that _id is not shown limit to 10 records
{{{> db.scooters.find({"retired": true, "manufacturer": "Not Slow Co"}, {_id:0}).limit(10)
{ "acquire_date" : "2015-11-25", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2015-12-21", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2017-09-28", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2015-01-09", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2015-12-12", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2015-09-07", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2014-05-28", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 25, "weight" : 15, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2017-12-03", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2018-06-21", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "acquire_date" : "2017-04-19", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }}}}

## 4 find scooters with max_speed larger than 35 limit to 10 records
{{{> db.scooters.find({"max_speed": {$gt: 35}}).limit(10)
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9f"), "acquire_date" : "2018-06-26", "retired" : false, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb0"), "acquire_date" : "2017-12-03", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb1"), "acquire_date" : "2018-06-21", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb2"), "acquire_date" : "2017-04-19", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb3"), "acquire_date" : "2015-08-10", "retired" : false, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb4"), "acquire_date" : "2016-06-20", "retired" : true, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abdb5"), "acquire_date" : "2017-10-11", "retired" : false, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }}}}

## 5 find first 10 scooters which has weight greater than 25 or max_speed greater or equal to 40
{{{> db.scooters.find( { $or: [ { "weight": { $gt: 25 } }, { "max_speed": {$gte: 40} } ] } ).limit(10)
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9e"), "acquire_date" : "2014-07-07", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abd9f"), "acquire_date" : "2018-06-26", "retired" : false, "scooter_type" : "Scoot V2", "max_speed" : 40, "weight" : 20, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda0"), "acquire_date" : "2015-11-25", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda1"), "acquire_date" : "2015-12-21", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda2"), "acquire_date" : "2015-12-19", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda3"), "acquire_date" : "2017-11-06", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda4"), "acquire_date" : "2017-09-28", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda5"), "acquire_date" : "2015-08-09", "retired" : false, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda6"), "acquire_date" : "2015-01-09", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }
{ "_id" : ObjectId("5c0b31ce2a2ad8e46d1abda7"), "acquire_date" : "2015-12-12", "retired" : true, "scooter_type" : "SuperStar v1", "max_speed" : 35, "weight" : 30, "manufacturer" : "Not Slow Co", "website" : "notslow.lol" }}}}

