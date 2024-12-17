function main(workbook: ExcelScript.Workbook) {
	let selectedSheet = workbook.getActiveWorksheet();
	// Toggle auto filter on selectedSheet
	selectedSheet.getAutoFilter().apply(selectedSheet.getRange("A1:O1"));
	// Auto fit the columns of range D:D on selectedSheet
	selectedSheet.getRange("D:D").getFormat().autofitColumns();
	// Custom sort on range spanned by auto filter
	selectedSheet.getAutoFilter().getRange().getSort().apply([{key: 3, ascending: false}], false, true);
	// Custom sort on range spanned by auto filter
	selectedSheet.getAutoFilter().getRange().getSort().apply([{key: 3, ascending: true}], false, true);
	// Set width of column(s) at range J:J on selectedSheet to 8.14
	selectedSheet.getRange("J:J").getFormat().setColumnWidth(8.14);
	// Auto fit the columns of range J:J on selectedSheet
	selectedSheet.getRange("J:J").getFormat().autofitColumns();
	// Delete range J:M on selectedSheet
	selectedSheet.getRange("J:M").delete(ExcelScript.DeleteShiftDirection.left);
	// Auto fit the columns of range B:B on selectedSheet
	selectedSheet.getRange("B:B").getFormat().autofitColumns();
	// Delete range C:C on selectedSheet
	selectedSheet.getRange("C:C").delete(ExcelScript.DeleteShiftDirection.left);
	// Auto fit the columns of range E:E on selectedSheet
	selectedSheet.getRange("E:E").getFormat().autofitColumns();
	// Auto fit the columns of range F:F on selectedSheet
	selectedSheet.getRange("F:F").getFormat().autofitColumns();
	// Delete range F:F on selectedSheet
	selectedSheet.getRange("F:F").delete(ExcelScript.DeleteShiftDirection.left);
	// Delete range A:A on selectedSheet
	selectedSheet.getRange("A:A").delete(ExcelScript.DeleteShiftDirection.left);
}