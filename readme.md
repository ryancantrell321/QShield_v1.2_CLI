<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>
<body style="font-family: Arial, sans-serif; margin: 0% 10% 0% 10%">

<div style="text-align: center;">
    <a href="https://i.ibb.co.com/VYr8X9p/Logo.png">
        <img src="https://i.ibb.co.com/VYr8X9p/Logo.png" alt="Logo">
    </a>
</div>

<h1 style="text-align: center;">Pandora QShield</h1>
<h2 style="text-align: center;">Version: 1.2 CLI</h2>
<h3 style="color: green; text-align: center;">Release: January 2025</h3>
<h3 style="color: orangered; text-align: center;">&copy; RyanCantrell321, Pandora Dynamics</h3>
<h3 style="text-align: center;">License: <a href="https://www.gnu.org/licenses/gpl-3.0.html#license-text">GNU General Public License (GPL) v3.0</a></h3>

<div style="text-align: center;">
    <img src="https://img.shields.io/badge/python-3.12-darkgreen" alt="Python 3.12">
    <img src="https://img.shields.io/badge/GPL-v3.0-orangered" alt="GPL v3.0">
    <img alt="GitHub Downloads (all assets, all releases)" src="https://img.shields.io/github/downloads/ryancantrell321/QShield_v1.2_CLI/total">

</div>

<h2>⬇️ Downloads:</h2>


<h2>About</h2>
<p style="text-align: justify; font-size: 16px;">
    Welcome to <strong>Pandora QShield CLI</strong> – a user-friendly backup and restore solution designed to keep your qBittorrent settings secure!
    With Pandora QShield, you can safely backup and restore your application settings with just a few clicks, ensuring that your preferences and configurations 
    are preserved no matter what; reinstalling Windows, migrating Windows versions, or reinstalling the qBittorrent software from scratch!
</p>

<h2>🎯 Key Features</h2>
<ul style="text-align: justify; font-size: 16px;">
    <li><strong>Portability:</strong> No installation required. Just launch QShield_CLI.exe with admin privileges.</li>
    <li><strong>Secure Backup & Restore:</strong> Easily save and restore qBittorrent settings to a location of your choice.</li>
    <li><strong>Performance Optimization:</strong> Multi-instance defense mechanism and memory efficiency algorithm.</li>
    <li><strong>Precise Event Logs:</strong> Contains a logging system that records all actions for easy debugging.</li>
</ul>

<h2>📥 Minimum System Requirements</h2>
<ul style="text-align: justify; font-size: 16px;">
    <li>Intel or AMD processors (post-2014)</li>
    <li>64-bit Windows 10 Update 2020++ or Windows 11</li>
    <li>RAM: 6 GB or better</li>
    <li>qBittorrent version 4.0 or newer</li>
    <li>Free disk space: 5 GB or more</li>
</ul>

<p style="color: crimson;"><strong>NOTE: NOT TESTED ON ARM64 PROCESSORS</strong></p>

<h2>🐞 Known Bugs</h2>
<p style="text-align: justify; font-size: 16px;">
    In some devices, qBittorrent may lose internet connectivity after a restore. Manually set the connection interface in qBittorrent to "Any Interface":
</p>
<p style="text-align: center; font-size: 16px; color: orangered;"><strong>qBittorrent &gt; Settings &gt; Advanced &gt; Network Interface &gt; Any Interface</strong></p>
<p>We plan to address this bug in a future update.</p>

<div style="text-align: center; font-size: 16px;">
    <a href="https://imgbb.com/"><img src="https://i.ibb.co.com/PwRWJrK/Screenshot-1.png" alt="Screenshot 1"></a>
    <a href="https://ibb.co.com/NSp9mk5"><img src="https://i.ibb.co.com/zJbX7Lp/Screenshot-2.png" alt="Screenshot 2" width="500"></a>
    <a href="https://imgbb.com/"><img src="https://i.ibb.co.com/qxY48tR/Screenshot-3.png" alt="Screenshot 3" width="500"></a>
</div>



<div>
        <p style="text-align: justify; font-size: 16px;">
        Because of the design language used, resizing of the software results in the GUI elements getting messy and disordered. We plan to fix this in a future update with another design language.</p>
</div>
    
<h2>📚 How to Install</h2>
<p style="color: crimson; font-size: 16px;"><strong>QSHIELD IS PORTABLE. NO INSTALLATION NEEDED. FOLLOW THESE STEPS:</strong></p>
<ol style="text-align: justify; font-size: 16px;">
    <li>Download qShield_v1.2.zip</li>
    <li>Extract the downloaded .zip file.</li>
    <li>Open the folder named qShield_v1.2.</li>
    <li>Double-click qShield_v1.2.exe and grant admin privileges.</li>
</ol>

<h2>💻 Usage</h2>

<p><strong>For both Backup Mode and Restore Mode, path strings must be entered without quotation marks.</strong> They can include underscores but must not contain spaces or hyphens. Before restoring, ensure that your disk directories remain in the same location as when the data was backed up.</p>

<p>You will be presented with 6 options. You need to choose accordingly.</p>

<h3>Backup Instructions</h3>
<p>When you press <strong>1</strong> for backup, the software retrieves data from the following directories:</p>
<ul>
<li><code>%localappdata%\qBittorrent</code></li>
<li><code>%appdata%\qBittorrent</code></li>
</ul>
<p>You will then be prompted to specify a location to save the backup. This location must already exist and cannot include spaces or hyphens but can contain underscores. Once the path is provided, the backup process will proceed.</p>

<h3>Restore Instructions</h3>
<p>For restoration, press <strong>2</strong> to initiate the process. The tool will automatically extract data from the <code>.zip</code> file it previously created and restore it to the original directories. You must specify the file path and name of the <code>.zip</code> file.</p>

<div class="important">
<strong>Important:</strong> Ensure that qBittorrent is completely closed before attempting to restore data.
</div>

<h3>General Guidelines</h3>
<ul>
<li>Run the program as an administrator.</li>
<li>For restoration, specify the location and file name of the previously saved <code>.zip</code> file and press Enter.</li>
<li>If you attempt to perform a backup or restore without administrative privileges, Pandora QShield Software will not function properly.</li>
</ul>


<h2>📷 Screenshots and Usage Video</h2>

<div style="text-align: center;">
<img src="https://i.ibb.co.com/BLchYdC/Picture1.png" alt="Picture1" border="0">
<img src="https://i.ibb.co.com/SmK2HfP/Picture2.png" alt="Picture2" border="0">
<img src="https://i.ibb.co.com/xh7Ht7Q/Picture3.png" alt="Picture3" border="0">
<img src="https://i.ibb.co.com/YNsch2T/Picture4.png" alt="Picture4" border="0">
</div>

<div style="text-align: center;">
<video><source src=""></video>
</div>

<h2>⚠️WITH GREAT POWER COMES GREAT RESPONSIBILITY!⚠️</h2>
<p style="text-align: justify; font-size: 16px;">Use this data deletion tool if you are experiencing qBittorrent interface corruption

<a href="https://github.com/ryancantrell321/qShield_Deleter/releases/tag/v1.0">qShield Deleter</a>
    
<h2>📑 License</h2>
<p style="text-align: justify; font-size: 16px;">
    Pandora QShield is licensed under the <a href="https://www.gnu.org/licenses/gpl-3.0.html#license-text">GNU General Public License (GPL) v3.0</a>.
</p>

<h2>🌐 Future Enhancements</h2>
<p style="text-align: justify; font-size: 16px;">
    Planned features include password-protected secure backups and cloud storage support.
</p>

<h2>💿 Virus Scan Results</h2>
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <td style="text-align: center;">QShield_1920x1080.exe</td>
        <td style="text-align: center;"><a href="https://virusscan.jotti.org/en-US/filescanjob/7sehuf5uhf" target="_blank">https://virusscan.jotti.org/en-US/filescanjob/7sehuf5uhf</a></td>
    </tr>
    <tr>
        <td style="text-align: center;">QShield_1920x1080.zip</td>
        <td style="text-align: center;"><a href="https://virusscan.jotti.org/en-US/filescanjob/quwkgxe18f" target="_blank">https://virusscan.jotti.org/en-US/filescanjob/quwkgxe18f</a></td>
    </tr>

</table>


<h2>📞 Contact Us or Report a Bug</h2>
<p style="text-align: justify; font-size: 16px;">
    <a href="mailto:pandoradynamics@gmail.com">pandoradynamics@gmail.com</a> <br>
    <a href="https://facebook.com/pandoradynamics22">Pandora Dynamics | Facebook</a> <br>
    <a href="https://instagram.com/pandoradynamics22">Pandora Dynamics | Instagram</a>
</p>

<div style="text-align: center;">
    <a href="https://i.ibb.co.com/gTnpSd6/Pandora-Dynamics-Logo-5-1.png">
        <img src="https://i.ibb.co.com/gTnpSd6/Pandora-Dynamics-Logo-5-1.png" alt="Pandora Dynamics Logo">
    </a>
</div>

</body>
</html>
