## **4.1 Planning and Design**

<table>
    <thead>
        <tr class="header">
            <th><strong>Requirement</strong></th>
            <th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
        </tr>
    </thead>
    <tbody>
        <tr class="odd">
            <td>A4.1.1 Identify relevant code associated with the data</td>
            <td>
                <p>B4.1.1a Create an inventory of the source code and/or libraries. This should include code used to create the data or code used to read, use, analyze or visualize the data. [DS +DE]</p>
                <p>B4.1.1b Determine which code are not restricted and are available for open release [DE]</p>
            </td>
        </tr>
        <tr class="even">
            <td>A4.1.2 Identify where the code will be hosted</td>
            <td>B4.1.2 Select a source code versioning repository. IMPACT should use GitHub. [DE]</td>
        </tr>
        <tr class="odd">
            <td>A4.1.3 Select an open, permissive code license in line with open science requirements</td>
            <td>B4.1.3 Use a permissive license with broad acceptance in the science community to share your code. This includes Apache License 2.0, the BSD 3-Clause “Revised” License, and the MIT License (<a href="https://www.earthdata.nasa.gov/engage/open-data-services-and-software/esds-open-source-policy"><span class="underline">ESDS Open Source Software Policy | Earthdata (nasa.gov)</span></a>). Note that in the past, most IMPACT projects have used the Apache License 2.0. If submitting through the NASA center process, the Center Intellectual Property Counsel may provide guidance on which license to select. [DE]</td>
        </tr>
        <tr class="even">
            <td>A4.1.4 Identify or develop a plan for how the repository and contributions will be managed long term.
                The plan should include a code of conduct and guidelines for contributing to the public repository.</td>
            <td>
                <p>B4.1.4a Determine if the code should be public where public is defined as code with no expectations for maintenance or accepting contributions versus open source where open source is traditional open source software code with external contributions. Code should always at a minimum be public. [DS + DE]</p>
                <p>B4.1.4b If the code is being managed as an open source repository, a plan should be developed that describes how contributions will be managed, how frequently the repo will be checked for contributions, how contributions will be checked for quality, etc…[DS + DE]</p>
                <p>B4.1.4c A code of conduct for the repository should be provided. Use <a href="https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct"><span class="underline">the Github code of conduct</span></a> until NASA SMD guidance is available [DS + DE]</p>
            </td>
        </tr>
        <tr class="odd">
            <td>A4.1.5 Identify the open source process required for the organization</td>
            <td>
                <p>B4.1.5 Ensure that NASA’s <a href="https://code.nasa.gov/#/guide"><span class="underline">Open Source paperwork</span></a> has been submitted before code is written. Note that IMPACT is required to open source any software that is developed that is funded by NASA. Use the IMPACT Open Source Software process template based on the process outlined below:</p>
                <ul>
                    <li>
                        <p>Login to <a href="https://softwarerelease.ndc.nasa.gov/"><span class="underline">https://softwarerelease.ndc.nasa.gov/</span></a></p>
                    </li>
                    <li>
                        <p>Select “Create a new software release package”</p>
                    </li>
                    <li>
                        <p>Click <a href="https://invention.nasa.gov/"><span class="underline">https://invention.nasa.gov/</span></a> and select Report your New NTR</p>
                    </li>
                    <li>
                        <p>You will need Project information including a description and members</p>
                    </li>
                    <li>
                        <p>Submit for approval</p>
                    </li>
                    <li>
                        <p>Once approved your new software will appear in <a href="https://softwarerelease.ndc.nasa.gov/dashboard/"><span class="underline">https://softwarerelease.ndc.nasa.gov/dashboard/</span></a></p>
                    </li>
                    <li>
                        <p>Fill out all the required details and submit for approval: you will need to zip the source code to upload</p>
                    </li>
                    <li>
                        <p>You will get an email from the MSFC OSS group</p>
                    </li>
                    <li>
                        <p>Save that email and periodically ask for status [DS]</p>
                    </li>
                </ul>
            </td>
        </tr>
        <tr class="even">
            <td>A4.1.6 Define the software citation</td>
            <td>B4.1.6 Work with the code provider, the PI and others to come to a consensus on how the code should be cited. This should include identifying the main contributors to the code, the order of the contributors in the citation and the code name. [DS]</td>
        </tr>
    </tbody>
</table>
