# excel-macros-and-scripts

Excel Macros and scripts for automating financial workflows and data organization.

---

## Office Scripts

### reconciliation_report.ts
- **Purpose**: Automates bank reconciliation reporting to organize financial data.
- **Features**:
  - Filters and structures financial data efficiently.
  - Provides organized output for reconciliation reporting.
- **How to Use**:
  1. Open Excel and navigate to the **Automate** tab.
  2. Upload the `reconciliation_report.ts` script into your script editor.
  3. Run the script on the relevant workbook containing bank reconciliation data.
  4. Review the processed and filtered output.

### ach_batches_report.ts
- **Purpose**: Automates reporting for ACH batches.
- **Features**:
  - Organizes ACH batches by **date**, **vendor**, and **addenda** (e.g., Invoice # or description of the invoice).
  - Filters and structures ACH-related financial data for easy analysis.
- **How to Use**:
  1. Open Excel and navigate to the **Automate** tab.
  2. Upload the `ach_batches_report.ts` script into your script editor.
  3. Run the script on the relevant workbook containing ACH batch data.
  4. Review the output sorted by date, vendor, and addenda details.

---

## Allocation Template

### allocation_template.xlsx
- **Purpose**: Automates the allocation of payments across funds and entities. *Useful if you're paying from multiple different bank accounts and entities and you have to allocate to multiple different funds*
- **Features**:
  - Designed for firms seeking to automate payment allocations without manual calculations.
  - Uses formulas to automatically allocate numbers based on input percentages.
  - **Allocation Database**:
    - Update the vendor database with relevant information.
    - Enter the percentages of entities or funds, ensuring they add up to 100%.
  - **Sheet 1**:
    - List all banks, funds, and entities paying for invoices.
    - Use the dropdown menu to select appropriate vendors and allocations.
- **How to Use**:
  1. Download `allocation_template.xlsx` from the repository.
  2. Open it in Excel.
  3. Update the **Allocation Database** with vendor information and percentages.
  4. On **Sheet 1**, list all banks, funds, and entities paying for the invoices.
  5. Use the dropdown menus to pick allocations – the formulas will handle the math automatically.
