class Smartmeter:

	def __init__(self):
		self.messages = []
		self.baseTopic = 'ha/sensor/smartmeter'

	def prepareStringValue(self, value):
		value = value.strip()
		value = value.rstrip(')')
		return value

	def prepareFloatValue(self, value):
		value = self.prepareStringValue(value)
		value = float(value)
		return value

	def prepareIntegerValue(self, value):
		value = self.prepareStringValue(value)
		value = int(value)
		return value

	def addMessage(self, topic, payload):
		self.messages.append([topic, payload, 0, False])

	def emptyMessages(self):
		self.messages = []

	def countMessages(self):
		return len(self.messages)

	def getMessages(self):
		return self.messages

	def processTranscriptLine(self, line):

		buf = line.split('(')

		# electricity equipment identifier
		if buf[0] == '0-0:96.1.1':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/identifier', self.prepareStringValue(content[0]))

		# kWh tariff 1 delivered (laag/dal)
		elif buf[0] == '1-0:1.8.1':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/kwh-low', self.prepareFloatValue(content[0]))

		# kWh tariff 2 delivered (hoog/dag)
		elif buf[0] == '1-0:1.8.2':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/kwh-high', self.prepareFloatValue(content[0]))

		# kWh tariff 1 generated (laag/dal)
		elif buf[0] == '1-0:2.8.1':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/kwh-generated-low', self.prepareFloatValue(content[0]))

		# kWh tariff 2 generated (hoog/dag)
		elif buf[0] == '1-0:2.8.2':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/kwh-generated-high', self.prepareFloatValue(content[0]))

		# kWh tariff indicator (2 = hoog, 1 = laag)
		elif buf[0] == '0-0:96.14.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/kwh-indicator', self.prepareIntegerValue(content[0]))

		# current kW delivered (actueel verbruik)
		elif buf[0] == '1-0:1.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/current-watt', self.prepareFloatValue(content[0]))

		# current kW generated (actueel teruglevering)
		elif buf[0] == '1-0:2.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/current-watt-generated', self.prepareFloatValue(content[0]))

		# number of power failures in any phase
		elif buf[0] == '0-0:96.7.21':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/phase-failures', self.prepareFloatValue(content[0]))

		# number of long power failures in any phase
		elif buf[0] == '0-0:96.7.9':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/phase-extended-failures', self.prepareFloatValue(content[0]))

		# number voltage sags in phase L1 (spannings dip)
		elif buf[0] == '1-0:32.32.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-sags-l1', self.prepareFloatValue(content[0]))

		# number voltage sags in phase L2 (spannings dip)
		elif buf[0] == '1-0:52.32.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-sags-l2', self.prepareFloatValue(content[0]))

		# number voltage sags in phase L3 (spannings dip)
		elif buf[0] == '1-0:72.32.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-sags-l3', self.prepareFloatValue(content[0]))

		# number voltage swells in phase L1 (spannings piek)
		elif buf[0] == '1-0:32.36.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-swells-l1', self.prepareFloatValue(content[0]))

		# number voltage swells in phase L2 (spannings piek)
		elif buf[0] == '1-0:52.36.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-swells-l2', self.prepareFloatValue(content[0]))

		# number voltage swells in phase L3 (spannings piek)
		elif buf[0] == '1-0:72.36.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/voltage-swells-l3', self.prepareFloatValue(content[0]))

		# current Amps L1
		elif buf[0] == '1-0:31.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/amps-l1', self.prepareFloatValue(content[0]))

		# current Amps L2
		elif buf[0] == '1-0:51.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/amps-l2', self.prepareFloatValue(content[0]))

		# current Amps L3
		elif buf[0] == '1-0:71.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/amps-l3', self.prepareFloatValue(content[0]))

		# current Watts L1 delivered
		elif buf[0] == '1-0:21.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-l1', self.prepareFloatValue(content[0]))

		# current Watts L2 delivered
		elif buf[0] == '1-0:41.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-l2', self.prepareFloatValue(content[0]))

		# current Watts L3 delivered
		elif buf[0] == '1-0:61.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-l3', self.prepareFloatValue(content[0]))

		# current Watts L1 generated
		elif buf[0] == '1-0:22.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-generated-l1', self.prepareFloatValue(content[0]))

		# current Watts L2 generated
		elif buf[0] == '1-0:42.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-generated-l2', self.prepareFloatValue(content[0]))

		# current Watts L3 generated
		elif buf[0] == '1-0:62.7.0':
			content = buf[1].split('*')
			self.addMessage(self.baseTopic + '/electricity/watts-generated-l3', self.prepareFloatValue(content[0]))

		# current gas count
		elif buf[0] == '0-1:24.2.1':
			content = buf[2].split('*')
			self.addMessage(self.baseTopic + '/gas/m3', self.prepareFloatValue(content[0]))
