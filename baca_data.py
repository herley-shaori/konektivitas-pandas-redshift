import pandas_redshift as pr

pr.connect_to_redshift(dbname = 'basis-data-satu',
                        host = 'redshiftdb-sfklwkncbbps.c740qungtmbm.ap-southeast-1.redshift.amazonaws.com',
                        port = 5439,
                        user = 'herley',
                        password = 'Katasandiyangsangatrahasia890123')

df = pr.redshift_to_pandas('select * from tabel_satu')
print(df)