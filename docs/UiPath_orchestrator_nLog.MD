
# Configuring UiPath Orchestrator to send logs to Splunk HEC collector for RPM App for Splunk

Changing the UiPath nLog configuration will enable UiPath Orchestrator activity logs to Splunk removing the need for a webhook and Splunk universal forwarder configurations.


## Updates to UiPath.Orchestrator.dll.config file

Add "NLog.Assembly.Splunk" to the UiPath.Orchestrator.dll.config file as shown below.

![Authentication for UF account](./images/uf_images/splunk_uf_2.jpg)

### For that Nlog.Targets.Splunk assembly, copy Nlog.Targets.Splunk.dll (net5.0 version) to the C:\Uipath\Orchestrator folder

1. Download the Splunk Universal Forwarder for Windows.  The .msi makes the installation simple prompting you through `Next` buttons to create configurations.  
[Download Splunk Universal Forwarder for Windows](https://www.splunk.com/en_us/download/universal-forwarder.html)

2. Move the .msi to the Windows machine running UiPath Orchestrator.  Then click the installer to begin the Installation wizard which will walk you through the initial setup.

3. First accept the license agreement and select your Splunk deployment to forward data to.  Once you have done both, click `Next`.
![Accept License & forward data to Splunk Cloud or Enterprise](./images/uf_images/splunk_uf_1.jpg)

4. Next enter the Administrator password for the Splunk Admin user.

 ![Authentication for UF account](./images/uf_images/splunk_uf_2.jpg)

5. Next is an optional configuration.  If you already have a Splunk deployment server to manage 100's/1000's of Universal Forwarders, you can point this newly installed UF to pull it's configuration from that server.  Those apps are installed as `deployment apps`.  If you are installing this Universal Forwarder and don't have an deployment server, you can leave the field blank and click `Next`.
![Optional - Deployment Server Config](./images/uf_images/splunk_uf_2.jpg)

## Available UiPath data SourceTypes
<table>
<tr>
<th>UiPath Data Source</th>
<th>Data Description</th>
<th>Source</th>
</tr>
<tr>
<td>uipath</td>
<td>Webhook to HEC - UiPath push events to HEC</td>
<td>UiPath webhooks for Job, Queue, Robot, Process events</td>
</tr>
<tr>
<td>uipath_log</td>
<td>UiPath Automation Logs</td>
<td>UiPath Execution logs for automation runs.</td>
</tr>

</table>
