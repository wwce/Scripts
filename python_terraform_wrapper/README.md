
  # Purpose:
  A python script that will wrap terraform so that we can deploy mulitiple tf files and configure VM Series firewalls where     required.

  # Usage: 
  
  python deploy.py <fwusername> <fwpassword> 
  fwusername = Fw login username
  fwpassword = Fw login password
  

  # Outputs:
  Outputs to file deployment_status
  Contents of json dict
  {"WebInDeploy": "Success", "WebInFWConf": "Success", "waf_conf": "Success"}
