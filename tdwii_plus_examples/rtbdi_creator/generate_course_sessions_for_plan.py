#! /usr/bin/env python

from datetime import datetime, timedelta
from sys import argv


from rtbdi_factory import gen_one_session, load_plan

if __name__ == "__main__":
    plan_path = argv[1]
    retrieve_ae_title = argv[2]
    plan_ds = load_plan(plan_path)
    planned_fractions = plan_ds.FractionGroupSequence[0].NumberOfFractionsPlanned
    start_date = datetime.now()
    date = start_date

    for i in range(planned_fractions):
        gen_one_session(plan_ds, i + 1, date, retrieve_ae_title)
        date += timedelta(days=1)
