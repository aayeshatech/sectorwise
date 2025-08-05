from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

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

@app.route('/')
def index():
    sectors = sorted(set(event['sector'] for event in astro_data))
    months = [datetime(2025, i, 1).strftime('%B') for i in range(1, 13)]
    symbols = sorted(symbol_to_sector.keys())
    return render_template('index.html', sectors=sectors, months=months, symbols=symbols)

@app.route('/report', methods=['POST'])
def report():
    report_type = request.form.get('report_type')
    result_data = None
    title = ""
    
    if report_type == 'sector':
        sector = request.form.get('sector')
        result_data = get_sector_report(sector)
        title = f"Astrological Report for {sector} Sector"
    elif report_type == 'month':
        month = request.form.get('month')
        result_data = get_month_report(month)
        title = f"Astrological Report for {month} 2025"
    elif report_type == 'symbol':
        symbol = request.form.get('symbol')
        result_data = get_symbol_report(symbol)
        if result_data is not None:
            sector_name = symbol_to_sector.get(symbol.upper(), "Unknown")
            title = f"Astrological Report for {symbol} ({sector_name} Sector)"
        else:
            title = f"No data found for symbol: {symbol}"
    
    if result_data is None or len(result_data) == 0:
        return render_template('no_results.html', title=title)
    
    # Format date for display
    for event in result_data:
        event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
    
    return render_template('report.html', 
                          data=result_data,
                          title=title,
                          count=len(result_data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
