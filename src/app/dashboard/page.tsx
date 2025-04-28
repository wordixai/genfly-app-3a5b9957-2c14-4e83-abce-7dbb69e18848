"use client";

import { useState } from 'react';
import Link from 'next/link';
import { BarChart, LineChart, PieChart, ArrowRight, Home, Building, Users, DollarSign, Tool, PercentCircle } from 'lucide-react';

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="flex">
        {/* Sidebar */}
        <div className="w-64 bg-white shadow-md h-screen p-4">
          <div className="mb-8">
            <h1 className="text-2xl font-bold text-blue-800">Real Estate</h1>
            <p className="text-sm text-gray-500">Management Dashboard</p>
          </div>
          
          <nav className="space-y-1">
            <button 
              onClick={() => setActiveTab('overview')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'overview' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <Home className="mr-3 h-5 w-5" />
              Overview
            </button>
            
            <button 
              onClick={() => setActiveTab('properties')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'properties' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <Building className="mr-3 h-5 w-5" />
              Properties
            </button>
            
            <button 
              onClick={() => setActiveTab('tenants')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'tenants' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <Users className="mr-3 h-5 w-5" />
              Tenants
            </button>
            
            <button 
              onClick={() => setActiveTab('financial')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'financial' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <DollarSign className="mr-3 h-5 w-5" />
              Financial
            </button>
            
            <button 
              onClick={() => setActiveTab('maintenance')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'maintenance' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <Tool className="mr-3 h-5 w-5" />
              Maintenance
            </button>
            
            <button 
              onClick={() => setActiveTab('occupancy')}
              className={`flex items-center w-full px-4 py-2 text-left rounded-md ${activeTab === 'occupancy' ? 'bg-blue-50 text-blue-700' : 'text-gray-700 hover:bg-gray-100'}`}
            >
              <PercentCircle className="mr-3 h-5 w-5" />
              Occupancy
            </button>
          </nav>
          
          <div className="mt-8 pt-4 border-t">
            <Link 
              href="/api/streamlit" 
              target="_blank"
              className="flex items-center px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
            >
              Open Streamlit Dashboard
              <ArrowRight className="ml-2 h-4 w-4" />
            </Link>
          </div>
        </div>
        
        {/* Main content */}
        <div className="flex-1 p-8">
          <div className="mb-8">
            <h2 className="text-2xl font-bold text-gray-800">
              {activeTab === 'overview' && 'Dashboard Overview'}
              {activeTab === 'properties' && 'Property Management'}
              {activeTab === 'tenants' && 'Tenant Management'}
              {activeTab === 'financial' && 'Financial Analytics'}
              {activeTab === 'maintenance' && 'Maintenance Tracking'}
              {activeTab === 'occupancy' && 'Occupancy Analytics'}
            </h2>
            <p className="text-gray-600">
              View detailed analytics in the Streamlit dashboard for more insights.
            </p>
          </div>
          
          {/* Dashboard content */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {/* Cards will change based on active tab */}
            {activeTab === 'overview' && (
              <>
                <div className="bg-white p-6 rounded-lg shadow">
                  <div className="flex items-center">
                    <div className="p-3 rounded-full bg-blue-100 text-blue-600">
                      <Building className="h-8 w-8" />
                    </div>
                    <div className="ml-4">
                      <p className="text-sm font-medium text-gray-500">Total Properties</p>
                      <p className="text-2xl font-semibold text-gray-900">5</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow">
                  <div className="flex items-center">
                    <div className="p-3 rounded-full bg-green-100 text-green-600">
                      <Users className="h-8 w-8" />
                    </div>
                    <div className="ml-4">
                      <p className="text-sm font-medium text-gray-500">Total Tenants</p>
                      <p className="text-2xl font-semibold text-gray-900">44</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow">
                  <div className="flex items-center">
                    <div className="p-3 rounded-full bg-purple-100 text-purple-600">
                      <PercentCircle className="h-8 w-8" />
                    </div>
                    <div className="ml-4">
                      <p className="text-sm font-medium text-gray-500">Occupancy Rate</p>
                      <p className="text-2xl font-semibold text-gray-900">94%</p>
                    </div>
                  </div>
                </div>
                
                <div className="bg-white p-6 rounded-lg shadow col-span-1 md:col-span-2 lg:col-span-3">
                  <h3 className="text-lg font-medium text-gray-900 mb-4">Revenue Overview</h3>
                  <div className="h-64 flex items-center justify-center">
                    <p className="text-gray-500">
                      For detailed charts and analytics, please open the Streamlit dashboard.
                    </p>
                  </div>
                </div>
              </>
            )}
            
            {/* Similar blocks for other tabs */}
            {activeTab !== 'overview' && (
              <div className="bg-white p-6 rounded-lg shadow col-span-1 md:col-span-2 lg:col-span-3">
                <h3 className="text-lg font-medium text-gray-900 mb-4">{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} Analytics</h3>
                <div className="h-64 flex flex-col items-center justify-center">
                  <p className="text-gray-500 mb-4">
                    For detailed {activeTab} analytics and visualizations, please open the Streamlit dashboard.
                  </p>
                  <Link 
                    href="/api/streamlit" 
                    target="_blank"
                    className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
                  >
                    Open Streamlit Dashboard
                  </Link>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}