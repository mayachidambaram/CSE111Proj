select F.f_filekey, F.f_title, F.f_author
from Files F
where F.f_publisherkey = (
    select P.p_publisherkey 
    From Publisher P
    Where P.p_publishername = 'HarperCollins'
)
-- Displays books published by a specific publisher
