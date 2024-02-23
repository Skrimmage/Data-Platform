select 
    CONCAT(forename, ' ', surname) as name,
    driverId,
    dob,
    nationality,
    url,
    driverRef,
    './' || driverRef as driver_link
from f1.drivers