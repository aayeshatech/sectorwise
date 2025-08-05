import pandas as pd
from datetime import datetime
import re

# Astrological data for 2025
astro_data = [
    # Pharma
    {"date": "2025-01-15", "sector": "Pharma", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short biotech stocks with late-stage trials"},
    {"date": "2025-02-05", "sector": "Pharma", "transit_aspect": "Venus Sextile Neptune", "trend": "Bullish", "strategy": "Long generic drug manufacturers (e.g., Lupin)"},
    {"date": "2025-03-10", "sector": "Pharma", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long R&D-focused pharma (e.g., Sun Pharma)"},
    
    # Auto
    {"date": "2025-01-20", "sector": "Auto", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long commercial vehicle makers (e.g., Tata Motors)"},
    {"date": "2025-02-28", "sector": "Auto", "transit_aspect": "Venus Trine Uranus", "trend": "Bullish", "strategy": "Long EV stocks (e.g., Tesla, TATA EV)"},
    {"date": "2025-04-10", "sector": "Auto", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short auto parts suppliers"},
    
    # FMCG
    {"date": "2025-01-25", "sector": "FMCG", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long staples (e.g., HUL, ITC)"},
    {"date": "2025-03-15", "sector": "FMCG", "transit_aspect": "Moon Trine Venus", "trend": "Bullish", "strategy": "Long rural-focused FMCG (e.g., Dabur)"},
    {"date": "2025-04-15", "sector": "FMCG", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury goods (e.g., premium cosmetics)"},
    
    # Metals
    {"date": "2025-01-30", "sector": "Metals", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold/silver miners (e.g., Vedanta)"},
    {"date": "2025-03-25", "sector": "Metals", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long steel (e.g., Tata Steel)"},
    {"date": "2025-05-10", "sector": "Metals", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short aluminum/copper miners"},
    
    # Oil & Gas
    {"date": "2025-02-14", "sector": "Oil & Gas", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long LNG exporters (e.g., Petronet)"},
    {"date": "2025-03-20", "sector": "Oil & Gas", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long oil refiners (e.g., Reliance)"},
    {"date": "2025-04-25", "sector": "Oil & Gas", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short upstream E&P companies"},
    
    # PSU Banks
    {"date": "2025-01-25", "sector": "PSU Banks", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short banks with high NPAs (e.g., PNB)"},
    {"date": "2025-03-05", "sector": "PSU Banks", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long infrastructure lenders (e.g., SBI)"},
    {"date": "2025-04-10", "sector": "PSU Banks", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long PSU banks (e.g., BOB)"},
    
    # Telecom
    {"date": "2025-02-28", "sector": "Telecom", "transit_aspect": "Jupiter Sextile Neptune", "trend": "Bullish", "strategy": "Long digital infrastructure (e.g., Indus Towers)"},
    {"date": "2025-03-25", "sector": "Telecom", "transit_aspect": "Mercury Trine Uranus", "trend": "Bullish", "strategy": "Long 5G stocks (e.g., Bharti Airtel)"},
    {"date": "2025-04-20", "sector": "Telecom", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short debt-laden telecoms (e.g., Vodafone Idea)"},
    
    # IT
    {"date": "2025-01-15", "sector": "IT", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short mid-cap IT with high debt"},
    {"date": "2025-04-10", "sector": "IT", "transit_aspect": "Uranus Conjunct Jupiter", "trend": "Bullish", "strategy": "Long cybersecurity/blockchain (e.g., TCS)"},
    {"date": "2025-05-05", "sector": "IT", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long AI/cloud stocks (e.g., Infosys)"},
    
    # Agriculture
    {"date": "2025-01-30", "sector": "Agriculture", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long fertilizers/seeds (e.g., Coromandel)"},
    {"date": "2025-03-15", "sector": "Agriculture", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long agri-logistics (e.g., KRBL)"},
    {"date": "2025-04-05", "sector": "Agriculture", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    
    # Tea
    {"date": "2025-02-14", "sector": "Tea", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long tea exporters (e.g., McLeod Russel)"},
    {"date": "2025-04-05", "sector": "Tea", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short tea stocks due to weather risks"},
    {"date": "2025-05-20", "sector": "Tea", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long premium tea brands"},
    
    # Sugar
    {"date": "2025-01-30", "sector": "Sugar", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long sugar stocks (e.g., Balrampur Chini)"},
    {"date": "2025-04-05", "sector": "Sugar", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    {"date": "2025-06-10", "sector": "Sugar", "transit_aspect": "Saturn Square Moon", "trend": "Bearish", "strategy": "Short sugar due to global oversupply"},
    
    # Hotel
    {"date": "2025-02-14", "sector": "Hotel", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long hotel stocks (e.g., Indian Hotels)"},
    {"date": "2025-04-15", "sector": "Hotel", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury hotels"},
    {"date": "2025-05-25", "sector": "Hotel", "transit_aspect": "Mercury Retrograde", "trend": "Bearish", "strategy": "Avoid new positions; travel disruptions"},
    
    # Paper
    {"date": "2025-03-10", "sector": "Paper", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long paper companies (e.g., West Coast Paper)"},
    {"date": "2025-04-20", "sector": "Paper", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short paper stocks due to rising input costs"},
    {"date": "2025-05-05", "sector": "Paper", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long packaging paper (e.g., JK Paper)"},
    
    # Gold
    {"date": "2025-01-30", "sector": "Gold", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold ETFs (e.g., Goldbees)"},
    {"date": "2025-03-20", "sector": "Gold", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long gold miners (e.g., Titan)"},
    {"date": "2025-04-15", "sector": "Gold", "transit_aspect": "Venus Square Sun", "trend": "Bearish", "strategy": "Short gold futures"},
    
    # Silver
    {"date": "2025-02-28", "sector": "Silver", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long silver ETFs (e.g., Silverbees)"},
    {"date": "2025-05-25", "sector": "Silver", "transit_aspect": "Sun Trine Neptune", "trend": "Bullish", "strategy": "Long silver miners"},
    {"date": "2025-06-05", "sector": "Silver", "transit_aspect": "Mars Opposite Pluto", "trend": "Bearish", "strategy": "Short silver futures"},
    
    # Crude Oil
    {"date": "2025-02-14", "sector": "Crude Oil", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long crude futures"},
    {"date": "2025-03-20", "sector": "Crude Oil", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long energy infrastructure"},
    {"date": "2025-04-25", "sector": "Crude Oil", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short oil services"},
    
    # Dow Jones
    {"date": "2025-01-25", "sector": "Dow Jones", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-03-25", "sector": "Dow Jones", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/tech"},
    {"date": "2025-04-10", "sector": "Dow Jones", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Dow futures"},
    
    # Nifty
    {"date": "2025-01-25", "sector": "Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-03-25", "sector": "Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/IT"},
    {"date": "2025-04-10", "sector": "Nifty", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Nifty futures"},
    
    # Bank Nifty
    {"date": "2025-01-25", "sector": "Bank Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short NBFCs with high debt"},
    {"date": "2025-04-15", "sector": "Bank Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long private banks (e.g., HDFC Bank)"},
    {"date": "2025-05-05", "sector": "Bank Nifty", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long financial services firms"},
    
    # BTC
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

# Create DataFrame
df = pd.DataFrame(astro_data)
df['date'] = pd.to_datetime(df['date'])

def get_sector_report(sector):
    """Generate report for a specific sector"""
    sector_df = df[df['sector'] == sector].sort_values('date')
    return sector_df

def get_month_report(month):
    """Generate report for a specific month"""
    month_num = datetime.strptime(month, "%B").month
    month_df = df[df['date'].dt.month == month_num].sort_values('date')
    return month_df

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

def display_report(report_df):
    """Display the report in a formatted way"""
    if report_df is None or report_df.empty:
        print("No data found for your selection.")
        return
    
    # Format date for display
    report_df = report_df.copy()
    report_df['date'] = report_df['date'].dt.strftime('%b %d, %Y')
    
    print("\n" + "="*100)
    print(f"{'DATE':<15} | {'SECTOR':<15} | {'TRANSIT/ASPECT':<30} | {'TREND':<10} | {'STRATEGY'}")
    print("="*100)
    
    for _, row in report_df.iterrows():
        print(f"{row['date']:<15} | {row['sector']:<15} | {row['transit_aspect']:<30} | {row['trend']:<10} | {row['strategy']}")
    
    print("="*100)
    print(f"\nTotal events: {len(report_df)}")

def main():
    print("=== Astrological Sector Report Generator ===")
    print("Available Sectors:", ", ".join(df['sector'].unique()))
    print("Available Months:", ", ".join([datetime(2025, i, 1).strftime('%B') for i in range(1, 13)]))
    print("Example Symbols:", ", ".join(list(symbol_to_sector.keys())[:5]))
    
    while True:
        print("\nOptions:")
        print("1. Get report by sector")
        print("2. Get report by month")
        print("3. Get report by stock symbol")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            sector = input("Enter sector name: ").title()
            report = get_sector_report(sector)
            display_report(report)
            
        elif choice == '2':
            month = input("Enter month name (e.g., January): ").title()
            try:
                report = get_month_report(month)
                display_report(report)
            except ValueError:
                print("Invalid month name. Please enter full month name (e.g., January)")
                
        elif choice == '3':
            symbol = input("Enter stock symbol (e.g., TATAMOTORS): ").upper()
            report = get_symbol_report(symbol)
            if report is not None:
                print(f"\nShowing report for {symbol} (Sector: {symbol_to_sector.get(symbol, 'Unknown')})")
                display_report(report)
            else:
                print(f"No data found for symbol: {symbol}")
                
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
