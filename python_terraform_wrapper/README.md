
  # Purpose:
  A python script that will wrap terraform so that we can deploy mulitiple tf files and configure VM Series firewalls where     required.

  # Usage: 
  
  python deploy.py fwusername fwpassword<br/>   
  fwusername = Fw login username<br/> 
  fwpassword = Fw login password<br/> 
  

  # Outputs:
  Outputs to file deployment_status<br/> 
  Contents of json dict<br/> 
  {"WebInDeploy": "Success", "WebInFWConf": "Success", "waf_conf": "Success"}
