# Import Hesiod libraries
from hesiod import lib_general as libgen
from hesiod import lib_json as libjson
from hesiod import lib_logs_and_headers as liblog 
from hesiod import lib_paramiko as libpko 

# Import Schema libraries
from lib import md as libmd

# Import Standard Python libraries
import os
import sys

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

# Import json configuration parameters
env_json_str = libjson.populate_var_from_json_file("json", "lab_environment.json")
env_json_py = libjson.load_json_variable(env_json_str)
this_script_name = os.path.basename(__file__)
logfile_name = env_json_py["logs"][this_script_name]

# Hesiod Header and Log init
liblog.hesiod_print_header()
liblog.hesiod_log_header(logfile_name)
err = "Successfully imported Hesiod python libraries."
liblog.write_to_logs(err, logfile_name)
err = "Succesfully initialized logs to "+logfile_name
liblog.write_to_logs(err, logfile_name)
err = ""
liblog.write_to_logs(err, logfile_name)

# Main functions
def _main_():
    print("Running hesiod-schema.py...")
    print("No arguments found. Defaulting to help menu. ")
    print("")
    help_stdout()
    err = "    Exiting script."
    liblog.write_to_logs(err, logfile_name)
    sys.exit() 

def help_stdout():
    print("HELP MENU: hesiod-schema.py [options]")
    print("Enter options 1x per run, do not add all parameters at once!")
    print("--help option to see this menu.")
    print("-o365    option to convert a word or excel document into Markdown.")
    print("")
    print("")

def match_help(args):
    if '--help' in args:
        return True

def match_o365(args):
    if '-o365' in args:
        return True
def match_json(args):
    if '-json' in args:
        return True
    
# Get args
err = "Getting args..."
liblog.write_to_logs(err, logfile_name)
arg_len = len(sys.argv) 
err = "    "+str(arg_len)+" args passed."
liblog.write_to_logs(err, logfile_name)

# Initialize default user options
user_options = ['n', 'n', 'n']

# Match args
match_found = False 
match_found = match_help(sys.argv)
if match_found :
    err = "    --help found. Initiating standard output."
    liblog.write_to_logs(err, logfile_name)
    help_stdout()
    err = "    Exiting script."
    liblog.write_to_logs(err, logfile_name)
    sys.exit() 

else:
  match_found = False 
  match_found = match_o365(sys.argv)
  if match_found :
      err = "    -o365 found. Converting O365 document to Markdown."
      liblog.write_to_logs(err, logfile_name)
      err = "    o365 file: "+env_json_py["drop_location"]+sys.argv[2]
      liblog.write_to_logs(err, logfile_name)
      err = "    markdown file: "+sys.argv[3]
      liblog.write_to_logs(err, logfile_name)
      markdowncontent = libmd.convert_o365_2_md(env_json_py["drop_location"]+sys.argv[2])
      libgen.append_text_to_file(markdowncontent, sys.argv[3])
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

  match_found = False 
  match_found = match_json(sys.argv)
  if match_found :
      err = "    -json found. Converting Markdown file to json."
      liblog.write_to_logs(err, logfile_name)
      err = "    markdown file: "+env_json_py["drop_location"]+sys.argv[2]
      liblog.write_to_logs(err, logfile_name)
      err = "    json file: "+sys.argv[3]
      liblog.write_to_logs(err, logfile_name)
      markdowncontent = libgen.populate_var_from_file(env_json_py["drop_location"]+sys.argv[2])
      md_json_str = libmd.convert_md_2_json(markdowncontent)
      #libgen.populate_file_from_var(sys.argv[3], md_json_str)
      md_json_py = libjson.load_json_variable(md_json_str)
      libjson.dump_json_to_file(md_json_py, sys.argv[3])
      err = "    Exiting script."
      liblog.write_to_logs(err, logfile_name)
      sys.exit() 

err = "No arguments found. Instantiating _main_()"
liblog.write_to_logs(err, logfile_name)
_main_()