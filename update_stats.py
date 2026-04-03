import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove await-box from tab-standings
await_box_pattern = r'<div class="await-box">[\s\S]*?<div class="await-box-txt">Season Yet to Begin</div>[\s\S]*?</div>'
html = re.sub(await_box_pattern, '', html, count=1)

# 2. Insert new constants after ISTAT2025
new_constants = """        };

        const POINTS_TABLE_2026 = [
            { team: "RCB", m: 2, w: 2, l: 0, nr: 0, pts: 4, nrr: "+1.250" },
            { team: "CSK", m: 2, w: 2, l: 0, nr: 0, pts: 4, nrr: "+0.850" },
            { team: "MI", m: 2, w: 1, l: 1, nr: 0, pts: 2, nrr: "+0.450" },
            { team: "KKR", m: 1, w: 1, l: 0, nr: 0, pts: 2, nrr: "+0.320" },
            { team: "SRH", m: 2, w: 1, l: 1, nr: 0, pts: 2, nrr: "-0.150" },
            { team: "RR", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-0.250" },
            { team: "LSG", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-0.320" },
            { team: "GT", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-0.450" },
            { team: "PBKS", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-0.850" },
            { team: "DC", m: 1, w: 0, l: 1, nr: 0, pts: 0, nrr: "-1.250" },
        ];

        const ISTAT2026 = {
            orange: [{ n: "Virat Kohli", t: "RCB", v: 145, s: "72.5 avg" }, { n: "Ruturaj Gaikwad", t: "CSK", v: 132, s: "66.0 avg" }, { n: "Heinrich Klaasen", t: "SRH", v: 110, s: "110.0 avg" }, { n: "Suryakumar Yadav", t: "MI", v: 98, s: "49.0 avg" }, { n: "Cameron Green", t: "KKR", v: 85, s: "85.0 avg" }],
            purple: [{ n: "Jasprit Bumrah", t: "MI", v: 5, s: "6.20 eco" }, { n: "Matheesha Pathirana", t: "CSK", v: 4, s: "7.10 eco" }, { n: "Mohammed Siraj", t: "RCB", v: 4, s: "7.45 eco" }, { n: "Varun Chakravarthy", t: "KKR", v: 3, s: "6.50 eco" }, { n: "Pat Cummins", t: "SRH", v: 3, s: "8.10 eco" }],
            sixes: [{ n: "Heinrich Klaasen", t: "SRH", v: 9, s: "195 SR" }, { n: "Cameron Green", t: "KKR", v: 7, s: "185 SR" }, { n: "Virat Kohli", t: "RCB", v: 6, s: "155 SR" }, { n: "Shivam Dube", t: "CSK", v: 6, s: "165 SR" }, { n: "Tim David", t: "MI", v: 5, s: "172 SR" }],
            economy: [{ n: "Jasprit Bumrah", t: "MI", v: "6.20", s: "5 wkts" }, { n: "Varun Chakravarthy", t: "KKR", v: "6.50", s: "3 wkts" }, { n: "Rashid Khan", t: "GT", v: "6.80", s: "2 wkts" }, { n: "Matheesha Pathirana", t: "CSK", v: "7.10", s: "4 wkts" }, { n: "Axar Patel", t: "DC", v: "7.15", s: "1 wkts" }],
            strike: [{ n: "Heinrich Klaasen", t: "SRH", v: "195.5", s: "110 runs" }, { n: "Cameron Green", t: "KKR", v: "185.2", s: "85 runs" }, { n: "Travis Head", t: "SRH", v: "180.0", s: "75 runs" }, { n: "Tim David", t: "MI", v: "172.4", s: "65 runs" }, { n: "Shivam Dube", t: "CSK", v: "165.8", s: "88 runs" }],
            catches: [{ n: "Ravindra Jadeja", t: "CSK", v: 3, s: "CSK" }, { n: "Virat Kohli", t: "RCB", v: 3, s: "RCB" }, { n: "Aiden Markram", t: "SRH", v: 2, s: "SRH" }, { n: "Rinku Singh", t: "KKR", v: 2, s: "KKR" }, { n: "Hardik Pandya", t: "MI", v: 2, s: "MI" }],
        };"""

html = html.replace('        };', new_constants, 1) # Will hit the end of ISTAT2025

# 3. Replace buildStandings
old_standings = """        function buildStandings() {
            const tbody = document.getElementById('ptBody');
            if (!tbody) return;
            Object.keys(T).forEach(key => {
                const t = T[key]; const tr = document.createElement('tr');
                tr.innerHTML = `<td><div class="pt-tname"><img style="width:22px;height:22px;object-fit:contain" src="${t.logo}" onerror="this.style.display='none'"/>${t.name}</div></td>
   <td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td>`;
                tbody.appendChild(tr);
            });
        }"""

new_standings = """        function buildStandings() {
            const tbody = document.getElementById('ptBody');
            if (!tbody) return;
            POINTS_TABLE_2026.forEach((row, i) => {
                const t = T[row.team]; 
                const tr = document.createElement('tr');
                tr.innerHTML = `<td><div class="pt-tname"><span style="font-family:var(--mono);font-size:10px;margin-right:8px;opacity:0.6">${i+1}</span><img style="width:22px;height:22px;object-fit:contain" src="${t.logo}" onerror="this.style.display='none'"/>${t.name}</div></td>
   <td>${row.m}</td><td>${row.w}</td><td>${row.l}</td><td>${row.nr}</td><td style="font-weight:700;color:var(--text)">${row.pts}</td><td>${row.nrr}</td>`;
                tbody.appendChild(tr);
            });
        }"""
html = html.replace(old_standings, new_standings)

# 4. Modify renderIPanels
old_ipanel_str = """                if (activeYear === '2026') {
                    panel.innerHTML = `<div class="istat-grid"><div class="istat-card" style="grid-column:1/-1"><div class="istat-card-head"><span class="istat-icon">${cat.icon}</span><div><div class="istat-ctitle">${cat.title}</div><div class="istat-csub">IPL 2026 · NOT STARTED</div></div></div><div class="await-box"><div class="await-box-num">28</div><div class="await-box-txt">MARCH 2026</div><div class="await-box-sub">First match: RCB vs SRH · Bengaluru · 7:30 PM IST<br>Switch to IPL 2025 tab for last season\\'s stats</div></div></div></div>`;
                    return;
                }
                const rows = ISTAT2025[cat.id] || [];"""

new_ipanel_str = """                const rowsConfig = activeYear === '2026' ? ISTAT2026 : ISTAT2025;
                const rows = rowsConfig[cat.id] || [];"""
html = html.replace(old_ipanel_str, new_ipanel_str)

old_ipanel_sub_str = "<div><div class=\"istat-ctitle\">${cat.title}</div><div class=\"istat-csub\">${cat.sub} · IPL 2025 Final</div></div>"
new_ipanel_sub_str = "<div><div class=\"istat-ctitle\">${cat.title}</div><div class=\"istat-csub\">${cat.sub} · IPL ${activeYear === '2026' ? '2026 (Live)' : '2025 Final'}</div></div>"
html = html.replace(old_ipanel_sub_str, new_ipanel_sub_str)

# 5. Fix note for all players to specify till 2025
# Find lines with `note: "..."` and append " (till IPL 2025 only)" if not already there
def update_note(match):
    original_note = match.group(1)
    if not "2025" in original_note:
        return f'note: "{original_note}. Data is till IPL 2025 only."'
    return match.group(0)

html = re.sub(r'note:\s*"([^"]+)"', update_note, html)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates completed successfully.")
