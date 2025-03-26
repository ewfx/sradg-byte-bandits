import pandas as pd
import argparse
from model import anomoliesBot

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load an Excel file into a DataFrame")
    parser.add_argument("file", type=str, help="Path to the Excel file")
    
    args = parser.parse_args()
    anomoliesBot.andetect_anomalies(args.file)
