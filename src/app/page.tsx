import Link from 'next/link';

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-4">Real Estate Management System</h1>
        <p className="text-xl text-gray-600 mb-8">Comprehensive property management solution with data visualization</p>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link 
            href="/dashboard" 
            className="px-6 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
          >
            Dashboard
          </Link>
          <Link 
            href="/api/streamlit" 
            target="_blank"
            className="px-6 py-3 bg-gray-200 text-gray-800 rounded-md hover:bg-gray-300 transition-colors"
          >
            Data Visualization
          </Link>
        </div>
      </div>
    </div>
  );
}