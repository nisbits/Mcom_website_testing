from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework.decorators import api_view
from mcom_website.settings import MEDIA_ROOT
from rest_framework.response import Response

from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
from .models import *   
import datetime
# Create your views here.
import json
from .serializers import * 

def circle_list(objs):
    cir=[]
    
    for obj in objs:
        cir.append(obj.CIRCLE)

    cir_set=set(cir)
    cir=list(cir_set)
    return cir

@ api_view(["POST"])
def SoftAt_Report_Upload(request):
    Soft_At_upload_status.objects.all().delete()
    Soft_At_report_file = request.FILES["Soft_At_report_file"] if 'Soft_At_report_file' in request.FILES else None
    if Soft_At_report_file:
            location = MEDIA_ROOT + r"\Soft_AT\temporary_files"
            fs = FileSystemStorage(location=location)
            file = fs.save(Soft_At_report_file.name, Soft_At_report_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            filepath = fs.path(file)
            print("file_path:-",filepath)
            df=pd.read_excel(filepath) # should do something if a csv file is coming from the frontend and the csv file should be deleted from the temp files
            os.remove(path=filepath)
            print(filepath,"deleted........")
            print(df)

            for i, d in df.iterrows():
                # try:
                    # if pd.isnull(d["CIRCLE"]) or pd.isnull(d["UNQUI ID"]) or pd.isnull(d["SITE_ID"]) or pd.isnull(d["Circle Project"]) or pd.isnull(d["RFAI_DATE"]) or pd.isnull(["OA_(COMMERCIAL_TRAFFIC_PUT_ON_AIR)_(MS1)_DATE"]) or pd.isnull(d["Status"] or pd.isnull("Date")):

                    pk=str(d["CIRCLE"])+str(d["SITE_ID"])+str(d["BAND"])+str(d["OEM_NAME"])
                    if pd.isnull(d['Date']):
                           Date=None
                    else:
                           Date=(d["Date"])
                    try:
                        obj=Soft_At_Table.objects.create(id=pk,
                                                        CIRCLE=str(d["CIRCLE"]),
                                                        SITE_ID=str(d["SITE_ID"]),
                                                        UNQUI_ID=str(d["UNQUI ID"]),
                                                        ENODEB_ID=str(d["ENODEB_ID"]),
                                                        BAND=str(d["BAND"]),
                                                        Circle_Project=str(d["Circle Project"]),  
                                                        OEM_NAME=(d["OEM_NAME"]),
                                                        Pending_Bucket=str(d["Bucket"]),
                                                        Alarm_Bucket=str(d["Alarm Bucket"]),
                                                        Status=str(d["Status"]),
                                                        Date=Date, 
                                                        )
                        
                    except Exception as e:
                            print("error",e)
                            Soft_At_upload_status.objects.create(id=pk,Site_id=d["SITE_ID"],update_status="Not Uploaded",Remark="Site Already Present in DataBase")
                            continue 

            objs=Soft_At_upload_status.objects.all()
            serializers=ser_Soft_At_upload_status(objs,many=True)          


            return Response({"status": True,"message":"Report uploaded Successfully .","status_obj":serializers.data})
    else:
         return Response({"status": False,"message":"No report file Sent"})
def df_raw_column_total(data):
        print("_________________circle_wise_data_____________________________________")
        print(data)
        df=pd.DataFrame(data)
        df=df.T
        # add a sum row at the bottom of the dataframe
        df.loc['Total'] = df.sum()
        # add a sum column at the right end of the dataframe
        df['Total'] = df.sum(axis=1)
        json_data = df.to_json(orient='index') # here json_data  converts the dataframe to a string json
        json_data=json.loads(json_data) # json.loads - Which converts the string form of json data to a dictionary in python.
        print(df)
        return(json_data)
def df_raw_column_total_circle_wise(data):
        print("_________________circle_wise_data_____________________________________")
        print(data)
        df=pd.DataFrame(data)
        df=df.T
        print("---------------------------dataframe------------------------",df)
        # add a sum row at the bottom of the dataframe
        df.loc['Total'] = df.sum()
        # add a sum column at the right end of the dataframe
        df['Total'] = df["Accepted"] + df["Rejected"] +df["Dismantle"] + df["Pending"] + df["Need_to_be_offer"] +df["offered"]
        json_data = df.to_json(orient='index') # here json_data  converts the dataframe to a string json
        json_data=json.loads(json_data) # json.loads - Which converts the string form of json data to a dictionary in python.
        print(df)
        return(json_data)
     

@api_view(["GET","POST"])
def SoftAt_Circlewise_Dashboard(request):
       str_Date=request.POST.get("Date")
       month=request.POST.get("month")
       week=request.POST.get("week")
       year=request.POST.get("year")
       str_from_date=request.POST.get("from_date")
       str_to_date=request.POST.get("to_date")
    
       print("month:-----",month)
       print("date:-----",str_Date)
       print("week:---",week)
       print("year:---",year)
       print("str_from_date:---",str_from_date)
       print("str_to_date---",str_to_date)
       year=int(year)
       objs=Soft_At_Table.objects.all()
       circles= circle_list(objs)
       print("Circle_list: ",circles)
       data={}
       for circle in circles:
             
            obj=Soft_At_Table.objects.filter(CIRCLE=circle)
            if str_Date != "":
                print("___________Inside Date___________")
                Date=datetime.datetime.strptime(str_Date,"%Y-%m-%d").date()
                print(Date)
                Accepted=obj.filter(Status__iexact="Accepted", Date=Date).count()
                Dismantle=obj.filter(Status__iexact="Dismantle", Date=Date).count()
                offered=obj.filter(Status__iexact="offered", Date=Date).count()
                Rejected=obj.filter(Status__iexact="Rejected", Date=Date).count()
                Need_to_be_offer=obj.filter(Status__iexact="Need to be offer", Date=Date).count()
                Pending=obj.filter(Date=None).count()

            elif month != "":
                
                print("___________Inside Month___________")
                print(month)
                
                Accepted=obj.filter(Status__iexact="Accepted",Date__month=month,Date__year=year).count()
                Dismantle=obj.filter(Status__iexact="Dismantle",Date__month=month,Date__year=year).count()
                offered=obj.filter(Status__iexact="offered",Date__month=month,Date__year=year).count()
                Rejected=obj.filter(Status__iexact="Rejected",Date__month=month,Date__year=year).count()
                Need_to_be_offer=obj.filter(Status__iexact="Need to be offer", Date__month=month,Date__year=year).count()
                Pending=obj.filter(Date=None).count()

            elif week != "":
                
                print("___________Inside week___________")
                week=int(week)
                
                Accepted=obj.filter(Status__iexact="Accepted",Date__week=week,Date__year=year).count()
                Dismantle=obj.filter(Status__iexact="Dismantle",Date__week=week,Date__year=year).count()
                offered=obj.filter(Status__iexact="offered",Date__week=week,Date__year=year).count()
                Rejected=obj.filter(Status__iexact="Rejected",Date__week=week,Date__year=year).count()
                Need_to_be_offer=obj.filter(Status__iexact="Need to be offer", Date__week=week,Date__year=year).count()
                Pending=obj.filter(Date=None).count()

            elif str_from_date != "" and str_to_date != "":
                
                print("___________Inside from and to ___________")
                from_date=datetime.datetime.strptime(str_from_date,"%Y-%m-%d").date()
                to_date=datetime.datetime.strptime(str_to_date,"%Y-%m-%d").date()
                print("from_date",from_date)
                print("to_date",to_date)

                
                
                Accepted=obj.filter(Status__iexact="Accepted",Date__range=(from_date,to_date)).count()
                Dismantle=obj.filter(Status__iexact="Dismantle",Date__range=(from_date,to_date)).count()
                offered=obj.filter(Status__iexact="offered",Date__range=(from_date,to_date)).count()
                Rejected=obj.filter(Status__iexact="Rejected",Date__range=(from_date,to_date)).count()
                Need_to_be_offer=obj.filter(Status__iexact="Need to be offer", Date__range=(from_date,to_date)).count()
                Pending=obj.filter(Date=None).count()
                  

            else:
                print("_________________Inside All_______________")
                Accepted=obj.filter(Status__iexact="Accepted").count()
                Dismantle=obj.filter(Status__iexact="Dismantle").count()
                offered=obj.filter(Status__iexact="offered").count()
                Rejected=obj.filter(Status__iexact="Rejected").count()
                Need_to_be_offer=obj.filter(Status__iexact="Need to be offer").count()
                Pending=obj.filter(Date=None).count()
            total=Accepted + Dismantle + offered + Rejected + Need_to_be_offer + Pending
            print(circle,total)
            if total != 0:
                Acceptance_percent=round(Accepted/total,2)
                Rejection_percent=round(Rejected/total,2)
            else:
                Acceptance_percent=0
                Rejection_percent=0
            data[circle]={"Accepted":Accepted,"Dismantle":Dismantle,"offered":offered,"Rejected":Rejected,"Pending":Pending,"Need_to_be_offer":Need_to_be_offer,"Accepted_per":Acceptance_percent,"Rejection_per":Rejection_percent}
       if len(data)!=0:
           data1=df_raw_column_total_circle_wise(data)
       else:
            return Response({"status":False,"message":"Database is empty"})
    
       ################### code for pending sites bucketization ###################
       
       Accepted_Eric_pending=objs.filter(Status="Pending", Pending_Bucket="Accepted(Eric pending)").count()
       Accepted_HW_Rejected=objs.filter(Status="Pending", Pending_Bucket = "Accepted(HW Rejected)").count()
       Circle_Team=objs.filter(Status="Pending", Pending_Bucket = "Circle Team").count()
       Circle_Team_NOC_Team=objs.filter(Status="Pending", Pending_Bucket = "Circle Team /NOC Team").count()
       circle_Team_Media_team=objs.filter(Status="Pending", Pending_Bucket = "Circle Team/Media team").count()
       Need_to_check=objs.filter(Status="Pending", Pending_Bucket = "Need to check").count()
       NOC_Team=objs.filter(Status="Pending", Pending_Bucket = "NOC Team").count()
       pending_sites_bucketization={}
       pending_sites_bucketization["Pending"]={
                                    "Accepted_Eric_pending":Accepted_Eric_pending,
                                    "Accepte_HW_Rejected":Accepted_HW_Rejected,
                                    "Circle_Team":Circle_Team,
                                    "Circle_Team_NOC_Team":Circle_Team_NOC_Team,
                                    "circle_Team_Media_team":circle_Team_Media_team,
                                    "Need_to_check":Need_to_check,
                                    "NOC_Team":NOC_Team,
                                    }
       pending_sites_bucketization=df_raw_column_total(pending_sites_bucketization)

       ################## Alarm_Bucket Code #########################
       Accepted_Eric_pending=0
       Accepted_HW_Rejected=0
       
       
       Accepted_Eric_pending=objs.filter(Alarm_Bucket="Accepted(Eric pending)").count()
       Accepted_HW_Rejected=objs.filter(Alarm_Bucket="Accepted(HW Rejected)").count()
       Configuration_issue=objs.filter(Alarm_Bucket="Configuration issue").count()
       GTPU_Trxmn_S1_Link_Alarm=objs.filter(Alarm_Bucket="GTPU/Trxmn/S1 Link Alarm").count()
       HW_Alarms=objs.filter(Alarm_Bucket="HW Alarms").count()
       Incomplete_AT_details_OSS_data=objs.filter(Alarm_Bucket="Incomplete AT details(OSS data)").count()
       License_Capacity_Software_Issue=objs.filter(Alarm_Bucket="License Capacity/Software Issue").count()
       Service_affec=objs.filter(Alarm_Bucket="Service affec").count()
       Service_affecting_alarm=objs.filter(Alarm_Bucket="Service affecting alarm").count()
       Sites_Locked_Down_Ping_Not_OK_Upload_Failed_Login_Failed=objs.filter(Alarm_Bucket="Sites Locked/Down/Ping Not OK/Upload Failed/Login Failed").count()
       Sync_Issue_GPS_TOP=objs.filter(Alarm_Bucket="Sync Issue - GPS/TOP").count()
       TWAMP_Issue=objs.filter(Alarm_Bucket="TWAMP Issue").count()
       VSWR_High_Config_Issue=objs.filter(Alarm_Bucket="VSWR High/Config Issue").count()
       
       total=Accepted_Eric_pending + Accepted_HW_Rejected + Configuration_issue + GTPU_Trxmn_S1_Link_Alarm + GTPU_Trxmn_S1_Link_Alarm + HW_Alarms +Incomplete_AT_details_OSS_data + License_Capacity_Software_Issue + Service_affec + Service_affecting_alarm + Sites_Locked_Down_Ping_Not_OK_Upload_Failed_Login_Failed + Sync_Issue_GPS_TOP + TWAMP_Issue +VSWR_High_Config_Issue
       alarm_bucketization={}
       alarm_bucketization["Accepted(Eric pending)"]={"Count_of_Alarm_Bucket":Accepted_Eric_pending}
       alarm_bucketization["Accepted(HW Rejected)"]={"Count_of_Alarm_Bucket":Accepted_HW_Rejected}
       alarm_bucketization["Configuration issue"]={"Count_of_Alarm_Bucket":Configuration_issue}
       alarm_bucketization["GTPU/Trxmn/S1 Link Alarm"]={"Count_of_Alarm_Bucket":GTPU_Trxmn_S1_Link_Alarm}
       alarm_bucketization["HW Alarms"]={"Count_of_Alarm_Bucket":HW_Alarms}
       alarm_bucketization["Incomplete AT details(OSS data)"]={"Count_of_Alarm_Bucket":Incomplete_AT_details_OSS_data}
       alarm_bucketization["License Capacity/Software Issue"]={"Count_of_Alarm_Bucket":License_Capacity_Software_Issue}
       alarm_bucketization["Service affec"]={"Count_of_Alarm_Bucket":Service_affec}
       alarm_bucketization["Service affecting alarm"]={"Count_of_Alarm_Bucket":Service_affecting_alarm}
       alarm_bucketization["Sites Locked/Down/Ping Not OK/Upload Failed/Login Failed"]={"Count_of_Alarm_Bucket":Sites_Locked_Down_Ping_Not_OK_Upload_Failed_Login_Failed}
       alarm_bucketization["Sync Issue - GPS/TOP"]={"Count_of_Alarm_Bucket":Sync_Issue_GPS_TOP}
       alarm_bucketization["TWAMP Issue"]={"Count_of_Alarm_Bucket":TWAMP_Issue}
       alarm_bucketization["VSWR High/Config Issue"]={"Count_of_Alarm_Bucket":VSWR_High_Config_Issue}
       alarm_bucketization["Grand Total"]={"Count_of_Alarm_Bucket":total}


       
       return Response({"status":True, 
                        "Data":data1,
                        "pending_sites_bucketization":pending_sites_bucketization,
                        "alarm_bucketization":alarm_bucketization})

       
       
       
       
    