select 
    CONCAT(forename, ' ', surname) as name,
    driverId,
    dob,
    nationality,
    url,
    driverRef,
    './' || driverRef as driver_link
from 'sources/drivers.csv'
