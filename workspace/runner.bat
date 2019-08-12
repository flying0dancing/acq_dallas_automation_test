SET Suite_Dir=D:\Eva\acq_dallas_automation_test\suite_automation_test
SET Report_Dir=C:\scanflow_rt\workspace\CSScanFlowReliabilityTest\Report

echo "Run smoke test suite"

squishrunner --testsuite %Suite_Dir% --reportgen xmljunit,%Report_Dir%\results.xml --reportgen html,%Report_Dir%

echo "Finished running scripts"