import argparse
import mysql.connector
import datetime

def wtBase(factor):
	now = (datetime.datetime.now() + datetime.timedelta(hours=2)).time()

def main():
	# create the top-level parser
	parser = argparse.ArgumentParser(description='doc4tune shell')
	subparsers = parser.add_subparsers(help='sub-command help', dest='command')

	setwt_parser = subparsers.add_parser('set-wt', help='Set waiting times')
	setwt_parser.add_argument('id', type=str, help='ID (private_id)')
	setwt_parser.add_argument('waiting_time', type=int, help='Waiting time in minutes')

	upwt_parser = subparsers.add_parser('update-wt', help='Update waiting times')

	args = parser.parse_args()

	mydb = mysql.connector.connect(
		host="localhost",
		user="script_worker",
		passwd="letmein", # yes, this is just horrible
		database="bitnami_wordpress",
	)

	if args.command == 'set-wt':
		mycursor = mydb.cursor()
		sql = "UPDATE wp_participants_database SET waiting_time = %s WHERE private_id = %s"
		val = (args.waiting_time, args.id)
		mycursor.execute(sql, val)
		mydb.commit()
		print("Done!")

	if args.command == 'update-wt':
		mycursor = mydb.cursor()
		sql = "UPDATE wp_participants_database SET waiting_time = FLOOR(RAND()*(25-4+1))+4"
		mycursor.execute(sql)
		mydb.commit()
		print("Done!")


if __name__ == "__main__":
	main()
