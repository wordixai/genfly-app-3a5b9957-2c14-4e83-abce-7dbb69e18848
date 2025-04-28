import { NextResponse } from 'next/server';

export async function GET() {
  // This endpoint will redirect to the Streamlit app
  return NextResponse.redirect('http://localhost:8501');
}