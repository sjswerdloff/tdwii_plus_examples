RT Beams Delivery Instruction and UPS Creator

PySide6 GUI and/or command line driven tool to automate construction of fraction/session specific
files for use in the IHE-RO TDW-II profile.

Command Line Interface:

generate_course_sessions_for_plan.py plan_filename cmove_AE_TITLE

will generate an entire course worth of RT Beams Delivery Instructions and Unified Procedure Steps, based on the number of fractions specified in the plan, with the start datetime being "now", with one fraction scheduled per day.
Example:
You are using OpenTPS to generate RT Ion Plans, are saving your plans in a subdirectory of your home directory in OpenTPS/Plans and saved a plan in a file named my_plan.dcm and you are using the pynetdicom sample application qrscp as the Object Store:

generate_course_sessions_for_plan.py ~/OpenTPS/Plans/my_plan.dcm QRSCP


GUI:

mainbdiwidget.py

After generating the RT BDI and UPS, you will want to C-STORE the RT BDI object(s) to QRSCP (e.g. using the pynetdicom sample application storescu) and then use ncreatescu.py to have the UPS(s) created in the UPSSCP
