# Sales Insight Automator

## Overview
Sales Insight Automator is a full-stack AI-powered analytics tool that allows users to upload a CSV sales dataset and automatically generate business insights.

## Features
- Upload CSV sales data
- Automatic revenue calculation
- Best selling product detection
- Region with highest sales
- Cancelled orders analysis
- AI generated insight summary

## Tech Stack
Frontend: React  
Backend: FastAPI (Python)  
AI: Google Gemini API  

## Workflow
React Frontend → FastAPI API → Data Analysis → AI Insights

## How to Run

Backend

cd backend
python -m uvicorn main:app --reload

Frontend

cd frontend
npm start