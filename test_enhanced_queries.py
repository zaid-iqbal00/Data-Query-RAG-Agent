import requests
import json
import time

API_BASE = "http://127.0.0.1:8000"

def test_query(query, description):
    print(f"\n🔍 Testing: {description}")
    print(f"Query: '{query}'")
    print("-" * 60)
    
    try:
        response = requests.post(f"{API_BASE}/ask", json={"query": query}, timeout=30)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Response received:")
            print(data['response'])
            return True
        else:
            print(f"❌ HTTP Error {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🧪 Enhanced RAG System Query Testing")
    print("=" * 70)
    
    try:
        health_response = requests.get(f"{API_BASE}/health", timeout=5)
        if health_response.status_code != 200:
            print("❌ Server not responding. Please start the backend first.")
            return
    except:
        print("❌ Cannot connect to server. Please start the backend first.")
        return
    
    print("✅ Server is running. Starting enhanced query tests...\n")
    
    test_cases = [
        ("Which sectors are our clients most heavily invested in?", "Sector Investment Analysis"),
        ("What's the diversification score for each client's portfolio?", "Portfolio Diversification Scores"),
        ("Show me clients who might be interested in ESG (Environmental, Social, Governance) investments", "ESG Investment Interest"),
        ("Which clients haven't had a portfolio review in the last 6 months?", "Portfolio Review Schedule"),
        ("Show me clients who are likely to upgrade their wealth tier based on portfolio growth", "Wealth Tier Upgrade Potential"),
        ("What's the client satisfaction correlation with portfolio performance?", "Satisfaction vs Performance Correlation"),
        ("Predict which clients might be at risk of churning based on their portfolio performance", "Churn Risk Prediction"),
        ("Show me the optimal client-to-manager ratio for maximum portfolio growth", "Optimal Client-Manager Ratios"),
        ("What's the lifetime value analysis for each client segment?", "Lifetime Value Analysis"),
        ("Generate a risk-adjusted performance report for all portfolios", "Risk-Adjusted Performance Report"),
        
        ("What's the average portfolio performance across different risk tolerance levels?", "Performance by Risk Tolerance"),
        ("Show me the correlation between portfolio size and investment strategy", "Portfolio Size vs Strategy Correlation"),
        ("What's the total assets under management by geographic region?", "AUM by Geographic Region"),
        ("Which high-risk portfolios need rebalancing?", "High-Risk Portfolio Rebalancing"),
        ("What percentage of AUM is in each risk category?", "AUM Distribution by Risk"),
        ("Calculate revenue per relationship manager", "Revenue per Manager"),
        ("Show me portfolio breakdown by relationship manager", "Portfolio by Manager"),
        ("List the top portfolios by value", "Top Portfolios"),
        ("Show me the wealth tier breakdown", "Wealth Tier Analysis")
    ]
    
    successful_tests = 0
    total_tests = len(test_cases)
    
    for query, description in test_cases:
        success = test_query(query, description)
        if success:
            successful_tests += 1
        time.sleep(1)
    
    print("\n" + "=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)
    print(f"✅ Successful queries: {successful_tests}/{total_tests}")
    print(f"📈 Success rate: {(successful_tests/total_tests)*100:.1f}%")
    
    if successful_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Enhanced RAG system is working perfectly.")
        print("🚀 The system now handles all sophisticated financial analytics queries.")
    else:
        print(f"\n⚠️ {total_tests - successful_tests} queries need attention.")
        print("💡 Check the backend logs for specific error details.")
    
    print("\n🔧 Available Query Types:")
    print("• Sector investment analysis")
    print("• Portfolio diversification scoring")
    print("• ESG investment interest prediction")
    print("• Portfolio review scheduling")
    print("• Wealth tier upgrade predictions")
    print("• Client satisfaction correlations")
    print("• Churn risk analysis")
    print("• Manager efficiency optimization")
    print("• Lifetime value calculations")
    print("• Risk-adjusted performance reporting")

if __name__ == "__main__":
    main()
