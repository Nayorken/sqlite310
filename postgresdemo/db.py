import psycopg2

#conectar a base de dados
con = psycopg2.connect(
        host="ec2-176-34-184-174.eu-west-1.compute.amazonaws.com",
        database="d4pa4trltbaaj7",
        user="kbioomkzsmgqrc",
        password="8394a132394b6def605325677449fba72d73ba826f3a545aa359d60650b73402")

#cursor
cur = con.cursor()


#fechar a conecção
con.close()
