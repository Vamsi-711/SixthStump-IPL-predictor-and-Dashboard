import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_points = """        const POINTS_TABLE_2026 = [
            { team: "RR", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+4.171" },
            { team: "RCB", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+2.907" },
            { team: "DC", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+1.397" },
            { team: "MI", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+0.687" },
            { team: "PBKS", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+0.509" },
            { team: "SRH", m: 2, w: 1, l: 1, nr: 0, pts: 2, nrr: "+0.469" },
            { team: "GT", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-0.509" },
            { team: "LSG", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-1.397" },
            { team: "KKR", m: 2, w: 0, l: 2, nr: 0, pts: 0, nrr: "-1.964" },
            { team: "CSK", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-4.171" }
        ];"""

new_istat = """        const ISTAT2026 = {
            orange: [{ n: "Angkrish Raghuvanshi", t: "KKR", v: 103, s: "runs" }, { n: "Ishan Kishan", t: "SRH", v: 94, s: "runs" }, { n: "Heinrich Klaasen", t: "SRH", v: 83, s: "runs" }, { n: "Ryan Rickelton", t: "MI", v: 81, s: "runs" }, { n: "Rohit Sharma", t: "MI", v: 78, s: "runs" }],
            purple: [{ n: "Jaydev Unadkat", t: "SRH", v: 4, s: "wkts" }, { n: "Blessing Muzarabani", t: "KKR", v: 4, s: "wkts" }, { n: "Jacob Duffy", t: "RCB", v: 3, s: "wkts" }, { n: "T Natarajan", t: "DC", v: 3, s: "wkts" }, { n: "Prasidh Krishna", t: "GT", v: 3, s: "wkts" }],
            sixes: [{ n: "Ryan Rickelton", t: "MI", v: 8, s: "sixes" }, { n: "Rohit Sharma", t: "MI", v: 6, s: "sixes" }, { n: "Ishan Kishan", t: "SRH", v: 5, s: "sixes" }, { n: "Ajinkya Rahane", t: "KKR", v: 5, s: "sixes" }, { n: "Cooper Connolly", t: "PBKS", v: 5, s: "sixes" }],
            strike: [{ n: "Finn Allen", t: "KKR", v: "400.0", s: "SR" }, { n: "Vaibhav Sooryavanshi", t: "RR", v: "305.9", s: "SR" }, { n: "Rajat Patidar", t: "RCB", v: "258.3", s: "SR" }, { n: "Aniket Verma", t: "SRH", v: "238.9", s: "SR" }, { n: "Devdutt Padikkal", t: "RCB", v: "234.6", s: "SR" }],
            economy: [{ n: "Jofra Archer", t: "RR", v: "4.75", s: "eco" }, { n: "Mohsin Khan", t: "LSG", v: "4.75", s: "eco" }, { n: "Marco Jansen", t: "PBKS", v: "5.00", s: "eco" }, { n: "Jacob Duffy", t: "RCB", v: "5.50", s: "eco" }, { n: "Nandre Burger", t: "RR", v: "6.50", s: "eco" }],
            catches: [{ n: "Angkrish Raghuvanshi", t: "KKR", v: 3, s: "catches" }, { n: "Ryan Rickelton", t: "MI", v: 3, s: "catches" }, { n: "Sam Curran", t: "GT", v: 3, s: "catches" }, { n: "Suryakumar Yadav", t: "PBKS", v: 2, s: "catches" }, { n: "Nehal Wadhera", t: "PBKS", v: 2, s: "catches" }],
        };"""

html = re.sub(r'const POINTS_TABLE_2026 = \[[^\]]*\];', new_points, html)
html = re.sub(r'const ISTAT2026 = \{[^\}]*\};', new_istat, html)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html patched with live data!")
