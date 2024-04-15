from datetime import datetime, time

import numpy
import pandas as pd
from django.core.management.base import BaseCommand

from ...models import Report  # Adjust this import based on your project structure


class Command(BaseCommand):
    help = "Upload data from Excel to database"

    def handle(self, *args, **options):
        # Read the Excel file
        df = pd.read_excel("static/docs/data.xlsx", engine="openpyxl")
        df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]])
        # # Iterate over the rows in the DataFrame
        for index, row in df.iterrows():
            # Create a new Report object for each row
            hour = row["hr"]
            time_str = f"{hour}::00"

            # print(type(hour), hour)
            time_object = datetime.strptime(time_str, "%H::%M").time()
            # print(time_object, type(time_object))
            # report_time = datetime.strptime(str(hour), "0")
            date_str = row["Date"].strftime("%Y-%m-%d")
            # print(date_str, type(date_str))
            report = Report(
                st=row["st"],
                date=date_str,
                time=time_object,
                vis=row["vis"],
                t_cld=row["t cld"],
                dd=row["dd"],
                fff=row["fff"],
                temp=row["temp"],
                dp=row["dp"],
                vp=round(row["vp"], 1),
                rh=row["rh"],
                msl=row["msl"],
                qnh=row["qnh"],
                w=row["w"],
                ww=row["ww"],
                t_lcld=row["t lcld"],
                cld=row["cld"],
                low=row["low"],
                mid=row["mid"],
                high=row["high"],
                high2=row["high2"],
                maxx=row["max"],
                minn=row["min"],
                rr=row["rr"],
                # rr_time=row['rr time'],
            )

            # Save the Report object to the database
            report.save()
            # print(report.vp)
            self.stdout.write(self.style.SUCCESS(f'Successfully added report {report}'))

        self.stdout.write(self.style.SUCCESS(report))
