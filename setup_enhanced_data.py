from pymongo import MongoClient
import mysql.connector
from datetime import datetime, timedelta
import random
import os
from dotenv import load_dotenv

load_dotenv()

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["client_profiles_db"]
profiles_collection = mongo_db["profiles"]

profiles_collection.delete_many({})

enhanced_profiles = [
    {
        "name": "John Smith",
        "age": 45,
        "portfolio_value": 2500000,
        "wealth_tier": "Premium",
        "risk_tolerance": "Moderate",
        "investment_strategy": "Balanced",
        "portfolio_performance_ytd": 0.085,
        "geographic_region": "North America",
        "assigned_manager": "Alice Johnson",
        "satisfaction_score": 8.2,
        "months_since_last_review": 3,
        "annual_fee_rate": 0.015,
        "diversification_score": 8.1
    },
    {
        "name": "Sarah Johnson",
        "age": 38,
        "portfolio_value": 5200000,
        "wealth_tier": "Ultra High Net Worth",
        "risk_tolerance": "High",
        "investment_strategy": "Growth",
        "portfolio_performance_ytd": 0.142,
        "geographic_region": "North America",
        "assigned_manager": "Bob Chen",
        "satisfaction_score": 9.1,
        "months_since_last_review": 2,
        "annual_fee_rate": 0.012,
        "diversification_score": 6.5
    },
    {
        "name": "Michael Brown",
        "age": 52,
        "portfolio_value": 1800000,
        "wealth_tier": "High Net Worth",
        "risk_tolerance": "Conservative",
        "investment_strategy": "Conservative",
        "portfolio_performance_ytd": 0.061,
        "geographic_region": "Europe",
        "assigned_manager": "Alice Johnson",
        "satisfaction_score": 7.8,
        "months_since_last_review": 7,
        "annual_fee_rate": 0.018,
        "diversification_score": 9.2
    },
    {
        "name": "Emily Davis",
        "age": 29,
        "portfolio_value": 8500000,
        "wealth_tier": "Ultra High Net Worth",
        "risk_tolerance": "High",
        "investment_strategy": "Growth",
        "portfolio_performance_ytd": 0.168,
        "geographic_region": "Asia Pacific",
        "assigned_manager": "Carol Martinez",
        "satisfaction_score": 9.4,
        "months_since_last_review": 1,
        "annual_fee_rate": 0.010,
        "diversification_score": 6.8
    },
    {
        "name": "Robert Wilson",
        "age": 61,
        "portfolio_value": 3200000,
        "wealth_tier": "Premium",
        "risk_tolerance": "Moderate",
        "investment_strategy": "Balanced",
        "portfolio_performance_ytd": 0.094,
        "geographic_region": "North America",
        "assigned_manager": "Bob Chen",
        "satisfaction_score": 8.7,
        "months_since_last_review": 4,
        "annual_fee_rate": 0.014,
        "diversification_score": 8.3
    },
    {
        "name": "Lisa Wang",
        "age": 33,
        "portfolio_value": 4100000,
        "wealth_tier": "Premium",
        "risk_tolerance": "High",
        "investment_strategy": "Growth",
        "portfolio_performance_ytd": 0.156,
        "geographic_region": "Asia Pacific",
        "assigned_manager": "David Thompson",
        "satisfaction_score": 8.9,
        "months_since_last_review": 2,
        "annual_fee_rate": 0.013,
        "diversification_score": 7.2
    },
    {
        "name": "James Rodriguez",
        "age": 47,
        "portfolio_value": 6800000,
        "wealth_tier": "Ultra High Net Worth",
        "risk_tolerance": "Moderate",
        "investment_strategy": "Balanced",
        "portfolio_performance_ytd": 0.089,
        "geographic_region": "Europe",
        "assigned_manager": "Carol Martinez",
        "satisfaction_score": 8.5,
        "months_since_last_review": 3,
        "annual_fee_rate": 0.011,
        "diversification_score": 8.7
    },
    {
        "name": "Maria Garcia",
        "age": 41,
        "portfolio_value": 2900000,
        "wealth_tier": "Premium",
        "risk_tolerance": "Conservative",
        "investment_strategy": "Conservative",
        "portfolio_performance_ytd": 0.048,
        "geographic_region": "North America",
        "assigned_manager": "Alice Johnson",
        "satisfaction_score": 6.8,
        "months_since_last_review": 8,
        "annual_fee_rate": 0.016,
        "diversification_score": 9.1
    },
    {
        "name": "Thomas Anderson",
        "age": 36,
        "portfolio_value": 1950000,
        "wealth_tier": "High Net Worth",
        "risk_tolerance": "High",
        "investment_strategy": "Growth",
        "portfolio_performance_ytd": 0.201,
        "geographic_region": "North America",
        "assigned_manager": "David Thompson",
        "satisfaction_score": 9.6,
        "months_since_last_review": 1,
        "annual_fee_rate": 0.017,
        "diversification_score": 6.2
    },
    {
        "name": "Jennifer Lee",
        "age": 44,
        "portfolio_value": 7200000,
        "wealth_tier": "Ultra High Net Worth",
        "risk_tolerance": "Moderate",
        "investment_strategy": "Balanced",
        "portfolio_performance_ytd": 0.076,
        "geographic_region": "Asia Pacific",
        "assigned_manager": "Bob Chen",
        "satisfaction_score": 8.1,
        "months_since_last_review": 5,
        "annual_fee_rate": 0.011,
        "diversification_score": 8.4
    }
]

profiles_collection.insert_many(enhanced_profiles)
print(f"✅ Inserted {len(enhanced_profiles)} enhanced client profiles into MongoDB")

try:
    mysql_conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE", "your_mysql_db")
    )
    
    cursor = mysql_conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS relationship_managers")
    cursor.execute("""
        CREATE TABLE relationship_managers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            specialization VARCHAR(100),
            years_experience INT,
            client_count INT,
            total_aum DECIMAL(15,2),
            avg_client_satisfaction DECIMAL(3,2),
            performance_rating VARCHAR(20)
        )
    """)
    
    managers_data = [
        ("Alice Johnson", "Conservative Strategies", 12, 3, 7200000, 7.6, "Good"),
        ("Bob Chen", "Balanced Portfolios", 8, 3, 14400000, 8.6, "Excellent"), 
        ("Carol Martinez", "Growth & International", 15, 2, 15300000, 8.95, "Outstanding"),
        ("David Thompson", "High-Risk Growth", 6, 2, 6050000, 9.25, "Outstanding")
    ]
    
    cursor.executemany("""
        INSERT INTO relationship_managers 
        (name, specialization, years_experience, client_count, total_aum, avg_client_satisfaction, performance_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, managers_data)
    
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("""
        CREATE TABLE transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            client_name VARCHAR(100),
            account_number VARCHAR(50),
            transaction_type VARCHAR(50),
            amount DECIMAL(12,2),
            transaction_date DATE,
            sector VARCHAR(50),
            performance_impact DECIMAL(5,4)
        )
    """)
    
    transactions_data = [
        ("John Smith", "ACC001", "Stock Purchase", 125000, "2024-06-15", "Technology", 0.0485),
        ("Sarah Johnson", "ACC002", "Bond Investment", 200000, "2024-06-20", "Finance", 0.0320),
        ("Michael Brown", "ACC003", "Dividend Reinvestment", 85000, "2024-06-25", "Utilities", 0.0415),
        ("Emily Davis", "ACC004", "Growth Stock Purchase", 350000, "2024-07-01", "Technology", 0.0625),
        ("Robert Wilson", "ACC005", "Balanced Fund", 160000, "2024-07-05", "Mixed", 0.0390),
        ("Lisa Wang", "ACC006", "International Equity", 220000, "2024-07-08", "Healthcare", 0.0540),
        ("James Rodriguez", "ACC007", "Real Estate Investment", 275000, "2024-07-10", "Real Estate", 0.0445),
        ("Maria Garcia", "ACC008", "Conservative Bond", 95000, "2024-07-12", "Government", 0.0285),
        ("Thomas Anderson", "ACC009", "High-Growth Tech", 180000, "2024-07-13", "Technology", 0.0780),
        ("Jennifer Lee", "ACC010", "ESG Fund", 240000, "2024-07-14", "ESG", 0.0520)
    ]
    
    cursor.executemany("""
        INSERT INTO transactions 
        (client_name, account_number, transaction_type, amount, transaction_date, sector, performance_impact)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, transactions_data)
    
    mysql_conn.commit()
    cursor.close()
    mysql_conn.close()
    
    print("✅ Enhanced MySQL data setup completed successfully")
    print("✅ Created relationship managers table with performance data")
    print("✅ Created transactions table with sector and performance data")
    
except mysql.connector.Error as e:
    print(f"❌ MySQL Error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n🎯 Enhanced Data Setup Complete!")
print("\nNew Analytics Available:")
print("📊 Sector investment analysis")
print("📈 Portfolio diversification scores")
print("🌱 ESG investment interest identification")
print("⏰ Portfolio review scheduling")
print("📈 Wealth tier upgrade predictions")
print("🔄 Client satisfaction vs performance correlation")
print("⚠️ Churn risk prediction")
print("👥 Optimal client-to-manager ratios")
print("💎 Lifetime value analysis by segment")
print("📊 Risk-adjusted performance reporting")
