

log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract() 
log("Extract phase Ended")

log("Transform phase Ended")

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")

log("ETL Job Ended")

:wq

