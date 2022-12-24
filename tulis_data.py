import pandas_redshift as pr
import pandas as pd
import random
from faker import Faker

fake = Faker()
def create_rows(num=1):
    output = [{"name":fake.name(),
                "address":fake.address(),
                "name":fake.name(),
                "email":fake.email(),
                "bs":fake.bs(),
                "address":fake.address(),
                "city":fake.city(),
                "state":fake.state(),
                "date_time":fake.date_time(),
                "paragraph":fake.paragraph(),
                "phrase":fake.catch_phrase(),
                "randomdata":random.randint(1000,2000)} for x in range(num)]
    return output

pr.connect_to_redshift(dbname = 'basis-data-satu',
                        host = 'redshiftdb-sfklwkncbbps.c740qungtmbm.ap-southeast-1.redshift.amazonaws.com',
                        port = 5439,
                        user = 'herley',
                        password = 'Katasandiyangsangatrahasia890123')

pr.connect_to_s3(aws_access_key_id = <>,
                aws_secret_access_key = <>,
                bucket = 'bucket-untuk-pandas-redshift',
                subdirectory = ''
                )

df = pd.DataFrame(create_rows(5000))
pr.pandas_to_redshift(data_frame = df, redshift_table_name = 'public.tabel_satu')