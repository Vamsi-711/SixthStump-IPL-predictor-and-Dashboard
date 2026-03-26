import json
from datetime import datetime
import os
import re

raw_data = """1 28-MAR-26 Sat 7:30 PM RCB SRH Bengaluru
2 29-MAR-26 Sun 7:30 PM MI KKR Mumbai
3 30-MAR-26 Mon 7:30 PM RR CSK Guwahati
4 31-MAR-26 Tue 7:30 PM PBKS GT New Chandigarh
5 01-APR-26 Wed 7:30 PM LSG DC Lucknow
6 02-APR-26 Thu 7:30 PM KKR SRH Kolkata
7 03-APR-26 Fri 7:30 PM CSK PBKS Chennai
8 04-APR-26 Sat 3:30 PM DC MI Delhi
9 04-APR-26 Sat 7:30 PM GT RR Ahmedabad
10 05-APR-26 Sun 3:30 PM SRH LSG Hyderabad
11 05-APR-26 Sun 7:30 PM RCB CSK Bengaluru
12 06-APR-26 Mon 7:30 PM KKR PBKS Kolkata
13 07-APR-26 Tue 7:30 PM RR MI Guwahati
14 08-APR-26 Wed 7:30 PM DC GT Delhi
15 09-APR-26 Thu 7:30 PM KKR LSG Kolkata
16 10-APR-26 Fri 7:30 PM RR RCB Guwahati
17 11-APR-26 Sat 3:30 PM PBKS SRH New Chandigarh
18 11-APR-26 Sat 7:30 PM CSK DC Chennai
19 12-APR-26 Sun 3:30 PM LSG GT Lucknow
20 12-APR-26 Sun 7:30 PM MI RCB Mumbai
21 13-APR-26 Mon 7:30 PM SRH RR Hyderabad
22 14-APR-26 Tue 7:30 PM CSK KKR Chennai
23 15-APR-26 Wed 7:30 PM RCB LSG Bengaluru
24 16-APR-26 Thu 7:30 PM MI PBKS Mumbai
25 17-APR-26 Fri 7:30 PM GT KKR Ahmedabad
26 18-APR-26 Sat 3:30 PM RCB DC Bengaluru
27 18-APR-26 Sat 7:30 PM SRH CSK Hyderabad
28 19-APR-26 Sun 3:30 PM KKR RR Kolkata
29 19-APR-26 Sun 7:30 PM PBKS LSG New Chandigarh
30 20-APR-26 Mon 7:30 PM GT MI Ahmedabad
31 21-APR-26 Tue 7:30 PM SRH DC Hyderabad
32 22-APR-26 Wed 7:30 PM LSG RR Lucknow
33 23-APR-26 Thu 7:30 PM MI CSK Mumbai
34 24-APR-26 Fri 7:30 PM RCB GT Bengaluru
35 25-APR-26 Sat 3:30 PM DC PBKS Delhi
36 25-APR-26 Sat 7:30 PM RR SRH Jaipur
37 26-APR-26 Sun 3:30 PM GT CSK Ahmedabad
38 26-APR-26 Sun 7:30 PM LSG KKR Lucknow
39 27-APR-26 Mon 7:30 PM DC RCB Delhi
40 28-APR-26 Tue 7:30 PM PBKS RR New Chandigarh
41 29-APR-26 Wed 7:30 PM MI SRH Mumbai
42 30-APR-26 Thu 7:30 PM GT RCB Ahmedabad
43 01-MAY-26 Fri 7:30 PM RR DC Jaipur
44 02-MAY-26 Sat 7:30 PM CSK MI Chennai
45 03-MAY-26 Sun 3:30 PM SRH KKR Hyderabad
46 03-MAY-26 Sun 7:30 PM GT PBKS Ahmedabad
47 04-MAY-26 Mon 7:30 PM MI LSG Mumbai
48 05-MAY-26 Tue 7:30 PM DC CSK Delhi
49 06-MAY-26 Wed 7:30 PM SRH PBKS Hyderabad
50 07-MAY-26 Thu 7:30 PM LSG RCB Lucknow
51 08-MAY-26 Fri 7:30 PM DC KKR Delhi
52 09-MAY-26 Sat 7:30 PM RR GT Jaipur
53 10-MAY-26 Sun 3:30 PM CSK LSG Chennai
54 10-MAY-26 Sun 7:30 PM RCB MI Raipur
55 11-MAY-26 Mon 7:30 PM PBKS DC Dharamshala
56 12-MAY-26 Tue 7:30 PM GT SRH Ahmedabad
57 13-MAY-26 Wed 7:30 PM RCB KKR Raipur
58 14-MAY-26 Thu 7:30 PM PBKS MI Dharamshala
59 15-MAY-26 Fri 7:30 PM LSG CSK Lucknow
60 16-MAY-26 Sat 7:30 PM KKR GT Kolkata
61 17-MAY-26 Sun 3:30 PM PBKS RCB Dharamshala
62 17-MAY-26 Sun 7:30 PM DC RR Delhi
63 18-MAY-26 Mon 7:30 PM CSK SRH Chennai
64 19-MAY-26 Tue 7:30 PM RR LSG Jaipur
65 20-MAY-26 Wed 7:30 PM KKR MI Kolkata
66 21-MAY-26 Thu 7:30 PM CSK GT Chennai
67 22-MAY-26 Fri 7:30 PM SRH RCB Hyderabad
68 23-MAY-26 Sat 7:30 PM LSG PBKS Lucknow
69 24-MAY-26 Sun 3:30 PM MI RR Mumbai
70 24-MAY-26 Sun 7:30 PM KKR DC Kolkata"""

vmap = {
    "Bengaluru": "M. Chinnaswamy Stadium",
    "Mumbai": "Wankhede Stadium",
    "Guwahati": "Barsapara Cricket Stadium",
    "New Chandigarh": "PCA Stadium",
    "Lucknow": "BRSABV Ekana Stadium",
    "Kolkata": "Eden Gardens",
    "Chennai": "MA Chidambaram Stadium",
    "Delhi": "Arun Jaitley Stadium",
    "Ahmedabad": "Narendra Modi Stadium",
    "Hyderabad": "Rajiv Gandhi Intl. Stadium",
    "Jaipur": "Sawai Mansingh Stadium",
    "Raipur": "Shaheed Veer Narayan Singh Intl. Stadium",
    "Dharamshala": "HPCA Stadium"
}

match_dates = []
schedule = []

import re
lines = raw_data.strip().splitlines()

for line in lines:
    parts = line.split()
    if len(parts) < 8:
        # handle new chandigarh properly
        m = re.match(r'^(\d+)\s+(\d{2}-[A-Z]{3}-\d{2})\s+([A-Z][a-z]{2})\s+(\d[^\s]+ PM)\s+([A-Z]+)\s+([A-Z]+)\s+(.+)$', line)
        if m:
            num, datestr, day, timestr, t1, t2, citystr = m.groups()
        else:
            continue
    else:
        num = parts[0]
        datestr = parts[1]
        day = parts[2]
        timestr = parts[3] + " " + parts[4]
        t1 = parts[5]
        t2 = parts[6]
        citystr = " ".join(parts[7:])
        
    num = int(num)
    city = citystr.strip()
    
    dt_str = f"{datestr} {timestr}"
    dt_obj = datetime.strptime(dt_str, "%d-%b-%y %I:%M %p")
    iso_dt = dt_obj.strftime("%Y-%m-%dT%H:%M:00+05:30")
    
    match_dates.append(f'            {{ n: {num}, dt: "{iso_dt}", t1: "{t1}", t2: "{t2}" }},')
    
    disp_date = f"{day} {dt_obj.strftime('%d %b')}"
    
    venue = vmap.get(city, city)
    
    schedule.append(f'            {{ n: {num}, date: "{disp_date}", time: "{timestr}", t1: "{t1}", t2: "{t2}", venue: "{venue}", city: "{city}" }},')

with open("e:/VS CODE/SixthStump/temp_schedule_out.txt", "w") as f:
    f.write("const MATCH_DATES = [\n")
    f.write("\n".join(match_dates))
    f.write("\n        ];\n")
    
    f.write("------------\n")
    
    f.write("const SCHEDULE = [\n")
    f.write("\n".join(schedule))
    f.write("\n        ];\n")

print("Done")
