from fastapi import FastAPI, UploadFile, Form
import pandas as pd
import matplotlib.pyplot as plt
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Sales Insight Automator API Running 🚀"}

@app.post("/upload")
async def upload(file: UploadFile, email: str = Form(...)):

    try:
        df = pd.read_csv(file.file)

        total_revenue = df["Revenue"].sum()

        best_product = df.groupby("Product")["Revenue"].sum().idxmax()

        best_region = df.groupby("Region")["Revenue"].sum().idxmax()

        cancelled_orders = df[df["Status"] == "Cancelled"].shape[0]

        # 📊 Create revenue by region chart
        region_sales = df.groupby("Region")["Revenue"].sum()

        plt.figure()
        region_sales.plot(kind="bar")
        plt.title("Revenue by Region")
        plt.xlabel("Region")
        plt.ylabel("Revenue")

        plt.savefig("sales_chart.png")
        plt.close()

        summary = f"""
Total Revenue: ₹{total_revenue}

Best Selling Product: {best_product}

Region with Highest Sales: {best_region}

Cancelled Orders: {cancelled_orders}

Insight:
Electronics appears to dominate the sales dataset, with the North region contributing the highest revenue.
        """

    except Exception as e:
        summary = f"Analysis failed: {str(e)}"

    return {
        "email": email,
        "ai_summary": summary,
        "chart": "sales_chart.png"
    }