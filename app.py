import streamlit as st
from datetime import datetime
from data import astro_data, symbol_to_sector

# Set page config
st.set_page_config(
    page_title="Astrological Sector Report Generator 2025",
    page_icon="🔮",
    layout="wide"
)

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

def format_report_data(report_data):
    """Create a formatted copy of the report data for display"""
    formatted_data = []
    for event in report_data:
        formatted_event = event.copy()
        formatted_event['date'] = datetime.strptime(event['date'], "%Y-%m-%d").strftime('%b %d, %Y')
        formatted_data.append(formatted_event)
    return formatted_data

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
                    formatted_data = format_report_data(report_data)
                    
                    # Display as dataframe
                    st.dataframe(
                        formatted_data,
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
                    formatted_data = format_report_data(report_data)
                    
                    # Display as dataframe
                    st.dataframe(
                        formatted_data,
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
                    formatted_data = format_report_data(report_data)
                    
                    # Display as dataframe
                    st.dataframe(
                        formatted_data,
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
                formatted_data = format_report_data(report_data)
                
                # Display as dataframe
                st.dataframe(
                    formatted_data,
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
