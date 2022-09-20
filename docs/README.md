# Configuration Docs

This section contains all of the documents required to setup the Splunk App for Robotic Process Monitoring (RPM).

#1. Prepare Splunk for Data ingest

Splunk requires 2 data inputs for the App to work.  First is the creation of the [Splunk HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/9.0.1/Data/UsetheHTTPEventCollector).  This allows UiPath to stream events from webhooks to the HTTPS endpoint.  Second, is the standard HTTP Listening port :9997.  This is for the Splunk Universal Forwarder (UF) for Windows.  The UF does two operations, collecting Windows perfmon (CPU, Mem, Disk, and Network) from the Robots and Orchestrators and to constantly monitor the log files produced by UiPath.

#2. Configure Data Collection

- Configure UiPath webhooks with ALL available event streams
- Configure Splunk Universal Forwarders to capture UiPath logs and Windows Performance KPI's

#3. Validate and Use App

- Best practice is to make sure that the Splunk deployment and the data collection are communicating to make sure basic connectivity has been established.
- First, check to see that the 'uipath' index is recieving the webhook data by running the search 'index=uipath'.  If there are events in the index the search will return results validating that UiPath is streaming events to the Splunk HEC HTTPS endpoint.  Secondly, is to make sure the Splunk Universal Forwarder (UF) is connected.  You can review this by searching 'index=_internal' and looking at the 'host' field to see the hostname of the UiPath host running Orchestrator OR the Robot software itself.
