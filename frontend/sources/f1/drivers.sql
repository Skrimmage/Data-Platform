select 
    CONCAT(forename, ' ', surname) as name,
    dob,
    nationality,
    url,
    driverRef,
    './' || driverRef as driver_link
from 'sources/drivers.csv'
