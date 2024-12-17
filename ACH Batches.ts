function main(workbook: ExcelScript.Workbook) {
	let selectedSheet = workbook.getActiveWorksheet();
	// Toggle auto filter on selectedSheet
	selectedSheet.getAutoFilter().apply(selectedSheet.getRange("A1:AC1"));
	// Custom sort on range spanned by auto filter
	selectedSheet.getAutoFilter().getRange().getSort().apply([{key: 0, ascending: true}], false, true);
	// Auto fit the columns of range G:G on selectedSheet
	selectedSheet.getRange("G:G").getFormat().autofitColumns();
	// Auto fit the columns of range H:H on selectedSheet
	selectedSheet.getRange("H:H").getFormat().autofitColumns();
	// Auto fit the columns of range K:K on selectedSheet
	selectedSheet.getRange("K:K").getFormat().autofitColumns();
	// Auto fit the columns of range R:R on selectedSheet
	selectedSheet.getRange("R:R").getFormat().autofitColumns();
	// Delete range S:AB on selectedSheet
	selectedSheet.getRange("S:AB").delete(ExcelScript.DeleteShiftDirection.left);
	// Delete range A:G on selectedSheet
	selectedSheet.getRange("A:G").delete(ExcelScript.DeleteShiftDirection.left);
	// Delete range B:G on selectedSheet
	selectedSheet.getRange("B:G").delete(ExcelScript.DeleteShiftDirection.left);
	// Delete range C:C on selectedSheet
	selectedSheet.getRange("C:C").delete(ExcelScript.DeleteShiftDirection.left);
}