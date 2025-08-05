import http.server
import socketserver
import os
import json
from datetime import datetime
from urllib.parse import parse_qs, urlparse

# Astrological data for 2025
astro_data = [
    {"date": "2025-01-15", "sector": "Pharma", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short biotech stocks with late-stage trials"},
    {"date": "2025-02-05", "sector": "Pharma", "transit_aspect": "Venus Sextile Neptune", "trend": "Bullish", "strategy": "Long generic drug manufacturers (e.g., Lupin)"},
    {"date": "2025-03-10", "sector": "Pharma", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long R&D-focused pharma (e.g., Sun Pharma)"},
    {"date": "2025-01-20", "sector": "Auto", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long commercial vehicle makers (e.g., Tata Motors)"},
    {"date": "2025-02-28", "sector": "Auto", "transit_aspect": "Venus Trine Uranus", "trend": "Bullish", "strategy": "Long EV stocks (e.g., Tesla, TATA EV)"},
    {"date": "2025-04-10", "sector": "Auto", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short auto parts suppliers"},
    {"date": "2025-01-25", "sector": "FMCG", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long staples (e.g., HUL, ITC)"},
    {"date": "2025-03-15", "sector": "FMCG", "transit_aspect": "Moon Trine Venus", "trend": "Bullish", "strategy": "Long rural-focused FMCG (e.g., Dabur)"},
    {"date": "2025-04-15", "sector": "FMCG", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury goods (e.g., premium cosmetics)"},
    {"date": "2025-01-30", "sector": "Metals", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold/silver miners (e.g., Vedanta)"},
    {"date": "2025-03-25", "sector": "Metals", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long steel (e.g., Tata Steel)"},
    {"date": "2025-05-10", "sector": "Metals", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short aluminum/copper miners"},
    {"date": "2025-02-14", "sector": "Oil & Gas", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long LNG exporters (e.g., Petronet)"},
    {"date": "2025-03-20", "sector": "Oil & Gas", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long oil refiners (e.g., Reliance)"},
    {"date": "2025-04-25", "sector": "Oil & Gas", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short upstream E&P companies"},
    {"date": "2025-01-25", "sector": "PSU Banks", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short banks with high NPAs (e.g., PNB)"},
    {"date": "2025-03-05", "sector": "PSU Banks", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long infrastructure lenders (e.g., SBI)"},
    {"date": "2025-04-10", "sector": "PSU Banks", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long PSU banks (e.g., BOB)"},
    {"date": "2025-02-28", "sector": "Telecom", "transit_aspect": "Jupiter Sextile Neptune", "trend": "Bullish", "strategy": "Long digital infrastructure (e.g., Indus Towers)"},
    {"date": "2025-03-25", "sector": "Telecom", "transit_aspect": "Mercury Trine Uranus", "trend": "Bullish", "strategy": "Long 5G stocks (e.g., Bharti Airtel)"},
    {"date": "2025-04-20", "sector": "Telecom", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short debt-laden telecoms (e.g., Vodafone Idea)"},
    {"date": "2025-01-15", "sector": "IT", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short mid-cap IT with high debt"},
    {"date": "2025-04-10", "sector": "IT", "transit_aspect": "Uranus Conjunct Jupiter", "trend": "Bullish", "strategy": "Long cybersecurity/blockchain (e.g., TCS)"},
    {"date": "2025-05-05", "sector": "IT", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long AI/cloud stocks (e.g., Infosys)"},
    {"date": "2025-01-30", "sector": "Agriculture", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long fertilizers/seeds (e.g., Coromandel)"},
    {"date": "2025-03-15", "sector": "Agriculture", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long agri-logistics (e.g., KRBL)"},
    {"date": "2025-04-05", "sector": "Agriculture", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    {"date": "2025-02-14", "sector": "Tea", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long tea exporters (e.g., McLeod Russel)"},
    {"date": "2025-04-05", "sector": "Tea", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short tea stocks due to weather risks"},
    {"date": "2025-05-20", "sector": "Tea", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long premium tea brands"},
    {"date": "2025-01-30", "sector": "Sugar", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long sugar stocks (e.g., Balrampur Chini)"},
    {"date": "2025-04-05", "sector": "Sugar", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    {"date": "2025-06-10", "sector": "Sugar", "transit_aspect": "Saturn Square Moon", "trend": "Bearish", "strategy": "Short sugar due to global oversupply"},
    {"date": "2025-02-14", "sector": "Hotel", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long hotel stocks (e.g., Indian Hotels)"},
    {"date": "2025-04-15", "sector": "Hotel", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury hotels"},
    {"date": "2025-05-25", "sector": "Hotel", "transit_aspect": "Mercury Retrograde", "trend": "Bearish", "strategy": "Avoid new positions; travel disruptions"},
    {"date": "2025-03-10", "sector": "Paper", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long paper companies (e.g., West Coast Paper)"},
    {"date": "2025-04-20", "sector": "Paper", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short paper stocks due to rising input costs"},
    {"date": "2025-05-05", "sector": "Paper", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long packaging paper (e.g., JK Paper)"},
    {"date": "2025-01-30", "sector": "Gold", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold ETFs (e.g., Goldbees)"},
    {"date": "2025-03-20", "sector": "Gold", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long gold miners (e.g., Titan)"},
    {"date": "2025-04-15", "sector": "Gold", "transit_aspect": "Venus Square Sun", "trend": "Bearish", "strategy": "Short gold futures"},
    {"date": "2025-02-28", "sector": "Silver", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long silver ETFs (e.g., Silverbees)"},
    {"date": "2025-05-25", "sector": "Silver", "transit_aspect": "Sun Trine Neptune", "trend": "Bullish", "strategy": "Long silver miners"},
    {"date": "2025-06-05", "sector": "Silver", "transit_aspect": "Mars Opposite Pluto", "trend": "Bearish", "strategy": "Short silver futures"},
    {"date": "2025-02-14", "sector": "Crude Oil", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long crude futures"},
    {"date": "2025-03-20", "sector": "Crude Oil", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long energy infrastructure"},
    {"date": "2025-04-25", "sector": "Crude Oil", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short oil services"},
    {"date": "2025-01-25", "sector": "Dow Jones", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-03-25", "sector": "Dow Jones", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/tech"},
    {"date": "2025-04-10", "sector": "Dow Jones", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Dow futures"},
    {"date": "2025-01-25", "sector": "Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-03-25", "sector": "Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/IT"},
    {"date": "2025-04-10", "sector": "Nifty", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Nifty futures"},
    {"date": "2025-01-25", "sector": "Bank Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short NBFCs with high debt"},
    {"date": "2025-04-15", "sector": "Bank Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long private banks (e.g., HDFC Bank)"},
    {"date": "2025-05-05", "sector": "Bank Nifty", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long financial services firms"},
    {"date": "2025-03-30", "sector": "BTC", "transit_aspect": "Jupiter Conjunct Uranus", "trend": "Bullish", "strategy": "Long BTC/ETH"},
    {"date": "2025-04-20", "sector": "BTC", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short crypto exchanges"},
    {"date": "2025-05-15", "sector": "BTC", "transit_aspect": "Uranus Trine Sun", "trend": "Bullish", "strategy": "Long DeFi tokens"},
]

# Symbol to sector mapping
symbol_to_sector = {
    "TATAMOTORS": "Auto",
    "SUNPHARMA": "Pharma",
    "HINDALCO": "Metals",
    "RELIANCE": "Oil & Gas",
    "SBIN": "PSU Banks",
    "BHARTIARTL": "Telecom",
    "TCS": "IT",
    "INFY": "IT",
    "COROMANDEL": "Agriculture",
    "Mcleodrussel": "Tea",
    "BALRAMCHIN": "Sugar",
    "INDIANHOTEL": "Hotel",
    "WESTCOAST": "Paper",
    "TITAN": "Gold",
    "GOLDBEES": "Gold",
    "SILVERBEES": "Silver",
    "PETRONET": "Oil & Gas",
    "HDFCBANK": "Bank Nifty",
    "BTC": "BTC",
    "ETH": "BTC"
}

def get_sector_report(sector):
    """Generate report for a specific sector"""
    sector_data = [event for event in astro_data if event['sector'] == sector]
    # Sort by date
    sector_data.sort(key=lambda x: x['date'])
    return sector_data

def get_month_report(month):
    """Generate report for a specific month"""
    month_num = datetime.strptime(month, "%B").month
    month_data = [event for event in astro_data if datetime.strptime(event['date'], "%Y-%m-%d").month == month_num]
    month_data.sort(key=lambda x: x['date'])
    return month_data

def get_symbol_report(symbol):
    """Generate report for a specific stock symbol"""
    symbol = symbol.upper()
    if symbol in symbol_to_sector:
        sector = symbol_to_sector[symbol]
        return get_sector_report(sector)
    else:
        # Try to find sector by keyword matching
        for sym, sec in symbol_to_sector.items():
            if symbol in sym or sym in symbol:
                return get_sector_report(sec)
        return None

def generate_html():
    """Generate the HTML for the web app"""
    sectors = sorted(set(event['sector'] for event in astro_data))
    months = [datetime(2025, i, 1).strftime('%B') for i in range(1, 13)]
    symbols = sorted(symbol_to_sector.keys())
    
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astrological Sector Report Generator</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            text-align: center;
        }}
        .container {{
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        .form-group {{
            margin-bottom: 15px;
        }}
        label {{
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }}
        select, input[type="text"] {{
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        button {{
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        button:hover {{
            background-color: #45a049;
        }}
        .tab-container {{
            margin-top: 20px;
        }}
        .tab {{
            overflow: hidden;
            border: 1px solid #ccc;
            background-color: #f1f1f1;
        }}
        .tab button {{
            background-color: inherit;
            float: left;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 14px 16px;
            transition: 0.3s;
            color: #333;
        }}
        .tab button:hover {{
            background-color: #ddd;
        }}
        .tab button.active {{
            background-color: #ccc;
        }}
        .tabcontent {{
            display: none;
            padding: 20px;
            border: 1px solid #ccc;
            border-top: none;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        tr:hover {{
            background-color: #e6f7ff;
        }}
        .summary {{
            margin: 20px 0;
            font-size: 18px;
            color: #555;
        }}
        .no-results {{
            color: #d9534f;
            font-weight: bold;
            text-align: center;
            padding: 20px;
        }}
    </style>
</head>
<body>
    <h1>🔮 Astrological Sector Report Generator</h1>
    
    <div class="container">
        <div class="tab-container">
            <div class="tab">
                <button class="tablinks active" onclick="openTab(event, 'sector-tab')">By Sector</button>
                <button class="tablinks" onclick="openTab(event, 'month-tab')">By Month</button>
                <button class="tablinks" onclick="openTab(event, 'symbol-tab')">By Symbol</button>
            </div>
            
            <div id="sector-tab" class="tabcontent" style="display: block;">
                <div class="form-group">
                    <label for="sector">Select Sector:</label>
                    <select id="sector" name="sector">
                        <option value="">-- Select Sector --</option>
                        {''.join([f'<option value="{sector}">{sector}</option>' for sector in sectors])}
                    </select>
                </div>
                <button onclick="generateSectorReport()">Generate Report</button>
            </div>
            
            <div id="month-tab" class="tabcontent">
                <div class="form-group">
                    <label for="month">Select Month:</label>
                    <select id="month" name="month">
                        <option value="">-- Select Month --</option>
                        {''.join([f'<option value="{month}">{month}</option>' for month in months])}
                    </select>
                </div>
                <button onclick="generateMonthReport()">Generate Report</button>
            </div>
            
            <div id="symbol-tab" class="tabcontent">
                <div class="form-group">
                    <label for="symbol">Enter Stock Symbol:</label>
                    <select id="symbol" name="symbol">
                        <option value="">-- Select Symbol --</option>
                        {''.join([f'<option value="{symbol}">{symbol}</option>' for symbol in symbols])}
                    </select>
                </div>
                <button onclick="generateSymbolReport()">Generate Report</button>
            </div>
        </div>
    </div>
    
    <div id="report-container"></div>
    
    <script>
        // Astrological data
        const astroData = {json.dumps(astro_data)};
        const symbolToSector = {json.dumps(symbol_to_sector)};
        
        function openTab(evt, tabName) {{
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {{
                tabcontent[i].style.display = "none";
            }}
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {{
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }}
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
        }}
        
        function formatDate(dateStr) {{
            const date = new Date(dateStr);
            return date.toLocaleDateString('en-US', {{ year: 'numeric', month: 'short', day: 'numeric' }});
        }}
        
        function generateSectorReport() {{
            const sector = document.getElementById('sector').value;
            if (!sector) {{
                alert('Please select a sector');
                return;
            }}
            
            const reportData = astroData.filter(event => event.sector === sector);
            reportData.sort((a, b) => new Date(a.date) - new Date(b.date));
            
            displayReport(`Astrological Report for ${{sector}} Sector`, reportData);
        }}
        
        function generateMonthReport() {{
            const month = document.getElementById('month').value;
            if (!month) {{
                alert('Please select a month');
                return;
            }}
            
            const monthNum = new Date(`${{month}} 1, 2025`).getMonth() + 1;
            const reportData = astroData.filter(event => {{
                const eventDate = new Date(event.date);
                return eventDate.getMonth() + 1 === monthNum;
            }});
            reportData.sort((a, b) => new Date(a.date) - new Date(b.date));
            
            displayReport(`Astrological Report for ${{month}} 2025`, reportData);
        }}
        
        function generateSymbolReport() {{
            const symbol = document.getElementById('symbol').value.toUpperCase();
            if (!symbol) {{
                alert('Please select a symbol');
                return;
            }}
            
            let sector = symbolToSector[symbol];
            if (!sector) {{
                // Try to find sector by keyword matching
                for (const [sym, sec] of Object.entries(symbolToSector)) {{
                    if (symbol.includes(sym) || sym.includes(symbol)) {{
                        sector = sec;
                        break;
                    }}
                }}
            }}
            
            if (!sector) {{
                displayReport(`No data found for symbol: ${{symbol}}`, []);
                return;
            }}
            
            const reportData = astroData.filter(event => event.sector === sector);
            reportData.sort((a, b) => new Date(a.date) - new Date(b.date));
            
            displayReport(`Astrological Report for ${{symbol}} (${{sector}} Sector)`, reportData);
        }}
        
        function displayReport(title, data) {{
            const container = document.getElementById('report-container');
            
            if (data.length === 0) {{
                container.innerHTML = `
                    <div class="container">
                        <h2>${{title}}</h2>
                        <div class="no-results">No astrological data found for your selection.</div>
                    </div>
                `;
                return;
            }}
            
            let tableRows = '';
            data.forEach(event => {{
                tableRows += `
                    <tr>
                        <td>${{formatDate(event.date)}}</td>
                        <td>${{event.sector}}</td>
                        <td>${{event.transit_aspect}}</td>
                        <td>${{event.trend}}</td>
                        <td>${{event.strategy}}</td>
                    </tr>
                `;
            }});
            
            container.innerHTML = `
                <div class="container">
                    <h2>${{title}}</h2>
                    <div class="summary">Total events: ${{data.length}}</div>
                    <table>
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Sector</th>
                                <th>Transit/Aspect</th>
                                <th>Trend</th>
                                <th>Strategy</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${{tableRows}}
                        </tbody>
                    </table>
                </div>
            `;
        }}
    </script>
</body>
</html>
    """
    return html

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(generate_html().encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    PORT = 5000
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
