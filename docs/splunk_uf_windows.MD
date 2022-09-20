
# Installing Splunk Universal Forwarder for Windows

Installing the Splunk Universal Forwarder (UF) allows Splunk to collect the UiPath Robot Exeuction logs in realtime.  The Splunk UF also allows you to collect Host vital resources such as CPU, Memory, Disk, and Network.  The Windows forwarder can also collect Security logs from Event Logs.


## Configuring The Splunk Universial Forwarder (UF) for Windows 

The Splunk Universal Forwarder is installed on the UiPath Orchestrator Server.  Here are step by step instructions to install the Univeral Forwarder and configure the required data inputs.

### Setting up Splunk Universal Forwarder for Windows

1. Download the Splunk Universal Forwarder for Windows.  The .msi makes the installation simple prompting you through `Next` buttons to create configurations.  
[Download Splunk Universal Forwarder for Windows](https://www.splunk.com/en_us/download/universal-forwarder.html)

2. Move the .msi to the Windows machine running UiPath Orchestrator.  Then click the installer to begin the Installation wizard which will walk you through the initial setup.

3. First accept the license agreement and select your Splunk deployment to forward data to.  Once you have done both, click `Next`.
![Accept License & forward data to Splunk Cloud or Enterprise](./images/uf_images/splunk_uf_1.jpg)

4. Next enter the Administrator password for the Splunk Admin user.

![Authentication for UF account](./images/uf_images/splunk_uf_2.jpg)

5. Next is an optional configuration.  If you already have a Splunk deployment server to manage 100's/1000's of Universal Forwarders, you can point this newly installed UF to pull it's configuration from that server.  Those apps are installed as `deployment apps`.  If you are installing this Universal Forwarder and don't have an deployment server, you can leave the field blank and click `Next`.

![Optional - Deployment Server Config](./images/uf_images/splunk_uf_2.jpg)


## Available Webhook Eventtypes
<table>
<tr>
<th>UiPath Data Source</th>
<th>Data Description</th>
<th>Source</th>
</tr>
<tr>
<td>GitHub::Repo</td>
<td>Repositories</td>
<td>Repository created, deleted, archived, unarchived, publicized, privatized, edited, renamed, or transferred.</td>
</tr>
<tr>
<td>GitHub::Push</td>
<td>Pushes</td>
<td>Git push to a repository.</td>
</tr>
<tr>
<td>GitHub::PullRequest</td>
<td>Pull requests</td>
<td>Pull request opened, closed, reopened, edited, assigned, unassigned, review requested, review request removed, labeled, unlabeled, synchronized, ready for review, converted to draft, locked, unlocked, auto merge enabled, auto merge disabled, milestoned, or demilestoned.</td>
</tr>
<tr>
<td>GitHub::PullRequest::Review</td>
<td>Pull request reviews</td>
<td>Pull request review submitted, edited, or dismissed.</td>
</tr>
<tr>
<td>GitHub::CodeScanning</td>
<td>Code scanning alerts</td>
<td>Alerts identified by CodeQL and other 3rd party/OSS scanning tools.</td>
</tr>

</table>
