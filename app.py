import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Astrological Sector Report Generator 2025",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Complete astrological data for 2025 (January to December)
astro_data = [
    # January 2025 Events
    {"date": "2025-01-15", "sector": "Pharma", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short biotech stocks with late-stage trials"},
    {"date": "2025-01-20", "sector": "Auto", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long commercial vehicle makers (e.g., Tata Motors)"},
    {"date": "2025-01-25", "sector": "FMCG", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long staples (e.g., HUL, ITC)"},
    {"date": "2025-01-25", "sector": "PSU Banks", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short banks with high NPAs (e.g., PNB)"},
    {"date": "2025-01-25", "sector": "Dow Jones", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-01-25", "sector": "Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short rate-sensitive stocks"},
    {"date": "2025-01-25", "sector": "Bank Nifty", "transit_aspect": "Saturn Square Pluto", "trend": "Bearish", "strategy": "Short NBFCs with high debt"},
    {"date": "2025-01-30", "sector": "Metals", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold/silver miners (e.g., Vedanta)"},
    {"date": "2025-01-30", "sector": "Agriculture", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long fertilizers/seeds (e.g., Coromandel)"},
    {"date": "2025-01-30", "sector": "Sugar", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long sugar stocks (e.g., Balrampur Chini)"},
    {"date": "2025-01-30", "sector": "Gold", "transit_aspect": "Pluto Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold ETFs (e.g., Goldbees)"},

    # February 2025 Events
    {"date": "2025-02-05", "sector": "Pharma", "transit_aspect": "Venus Sextile Neptune", "trend": "Bullish", "strategy": "Long generic drug manufacturers (e.g., Lupin)"},
    {"date": "2025-02-14", "sector": "Oil & Gas", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long LNG exporters (e.g., Petronet)"},
    {"date": "2025-02-14", "sector": "Tea", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long tea exporters (e.g., McLeod Russel)"},
    {"date": "2025-02-14", "sector": "Hotel", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long hotel stocks (e.g., Indian Hotels)"},
    {"date": "2025-02-14", "sector": "Crude Oil", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long crude futures"},
    {"date": "2025-02-28", "sector": "Auto", "transit_aspect": "Venus Trine Uranus", "trend": "Bullish", "strategy": "Long EV stocks (e.g., Tesla, TATA EV)"},
    {"date": "2025-02-28", "sector": "Telecom", "transit_aspect": "Jupiter Sextile Neptune", "trend": "Bullish", "strategy": "Long digital infrastructure (e.g., Indus Towers)"},
    {"date": "2025-02-28", "sector": "Silver", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long silver ETFs (e.g., Silverbees)"},

    # March 2025 Events
    {"date": "2025-03-05", "sector": "PSU Banks", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long infrastructure lenders (e.g., SBI)"},
    {"date": "2025-03-10", "sector": "Pharma", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long R&D-focused pharma (e.g., Sun Pharma)"},
    {"date": "2025-03-10", "sector": "Paper", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Long paper companies (e.g., West Coast Paper)"},
    {"date": "2025-03-15", "sector": "FMCG", "transit_aspect": "Moon Trine Venus", "trend": "Bullish", "strategy": "Long rural-focused FMCG (e.g., Dabur)"},
    {"date": "2025-03-15", "sector": "Agriculture", "transit_aspect": "Jupiter Trine Venus", "trend": "Bullish", "strategy": "Long agri-logistics (e.g., KRBL)"},
    {"date": "2025-03-20", "sector": "Oil & Gas", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long oil refiners (e.g., Reliance)"},
    {"date": "2025-03-20", "sector": "Crude Oil", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long energy infrastructure"},
    {"date": "2025-03-25", "sector": "Metals", "transit_aspect": "Mars Trine Saturn", "trend": "Bullish", "strategy": "Long steel (e.g., Tata Steel)"},
    {"date": "2025-03-25", "sector": "Telecom", "transit_aspect": "Mercury Trine Uranus", "trend": "Bullish", "strategy": "Long 5G stocks (e.g., Bharti Airtel)"},
    {"date": "2025-03-25", "sector": "Dow Jones", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/tech"},
    {"date": "2025-03-25", "sector": "Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long financials/IT"},
    {"date": "2025-03-30", "sector": "BTC", "transit_aspect": "Jupiter Conjunct Uranus", "trend": "Bullish", "strategy": "Long BTC/ETH"},

    # April 2025 Events
    {"date": "2025-04-05", "sector": "Agriculture", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    {"date": "2025-04-05", "sector": "Tea", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short tea stocks due to weather risks"},
    {"date": "2025-04-05", "sector": "Sugar", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short sugar/ethanol stocks"},
    {"date": "2025-04-10", "sector": "Auto", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short auto parts suppliers"},
    {"date": "2025-04-10", "sector": "PSU Banks", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long PSU banks (e.g., BOB)"},
    {"date": "2025-04-10", "sector": "IT", "transit_aspect": "Uranus Conjunct Jupiter", "trend": "Bullish", "strategy": "Long cybersecurity/blockchain (e.g., TCS)"},
    {"date": "2025-04-10", "sector": "Dow Jones", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Dow futures"},
    {"date": "2025-04-10", "sector": "Nifty", "transit_aspect": "Jupiter Trine Mercury", "trend": "Bullish", "strategy": "Long Nifty futures"},
    {"date": "2025-04-15", "sector": "FMCG", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury goods (e.g., premium cosmetics)"},
    {"date": "2025-04-15", "sector": "Hotel", "transit_aspect": "Saturn Square Venus", "trend": "Bearish", "strategy": "Short luxury hotels"},
    {"date": "2025-04-15", "sector": "Gold", "transit_aspect": "Venus Square Sun", "trend": "Bearish", "strategy": "Short gold futures"},
    {"date": "2025-04-15", "sector": "Bank Nifty", "transit_aspect": "Jupiter Conjunct Pluto", "trend": "Bullish", "strategy": "Long private banks (e.g., HDFC Bank)"},
    {"date": "2025-04-20", "sector": "Telecom", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short debt-laden telecoms (e.g., Vodafone Idea)"},
    {"date": "2025-04-20", "sector": "Paper", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short paper stocks due to rising input costs"},
    {"date": "2025-04-20", "sector": "BTC", "transit_aspect": "Saturn Square Mercury", "trend": "Bearish", "strategy": "Short crypto exchanges"},
    {"date": "2025-04-25", "sector": "Oil & Gas", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short upstream E&P companies"},
    {"date": "2025-04-25", "sector": "Crude Oil", "transit_aspect": "Saturn Square Neptune", "trend": "Bearish", "strategy": "Short oil services"},

    # May 2025 Events
    {"date": "2025-05-05", "sector": "IT", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long AI/cloud stocks (e.g., Infosys)"},
    {"date": "2025-05-05", "sector": "Paper", "transit_aspect": "Mercury Trine Neptune", "trend": "Bullish", "strategy": "Long packaging paper (e.g., JK Paper)"},
    {"date": "2025-05-05", "sector": "Bank Nifty", "transit_aspect": "Jupiter Trine Saturn", "trend": "Bullish", "strategy": "Long financial services firms"},
    {"date": "2025-05-10", "sector": "Metals", "transit_aspect": "Saturn Square Mars", "trend": "Bearish", "strategy": "Short aluminum/copper miners"},
    {"date": "2025-05-15", "sector": "BTC", "transit_aspect": "Uranus Trine Sun", "trend": "Bullish", "strategy": "Long DeFi tokens"},
    {"date": "2025-05-20", "sector": "Tea", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long premium tea brands"},
    {"date": "2025-05-25", "sector": "Hotel", "transit_aspect": "Mercury Retrograde", "trend": "Bearish", "strategy": "Avoid new positions; travel disruptions"},
    {"date": "2025-05-25", "sector": "Silver", "transit_aspect": "Sun Trine Neptune", "trend": "Bullish", "strategy": "Long silver miners"},

    # June 2025 Events
    {"date": "2025-06-05", "sector": "Silver", "transit_aspect": "Mars Opposite Pluto", "trend": "Bearish", "strategy": "Short silver futures"},
    {"date": "2025-06-10", "sector": "Sugar", "transit_aspect": "Saturn Square Moon", "trend": "Bearish", "strategy": "Short sugar due to global oversupply"},

    # July 2025 Events
    {"date": "2025-07-10", "sector": "Pharma", "transit_aspect": "Sun Trine Jupiter", "trend": "Bullish", "strategy": "Long biotech stocks with breakthrough drugs"},
    {"date": "2025-07-15", "sector": "Auto", "transit_aspect": "Venus Trine Mars", "trend": "Bullish", "strategy": "Long EV manufacturers with new models"},
    {"date": "2025-07-20", "sector": "FMCG", "transit_aspect": "Moon Trine Jupiter", "trend": "Bullish", "strategy": "Long consumer goods companies with strong brands"},
    {"date": "2025-07-25", "sector": "Metals", "transit_aspect": "Mercury Trine Saturn", "trend": "Neutral", "strategy": "Hold positions in diversified metal companies"},

    # August 2025 Events
    {"date": "2025-08-05", "sector": "Oil & Gas", "transit_aspect": "Mars Trine Uranus", "trend": "Bullish", "strategy": "Long energy companies with renewable focus"},
    {"date": "2025-08-10", "sector": "PSU Banks", "transit_aspect": "Jupiter Sextile Saturn", "trend": "Bullish", "strategy": "Long banks with improved NPA ratios"},
    {"date": "2025-08-15", "sector": "Telecom", "transit_aspect": "Venus Trine Neptune", "trend": "Bullish", "strategy": "Long telecom companies with 5G expansion"},
    {"date": "2025-08-20", "sector": "IT", "transit_aspect": "Sun Trine Uranus", "trend": "Bullish", "strategy": "Long tech companies with AI innovations"},
    {"date": "2025-08-25", "sector": "Agriculture", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long agri-companies with monsoon benefits"},

    # September 2025 Events
    {"date": "2025-09-05", "sector": "Tea", "transit_aspect": "Mercury Trine Venus", "trend": "Bullish", "strategy": "Long tea exporters with festive demand"},
    {"date": "2025-09-10", "sector": "Sugar", "transit_aspect": "Jupiter Trine Moon", "trend": "Bullish", "strategy": "Long sugar companies with ethanol capacity"},
    {"date": "2025-09-15", "sector": "Hotel", "transit_aspect": "Venus Trine Jupiter", "trend": "Bullish", "strategy": "Long hotel chains with tourist season"},
    {"date": "2025-09-20", "sector": "Paper", "transit_aspect": "Saturn Trine Uranus", "trend": "Neutral", "strategy": "Hold paper packaging companies"},
    {"date": "2025-09-25", "sector": "Gold", "transit_aspect": "Jupiter Trine Pluto", "trend": "Bullish", "strategy": "Long gold as safe haven asset"},

    # October 2025 Events
    {"date": "2025-10-05", "sector": "Gold", "transit_aspect": "Sun Conjunct Jupiter", "trend": "Bullish", "strategy": "Long gold as safe haven asset"},
    {"date": "2025-10-10", "sector": "Silver", "transit_aspect": "Venus Trine Mars", "trend": "Bullish", "strategy": "Long silver for industrial demand"},
    {"date": "2025-10-15", "sector": "Crude Oil", "transit_aspect": "Mars Square Saturn", "trend": "Bearish", "strategy": "Short oil due to geopolitical tensions"},
    {"date": "2025-10-20", "sector": "Dow Jones", "transit_aspect": "Jupiter Trine Neptune", "trend": "Bullish", "strategy": "Long blue-chip stocks"},
    {"date": "2025-10-25", "sector": "Nifty", "transit_aspect": "Mercury Trine Jupiter", "trend": "Bullish", "strategy": "Large-cap index funds"},

    # November 2025 Events
    {"date": "2025-11-05", "sector": "Bank Nifty", "transit_aspect": "Venus Trine Saturn", "trend": "Neutral", "strategy": "Hold banking sector with caution"},
    {"date": "2025-11-10", "sector": "BTC", "transit_aspect": "Uranus Trine Jupiter", "trend": "Bullish", "strategy": "Long crypto for institutional adoption"},
    {"date": "2025-11-15", "sector": "Pharma", "transit_aspect": "Neptune Trine Sun", "trend": "Bullish", "strategy": "Long specialty pharma companies"},
    {"date": "2025-11-20", "sector": "Auto", "transit_aspect": "Saturn Trine Uranus", "trend": "Volatile", "strategy": "Trade auto stocks with tight stops"},
    {"date": "2025-11-25", "sector": "FMCG", "transit_aspect": "Jupiter Conjunct Venus", "trend": "Bullish", "strategy": "Long FMCG for holiday season demand"},

    # December 2025 Events
    {"date": "2025-12-05", "sector": "Metals", "transit_aspect": "Mars Trine Jupiter", "trend": "Bullish", "strategy": "Long metals for infrastructure spending"},
    {"date": "2025-12-10", "sector": "Oil & Gas", "transit_aspect": "Venus Trine Neptune", "trend": "Neutral", "strategy": "Hold energy stocks with balanced exposure"},
    {"date": "2025-12-15", "sector": "PSU Banks", "transit_aspect": "Mercury Trine Saturn", "trend": "Neutral", "strategy": "Wait for policy clarity before entering"},
    {"date": "2025-12-20", "sector": "Telecom", "transit_aspect": "Sun Trine Uranus", "trend": "Bullish", "strategy": "Long telecom for digital growth"},
    {"date": "2025-12-25", "sector": "IT", "transit_aspect": "Jupiter Trine Uranus", "trend": "Bullish", "strategy": "Long IT for year-end tech rally"},
    {"date": "2025-12-30", "sector": "Agriculture", "transit_aspect": "Saturn Trine Jupiter", "trend": "Bullish", "strategy": "Long agri-companies for winter crop harvest"},
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

# Helper functions
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

def get_all_sectors_report():
    """Generate report for all sectors"""
    return astro_data

# Main app
def main():
    st.title("🔮 Astrological Sector Report Generator 2025")
    st.markdown("Generate astrological reports by sector, month, symbol, or view all sectors")
    
    # Get unique sectors and months
    sectors = sorted(set(event['sector'] for event in astro_data))
    months = [datetime(2025, i, 1).strftime('%B') for i in range(1, 13)]
    symbols = sorted(symbol_to_sector.keys())
    
    # Create tabs for different report types
    tab1, tab2, tab3, tab4 = st.tabs(["By Sector", "By Month", "By Symbol", "All Sectors"])
    
    with tab1:
        st.header("Sector Report")
        selected_sector = st.selectbox("Select a sector", [""] + sectors)
        
        if st.button("Generate Sector Report", key="sector_btn"):
            if selected_sector:
                report_data = get_sector_report(selected_sector)
                if report_data:
                    st.subheader(f"Astrological Report for {selected_sector} Sector (2025)")
                    st.markdown(f"**Total events:** {len(report_data)}")
                    
                    # Format date for display
                    for event in report_data:
                        event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
                    
                    # Display as dataframe
                    st.dataframe(
                        report_data,
                        column_config={
                            "date": "Date",
                            "sector": "Sector",
                            "transit_aspect": "Transit/Aspect",
                            "trend": "Trend",
                            "strategy": "Strategy"
                        },
                        use_container_width=True
                    )
                else:
                    st.warning(f"No data found for {selected_sector} sector")
            else:
                st.warning("Please select a sector")
    
    with tab2:
        st.header("Monthly Report")
        selected_month = st.selectbox("Select a month", [""] + months)
        
        if st.button("Generate Monthly Report", key="month_btn"):
            if selected_month:
                report_data = get_month_report(selected_month)
                if report_data:
                    st.subheader(f"Astrological Report for {selected_month} 2025")
                    st.markdown(f"**Total events:** {len(report_data)}")
                    
                    # Format date for display
                    for event in report_data:
                        event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
                    
                    # Display as dataframe
                    st.dataframe(
                        report_data,
                        column_config={
                            "date": "Date",
                            "sector": "Sector",
                            "transit_aspect": "Transit/Aspect",
                            "trend": "Trend",
                            "strategy": "Strategy"
                        },
                        use_container_width=True
                    )
                else:
                    st.warning(f"No data found for {selected_month}")
            else:
                st.warning("Please select a month")
    
    with tab3:
        st.header("Symbol Report")
        selected_symbol = st.selectbox("Select a symbol", [""] + symbols)
        
        if st.button("Generate Symbol Report", key="symbol_btn"):
            if selected_symbol:
                report_data = get_symbol_report(selected_symbol)
                if report_data:
                    sector_name = symbol_to_sector.get(selected_symbol.upper(), "Unknown")
                    st.subheader(f"Astrological Report for {selected_symbol} ({sector_name} Sector)")
                    st.markdown(f"**Total events:** {len(report_data)}")
                    
                    # Format date for display
                    for event in report_data:
                        event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
                    
                    # Display as dataframe
                    st.dataframe(
                        report_data,
                        column_config={
                            "date": "Date",
                            "sector": "Sector",
                            "transit_aspect": "Transit/Aspect",
                            "trend": "Trend",
                            "strategy": "Strategy"
                        },
                        use_container_width=True
                    )
                else:
                    st.warning(f"No data found for symbol {selected_symbol}")
            else:
                st.warning("Please select a symbol")
    
    with tab4:
        st.header("All Sectors Report")
        st.markdown("View all astrological events for all sectors in 2025")
        
        if st.button("Generate All Sectors Report", key="all_btn"):
            report_data = get_all_sectors_report()
            if report_data:
                st.subheader("Complete Astrological Report for All Sectors (2025)")
                st.markdown(f"**Total events:** {len(report_data)}")
                
                # Format date for display
                for event in report_data:
                    event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
                
                # Display as dataframe
                st.dataframe(
                    report_data,
                    column_config={
                        "date": "Date",
                        "sector": "Sector",
                        "transit_aspect": "Transit/Aspect",
                        "trend": "Trend",
                        "strategy": "Strategy"
                    },
                    use_container_width=True
                )
            else:
                st.warning("No data found")
    
    # Add footer
    st.markdown("---")
    st.markdown("© 2025 Astrological Sector Report Generator | Data is for informational purposes only")

if __name__ == "__main__":
    main()
