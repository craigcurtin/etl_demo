class Load(object):
    def __init__(self):
        pass

    def persist(self, target, data):
        data.to_csv(target)


def log(message):
    timestamp_format = '%H:%M:%S-%h-%d-%Y'
    # Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("dealership_logfile.txt", "a") as f: f.write(timestamp + ',' + message + 'n')
