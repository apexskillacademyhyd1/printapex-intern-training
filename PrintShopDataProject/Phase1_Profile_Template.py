"""
PHASE 1: DATA PROFILING & ISSUE IDENTIFICATION
===============================================

Days 1-2: Understand the raw data
- Load both datasets
- Profile every column
- Identify data quality issues
- Log all findings

This is a template. Copy it into Jupyter and run cell-by-cell.
"""

# ============================================================================
# CELL 1: IMPORT LIBRARIES
# ============================================================================

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully")
print(f"pandas version: {pd.__version__}")


# ============================================================================
# CELL 2: LOAD BOTH DATASETS
# ============================================================================

# Adjust paths if needed
df_10k = pd.read_csv('../../data/raw/shops_raw_data_10k.csv')
df_25k = pd.read_csv('../../data/raw/shops_raw_data_25k.csv')

print(f"10k dataset loaded: {df_10k.shape[0]:,} rows × {df_10k.shape[1]} columns")
print(f"25k dataset loaded: {df_25k.shape[0]:,} rows × {df_25k.shape[1]} columns")


# ============================================================================
# CELL 3: QUICK PREVIEW
# ============================================================================

print("\n" + "="*80)
print("PREVIEW - 10K DATASET (First 5 rows)")
print("="*80)
print(df_10k.head())

print("\n" + "="*80)
print("COLUMN NAMES & TYPES")
print("="*80)
print(df_10k.dtypes)


# ============================================================================
# CELL 4: BASIC STATISTICS
# ============================================================================

print("\n" + "="*80)
print("BASIC STATISTICS - 10K DATASET")
print("="*80)
print(f"Total rows: {df_10k.shape[0]:,}")
print(f"Total columns: {df_10k.shape[1]}")
print(f"Memory usage: {df_10k.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Rows with NO missing values: {len(df_10k.dropna())}")
print(f"Exact duplicate rows: {df_10k.duplicated().sum()}")

print("\n" + "-"*80)
print("BASIC STATISTICS - 25K DATASET")
print("-"*80)
print(f"Total rows: {df_25k.shape[0]:,}")
print(f"Total columns: {df_25k.shape[1]}")
print(f"Memory usage: {df_25k.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Rows with NO missing values: {len(df_25k.dropna())}")
print(f"Exact duplicate rows: {df_25k.duplicated().sum()}")


# ============================================================================
# CELL 5: DETAILED INFO
# ============================================================================

print("\n" + "="*80)
print("DETAILED INFO - 10K DATASET")
print("="*80)
df_10k.info()


# ============================================================================
# CELL 6: NULL VALUES ANALYSIS
# ============================================================================

def null_summary(df, dataset_name):
    """Generate comprehensive null value report"""
    null_data = {
        'Column': df.columns,
        'Null_Count': df.isnull().sum(),
        'Null_Percent': round((df.isnull().sum() / len(df)) * 100, 2),
        'Data_Type': df.dtypes.values
    }
    summary_df = pd.DataFrame(null_data).sort_values('Null_Percent', ascending=False)
    
    print(f"\n{dataset_name} - NULL VALUES SUMMARY")
    print(f"Total columns: {len(summary_df)}")
    print(f"Columns with nulls: {(summary_df['Null_Count'] > 0).sum()}")
    print("\n" + summary_df.to_string(index=False))
    
    return summary_df

null_10k = null_summary(df_10k, "10K DATASET")
null_25k = null_summary(df_25k, "25K DATASET")


# ============================================================================
# CELL 7: DUPLICATE ANALYSIS
# ============================================================================

def duplicate_analysis(df, dataset_name):
    """Analyze duplicates in detail"""
    print(f"\n{'='*80}")
    print(f"DUPLICATE ANALYSIS - {dataset_name}")
    print(f"{'='*80}")
    
    # Exact row duplicates
    exact_dupes = df.duplicated().sum()
    print(f"Exact duplicate rows: {exact_dupes}")
    
    # Duplicate IDs
    dup_ids = df['id'].duplicated().sum()
    print(f"Duplicate ID values: {dup_ids}")
    
    # Duplicate slugs (if relevant)
    dup_slugs = df['slug'].duplicated().sum()
    print(f"Duplicate slug values: {dup_slugs}")
    
    # Show examples if any
    if exact_dupes > 0:
        print(f"\nExample of duplicate rows:")
        dupe_rows = df[df.duplicated(keep=False)].head(2)
        print(dupe_rows[['id', 'business_name', 'created_at', 'updated_at']])
    
    if dup_ids > 0:
        print(f"\nExample of duplicate IDs:")
        dup_id_rows = df[df['id'].duplicated(keep=False)].head(2)
        print(dup_id_rows[['id', 'business_name', 'city']])

duplicate_analysis(df_10k, "10K DATASET")
duplicate_analysis(df_25k, "25K DATASET")


# ============================================================================
# CELL 8: DATE FIELD ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("DATE FIELD ANALYSIS")
print("="*80)

date_columns = ['created_at', 'updated_at', 'approved_at', 'suspended_at', 'expired_at', 'subscription_verified_at', 'current_period_end']

for col in date_columns:
    if col in df_10k.columns:
        print(f"\n{col} (10K):")
        print(f"  Non-null: {df_10k[col].notna().sum():,}")
        print(f"  Min date: {df_10k[col].min()}")
        print(f"  Max date: {df_10k[col].max()}")
        
        # Check for future dates
        today = pd.Timestamp.now()
        future_count = (pd.to_datetime(df_10k[col], errors='coerce') > today).sum()
        if future_count > 0:
            print(f"  ⚠️  FUTURE DATES: {future_count} rows")


# ============================================================================
# CELL 9: IMPOSSIBLE DATE LOGIC
# ============================================================================

print("\n" + "="*80)
print("DATE LOGIC VALIDATION")
print("="*80)

try:
    df_10k['created_dt'] = pd.to_datetime(df_10k['created_at'], errors='coerce')
    df_10k['updated_dt'] = pd.to_datetime(df_10k['updated_at'], errors='coerce')
    
    # Check created > updated (impossible)
    impossible = (df_10k['created_dt'] > df_10k['updated_dt']).sum()
    print(f"\n10K - Rows where created_at > updated_at: {impossible}")
    if impossible > 0:
        print(f"  Example:")
        print(df_10k[df_10k['created_dt'] > df_10k['updated_dt']][['id', 'created_at', 'updated_at']].head(3))
    
    # Clean up temp columns
    df_10k.drop(['created_dt', 'updated_dt'], axis=1, inplace=True)
    
except Exception as e:
    print(f"Error during date validation: {e}")


# ============================================================================
# CELL 10: CATEGORICAL ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("CATEGORICAL FIELDS - DISTRIBUTION")
print("="*80)

categorical_fields = ['status', 'subscription_plan', 'subscription_status', 'gst_status']

for field in categorical_fields:
    if field in df_10k.columns:
        print(f"\n{field} (10K):")
        print(df_10k[field].value_counts(dropna=False))


# ============================================================================
# CELL 11: PHONE NUMBER FORMAT CHECK
# ============================================================================

print("\n" + "="*80)
print("PHONE NUMBER ANALYSIS")
print("="*80)

# Check contact_phone formats
print("\n10K - contact_phone formats (sample of first 50 non-null):")
phone_samples = df_10k['contact_phone'].dropna().head(50).unique()
for i, phone in enumerate(phone_samples[:10]):
    print(f"  {phone}")

# Count various formats
no_phone = df_10k['contact_phone'].isna().sum()
with_plus91 = df_10k['contact_phone'].astype(str).str.contains(r'^\+91', na=False).sum()
with_91_dash = df_10k['contact_phone'].astype(str).str.contains(r'^91-', na=False).sum()
plain_10 = df_10k['contact_phone'].astype(str).str.match(r'^\d{10}$', na=False).sum()

print(f"\nPhone format breakdown:")
print(f"  Missing: {no_phone}")
print(f"  Format +91...: {with_plus91}")
print(f"  Format 91-...: {with_91_dash}")
print(f"  Plain 10 digits: {plain_10}")


# ============================================================================
# CELL 12: BUSINESS NAME ISSUES
# ============================================================================

print("\n" + "="*80)
print("BUSINESS NAME ANALYSIS")
print("="*80)

# Check for leading/trailing spaces
leading_space = df_10k['business_name'].astype(str).str.startswith(' ').sum()
trailing_space = df_10k['business_name'].astype(str).str.endswith(' ').sum()
mixed_case = df_10k['business_name'].nunique()
all_lower = df_10k['business_name'].astype(str).str.islower().sum()

print(f"\nBusiness name issues:")
print(f"  With leading spaces: {leading_space}")
print(f"  With trailing spaces: {trailing_space}")
print(f"  Unique names: {mixed_case:,}")
print(f"  All lowercase: {all_lower}")

# Sample names with inconsistent casing
print(f"\nSample business names (first 20):")
for name in df_10k['business_name'].head(20):
    print(f"  '{name}'")


# ============================================================================
# CELL 13: POSTAL CODE VALIDATION
# ============================================================================

print("\n" + "="*80)
print("POSTAL CODE ANALYSIS")
print("="*80)

# Check postal code lengths
postal_null = df_10k['postal_code'].isna().sum()
postal_lengths = df_10k['postal_code'].astype(str).str.len().value_counts().sort_index()

print(f"Postal code breakdown:")
print(f"  Null values: {postal_null}")
print(f"  Length distribution:")
print(postal_lengths)

# Show invalid lengths
invalid_postal = df_10k[~df_10k['postal_code'].astype(str).str.match(r'^\d{6}$', na=False)]
print(f"\nInvalid postal codes (not 6 digits): {len(invalid_postal)}")
print(invalid_postal[['city', 'postal_code']].head(10))


# ============================================================================
# CELL 14: GST NUMBER VALIDATION
# ============================================================================

print("\n" + "="*80)
print("GST NUMBER ANALYSIS")
print("="*80)

# GST status distribution
print("GST Status distribution:")
print(df_10k['gst_status'].value_counts(dropna=False))

# Check GST number lengths
print("\nGST number format:")
gst_null = df_10k['gst_number'].isna().sum()
gst_lengths = df_10k['gst_number'].astype(str).str.len().value_counts().sort_index()

print(f"  Null values: {gst_null}")
print(f"  Length distribution (should be 15 for registered):")
print(gst_lengths)

# Check for mismatch: registered but no GST number
mismatch = df_10k[(df_10k['gst_status'] == 'registered') & (df_10k['gst_number'].isna())]
print(f"\nMismatch: registered status but no GST number: {len(mismatch)}")


# ============================================================================
# CELL 15: UPI CONFIGURATION
# ============================================================================

print("\n" + "="*80)
print("UPI PAYMENT CONFIGURATION")
print("="*80)

upi_configured = df_10k['payout_upi_id'].notna().sum()
upi_missing = df_10k['payout_upi_id'].isna().sum()

print(f"UPI configured: {upi_configured} ({100*upi_configured/len(df_10k):.1f}%)")
print(f"UPI missing: {upi_missing} ({100*upi_missing/len(df_10k):.1f}%)")

# Sample UPI IDs
print("\nSample UPI IDs (first 10):")
for upi in df_10k['payout_upi_id'].dropna().head(10):
    print(f"  {upi}")


# ============================================================================
# CELL 16: PRINTER CONFIGURATION
# ============================================================================

print("\n" + "="*80)
print("PRINTER CONFIGURATION")
print("="*80)

# Printer make distribution
print("Printer makes (top 10):")
print(df_10k['printer_make'].value_counts(dropna=False).head(10))

# Shops with no printer set
no_printer_make = (df_10k['printer_make'].isna() | (df_10k['printer_make'] == '')).sum()
print(f"\nShops with no printer make: {no_printer_make} ({100*no_printer_make/len(df_10k):.1f}%)")


# ============================================================================
# CELL 17: SUBSCRIPTION ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("SUBSCRIPTION ANALYSIS")
print("="*80)

# Plan distribution
print("Subscription plans (all shops):")
print(df_10k['subscription_plan'].value_counts(dropna=False))

# Status distribution
print("\nSubscription status:")
print(df_10k['subscription_status'].value_counts(dropna=False))

# Logic check: active status but no plan
logic_error = df_10k[(df_10k['status'] == 'active') & (df_10k['subscription_plan'].isna())]
print(f"\nLogic error: active shops with no subscription plan: {len(logic_error)}")


# ============================================================================
# CELL 18: CITY/STATE CONSISTENCY
# ============================================================================

print("\n" + "="*80)
print("CITY & STATE ANALYSIS")
print("="*80)

# Unique states
print(f"Unique states: {df_10k['state'].nunique()}")
print("\nState distribution (top 15):")
print(df_10k['state'].value_counts().head(15))

# Unique cities
print(f"\nUnique cities: {df_10k['city'].nunique()}")
print("City distribution (top 15):")
print(df_10k['city'].value_counts().head(15))


# ============================================================================
# CELL 19: DATA TYPE CHECK
# ============================================================================

print("\n" + "="*80)
print("DATA TYPE ANALYSIS")
print("="*80)

print("\n10K Dataset:")
print(df_10k.dtypes)


# ============================================================================
# CELL 20: GENERATE SUMMARY REPORT
# ============================================================================

print("\n" + "="*80)
print("SUMMARY - ISSUES TO INVESTIGATE")
print("="*80)

issues = []

# Issue 1: Nulls
for col in df_10k.columns:
    null_pct = (df_10k[col].isna().sum() / len(df_10k)) * 100
    if null_pct > 0.5:  # More than 0.5% null
        issues.append(f"{col}: {null_pct:.2f}% null ({df_10k[col].isna().sum()} rows)")

# Issue 2: Duplicates
if df_10k.duplicated().sum() > 0:
    issues.append(f"Exact duplicates: {df_10k.duplicated().sum()} rows")

# Issue 3: Bad dates
try:
    created = pd.to_datetime(df_10k['created_at'], errors='coerce')
    updated = pd.to_datetime(df_10k['updated_at'], errors='coerce')
    bad_dates = (created > updated).sum()
    if bad_dates > 0:
        issues.append(f"Impossible dates (created > updated): {bad_dates} rows")
except:
    pass

print("\nTop issues found:")
for i, issue in enumerate(issues, 1):
    print(f"{i}. {issue}")

print("\n" + "="*80)
print("PHASE 1 PROFILING COMPLETE")
print("="*80)
print("\nNow create output/issue_log.txt with detailed findings")
print("for each issue above.")
