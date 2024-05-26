from flask import session,request
import insert

def before_request(app):
   @app.before_request
   def before():
       if "name" in session:
           if "logsid" in session:
               logsid=session["logsid"]
               insert.updatelogs(logsid)
           plc = insert.insertlogs(request, session["id"])
           session["logsid"]=plc[0]
           print(plc[0],"hellop")
           print(request.cookies["session"])
           print(session["name"])
