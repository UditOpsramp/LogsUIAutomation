import yaml
import ruamel.yaml
import time
import os
import subprocess as sp

PostedLog = ''


def LogsGenerator(getLogCountData):
	global PostedLog

	workdirectory = os.path.dirname(os.path.abspath(__file__))
	with open(workdirectory + "/customLogConfigFile.yaml", "r") as file:
		logConfigFile = yaml.load_all(file, Loader=yaml.FullLoader)
		logConfigFileList = list(logConfigFile)

	for i in logConfigFileList:
		for k, j in i['inputs'].items():
			(j['include'][0]) = workdirectory + "/*.log"

	logConfigFile = yaml.safe_dump_all(
		logConfigFileList, sort_keys=False, explicit_start=True)

	yaml_new = ruamel.yaml.YAML(typ='safe')
	data = yaml_new.load(logConfigFile)

	with open(workdirectory + "/customLogConfigFile.yaml", "w") as file:
		yaml.dump(data, file, explicit_start=True, sort_keys=False)

	cmd = "sudo cp " + workdirectory + \
		  "/customLogConfigFile.yaml /opt/opsramp/agent/conf/log.d/log-config.yaml"
	sp.getoutput(cmd)

	cmd = "sudo systemctl restart opsramp-agent"
	sp.getoutput(cmd)

	time.sleep(30)

	cmd = "sudo go build -o " + workdirectory + "/loggeneratorscript " + workdirectory + "/loggeneratorscript.go"
	sp.getoutput(cmd)

	cmd = "sudo chmod +x " + workdirectory + "/loggeneratorscript"
	sp.getoutput(cmd)

	cmd = "sudo " + workdirectory + "/./loggeneratorscript" + ' ' + str(getLogCountData['NumberOfLogs']) + ' ' + str(
		getLogCountData['NumberOfLogFiles']) + ' ' + str(getLogCountData['LogMsgLength']) + ' ' + str(
		getLogCountData['LogRotateSizeInMB']) + ' ' + str(getLogCountData['TimeToSleep'])
	sp.getoutput(cmd)

	for i in logConfigFileList:
		for k, j in i['inputs'].items():
			path = (j['include'][0])

			cmd = "cat " + path
			PostedLog = sp.getoutput(cmd)

	time.sleep(20)

	RemoveLogsGenerator(workdirectory)

	return PostedLog


def RemoveLogsGenerator(workdirectory):
	cmd = "rm -rf " + workdirectory + "/loggeneratorscript"
	sp.getoutput(cmd)

	cmd = "rm -rf " + workdirectory + "/*.log"
	sp.getoutput(cmd)
