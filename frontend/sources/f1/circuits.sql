select 
    circuitId,
    circuitRef,
    name,
    location,
    country,
    lat,
    lng,
    alt,
    url,
    './' || circuitRef as circuit_link
from 'sources/circuits.csv'
