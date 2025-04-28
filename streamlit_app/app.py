import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Real Estate Analytics Dashboard",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API connection settings
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:4000/api")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2563EB;
        margin-bottom: 0.5rem;
    }
    .card {
        background-color: #F3F4F6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1E40AF;
    }
    .metric-label {
        font-size: 1rem;
        color: #6B7280;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions
def fetch_data(endpoint):
    """Fetch data from API endpoint"""
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return None

def format_currency(value):
    """Format value as currency"""
    return f"${value:,.2f}"

# Sidebar for navigation
st.sidebar.markdown("<div class='main-header'>Real Estate Analytics</div>", unsafe_allow_html=True)
page = st.sidebar.selectbox(
    "Select Dashboard",
    ["Overview", "Properties", "Tenants", "Financial", "Maintenance", "Occupancy"]
)

# Sidebar filters
st.sidebar.markdown("<div class='sub-header'>Filters</div>", unsafe_allow_html=True)
date_range = st.sidebar.date_input(
    "Date Range",
    value=[datetime.now().replace(month=1, day=1), datetime.now()],
    key="date_range"
)

# Mock data for demonstration
# In production, this would be replaced with actual API calls
@st.cache_data(ttl=300)
def load_mock_data():
    # Properties data
    properties = [
        {"id": 1, "name": "Sunset Apartments", "type": "RESIDENTIAL", "status": "ACTIVE", "city": "New York", "units": 24},
        {"id": 2, "name": "Downtown Office Complex", "type": "COMMERCIAL", "status": "ACTIVE", "city": "Chicago", "units": 12},
        {"id": 3, "name": "Riverside Villas", "type": "RESIDENTIAL", "status": "MAINTENANCE", "city": "Miami", "units": 8},
        {"id": 4, "name": "Tech Park", "type": "INDUSTRIAL", "status": "ACTIVE", "city": "San Francisco", "units": 5},
        {"id": 5, "name": "Green Meadows", "type": "LAND", "status": "LISTED_FOR_SALE", "city": "Austin", "units": 0}
    ]
    
    # Financial data
    payments = [
        {"month": "Jan", "amount": 45000, "category": "RENT"},
        {"month": "Feb", "amount": 47500, "category": "RENT"},
        {"month": "Mar", "amount": 46800, "category": "RENT"},
        {"month": "Apr", "amount": 48200, "category": "RENT"},
        {"month": "May", "amount": 49100, "category": "RENT"}
    ]
    
    expenses = [
        {"month": "Jan", "amount": 12000, "category": "MAINTENANCE"},
        {"month": "Feb", "amount": 9500, "category": "UTILITY"},
        {"month": "Mar", "amount": 11200, "category": "MAINTENANCE"},
        {"month": "Apr", "amount": 10800, "category": "UTILITY"},
        {"month": "May", "amount": 13500, "category": "INSURANCE"}
    ]
    
    # Occupancy data
    occupancy = [
        {"month": "Jan", "rate": 0.92},
        {"month": "Feb", "rate": 0.94},
        {"month": "Mar", "rate": 0.95},
        {"month": "Apr", "rate": 0.93},
        {"month": "May", "rate": 0.96}
    ]
    
    # Maintenance data
    maintenance = [
        {"status": "OPEN", "count": 8},
        {"status": "IN_PROGRESS", "count": 12},
        {"status": "COMPLETED", "count": 45},
        {"status": "CANCELLED", "count": 3}
    ]
    
    # Tenant data
    tenants = [
        {"property": "Sunset Apartments", "count": 22, "avg_lease_length": 12},
        {"property": "Downtown Office Complex", "count": 10, "avg_lease_length": 24},
        {"property": "Riverside Villas", "count": 7, "avg_lease_length": 6},
        {"property": "Tech Park", "count": 5, "avg_lease_length": 36},
        {"property": "Green Meadows", "count": 0, "avg_lease_length": 0}
    ]
    
    return {
        "properties": pd.DataFrame(properties),
        "payments": pd.DataFrame(payments),
        "expenses": pd.DataFrame(expenses),
        "occupancy": pd.DataFrame(occupancy),
        "maintenance": pd.DataFrame(maintenance),
        "tenants": pd.DataFrame(tenants)
    }

data = load_mock_data()

# Overview Dashboard
if page == "Overview":
    st.markdown("<div class='main-header'>Real Estate Portfolio Overview</div>", unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Total Properties</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{len(data['properties'])}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Total Units</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['properties']['units'].sum()}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Avg Occupancy</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['occupancy']['rate'].mean()*100:.1f}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Monthly Revenue</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{format_currency(data['payments']['amount'].iloc[-1])}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Property distribution by type
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='sub-header'>Property Distribution by Type</div>", unsafe_allow_html=True)
        fig = px.pie(
            data['properties'], 
            names='type', 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("<div class='sub-header'>Property Status</div>", unsafe_allow_html=True)
        fig = px.bar(
            data['properties'].groupby('status').size().reset_index(name='count'),
            x='status',
            y='count',
            color='status',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
    
    # Financial overview
    st.markdown("<div class='sub-header'>Financial Overview</div>", unsafe_allow_html=True)
    
    # Combine payments and expenses
    payments_df = data['payments'].copy()
    payments_df['type'] = 'Revenue'
    expenses_df = data['expenses'].copy()
    expenses_df['type'] = 'Expense'
    
    financial_df = pd.concat([payments_df, expenses_df])
    
    fig = px.bar(
        financial_df,
        x='month',
        y='amount',
        color='type',
        barmode='group',
        color_discrete_sequence=['#10B981', '#EF4444']
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="Amount ($)")
    st.plotly_chart(fig, use_container_width=True)

# Properties Dashboard
elif page == "Properties":
    st.markdown("<div class='main-header'>Property Analytics</div>", unsafe_allow_html=True)
    
    # Property filters
    col1, col2 = st.columns(2)
    with col1:
        property_type = st.multiselect(
            "Property Type",
            options=data['properties']['type'].unique(),
            default=data['properties']['type'].unique()
        )
    
    with col2:
        property_status = st.multiselect(
            "Property Status",
            options=data['properties']['status'].unique(),
            default=data['properties']['status'].unique()
        )
    
    # Filter properties
    filtered_properties = data['properties'][
        (data['properties']['type'].isin(property_type)) &
        (data['properties']['status'].isin(property_status))
    ]
    
    # Property table
    st.markdown("<div class='sub-header'>Property List</div>", unsafe_allow_html=True)
    st.dataframe(filtered_properties, use_container_width=True)
    
    # Property metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='sub-header'>Units by Property</div>", unsafe_allow_html=True)
        fig = px.bar(
            filtered_properties,
            x='name',
            y='units',
            color='type',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="Number of Units")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("<div class='sub-header'>Properties by City</div>", unsafe_allow_html=True)
        fig = px.pie(
            filtered_properties,
            names='city',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

# Tenants Dashboard
elif page == "Tenants":
    st.markdown("<div class='main-header'>Tenant Analytics</div>", unsafe_allow_html=True)
    
    # Tenant metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Total Tenants</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['tenants']['count'].sum()}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Avg Lease Length</div>", unsafe_allow_html=True)
        avg_lease = data['tenants'][data['tenants']['count'] > 0]['avg_lease_length'].mean()
        st.markdown(f"<div class='metric-value'>{avg_lease:.1f} months</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Occupancy Rate</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['occupancy']['rate'].iloc[-1]*100:.1f}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Tenant distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='sub-header'>Tenant Count by Property</div>", unsafe_allow_html=True)
        fig = px.bar(
            data['tenants'],
            x='property',
            y='count',
            color='property',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="Number of Tenants")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("<div class='sub-header'>Average Lease Length by Property</div>", unsafe_allow_html=True)
        fig = px.bar(
            data['tenants'][data['tenants']['count'] > 0],
            x='property',
            y='avg_lease_length',
            color='property',
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="Months")
        st.plotly_chart(fig, use_container_width=True)

# Financial Dashboard
elif page == "Financial":
    st.markdown("<div class='main-header'>Financial Analytics</div>", unsafe_allow_html=True)
    
    # Financial metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Total Revenue</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{format_currency(data['payments']['amount'].sum())}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Total Expenses</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{format_currency(data['expenses']['amount'].sum())}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Net Income</div>", unsafe_allow_html=True)
        net_income = data['payments']['amount'].sum() - data['expenses']['amount'].sum()
        st.markdown(f"<div class='metric-value'>{format_currency(net_income)}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Revenue vs Expenses
    st.markdown("<div class='sub-header'>Revenue vs Expenses</div>", unsafe_allow_html=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data['payments']['month'],
        y=data['payments']['amount'],
        mode='lines+markers',
        name='Revenue',
        line=dict(color='#10B981', width=3)
    ))
    fig.add_trace(go.Scatter(
        x=data['expenses']['month'],
        y=data['expenses']['amount'],
        mode='lines+markers',
        name='Expenses',
        line=dict(color='#EF4444', width=3)
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), xaxis_title="", yaxis_title="Amount ($)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Expense breakdown
    st.markdown("<div class='sub-header'>Expense Breakdown by Category</div>", unsafe_allow_html=True)
    
    expense_by_category = data['expenses'].groupby('category')['amount'].sum().reset_index()
    fig = px.pie(
        expense_by_category,
        values='amount',
        names='category',
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# Maintenance Dashboard
elif page == "Maintenance":
    st.markdown("<div class='main-header'>Maintenance Analytics</div>", unsafe_allow_html=True)
    
    # Maintenance metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Open Tasks</div>", unsafe_allow_html=True)
        open_tasks = data['maintenance'][data['maintenance']['status'] == 'OPEN']['count'].iloc[0]
        st.markdown(f"<div class='metric-value'>{open_tasks}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>In Progress</div>", unsafe_allow_html=True)
        in_progress = data['maintenance'][data['maintenance']['status'] == 'IN_PROGRESS']['count'].iloc[0]
        st.markdown(f"<div class='metric-value'>{in_progress}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Completed</div>", unsafe_allow_html=True)
        completed = data['maintenance'][data['maintenance']['status'] == 'COMPLETED']['count'].iloc[0]
        st.markdown(f"<div class='metric-value'>{completed}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Cancelled</div>", unsafe_allow_html=True)
        cancelled = data['maintenance'][data['maintenance']['status'] == 'CANCELLED']['count'].iloc[0]
        st.markdown(f"<div class='metric-value'>{cancelled}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Maintenance status
    st.markdown("<div class='sub-header'>Maintenance Tasks by Status</div>", unsafe_allow_html=True)
    
    fig = px.pie(
        data['maintenance'],
        values='count',
        names='status',
        color='status',
        color_discrete_map={
            'OPEN': '#EF4444',
            'IN_PROGRESS': '#F59E0B',
            'COMPLETED': '#10B981',
            'CANCELLED': '#6B7280'
        },
        hole=0.4
    )
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig, use_container_width=True)

# Occupancy Dashboard
elif page == "Occupancy":
    st.markdown("<div class='main-header'>Occupancy Analytics</div>", unsafe_allow_html=True)
    
    # Occupancy metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Current Occupancy Rate</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['occupancy']['rate'].iloc[-1]*100:.1f}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='metric-label'>Average Occupancy Rate</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metric-value'>{data['occupancy']['rate'].mean()*100:.1f}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Occupancy trend
    st.markdown("<div class='sub-header'>Occupancy Rate Trend</div>", unsafe_allow_html=True)
    
    fig = px.line(
        data['occupancy'],
        x='month',
        y='rate',
        markers=True,
        line_shape='spline',
        color_discrete_sequence=['#2563EB']
    )
    fig.update_traces(line=dict(width=3))
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        xaxis_title="",
        yaxis_title="Occupancy Rate",
        yaxis=dict(tickformat='.0%')
    )
    st.plotly_chart(fig, use_container_width=True)