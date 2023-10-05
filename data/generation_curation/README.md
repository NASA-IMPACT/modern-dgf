**1.2 Generation / Curation (Collection, Creation, Production, Acquisition, Curation, Ingestion, Storage)**
-------------------------------------------------------------------------------------------------------

<table>
    <thead>
        <tr class="header">
            <th><strong>Requirement</strong></th>
            <th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
        </tr>
    </thead>
    <tbody>
        <tr class="odd">
            <td>A1.2.1 Ensure complete and accurate ingest of data</td>
            <td>
                <p>B1.2.1a Obtain a manifest file from the data provider. The manifest file should contain total file
                    numbers and checksums of individual files using an SHA algorithm (recommend at minimum SHA256) [DE]
                </p>
                <p>B1.2.1b Confirm number of ingested files matches source [DE]</p>
                <p>B1.2.1c Perform checksums and confirm match to source [DE]</p>
                <p>B1.2.1d Generate an ingest report [DE]</p>
                <ul>
                    <li>
                        <p>An ingest report is a document that serves as a receipt verifying that the ingested data
                            matches the manifest file from the data provider (see B1.2.1a). It should include a list
                            of files with checksums, data volume, and date/time of ingest. This can be shared with
                            the data provider if needed.</p>
                    </li>
                    <li>
                        <p>The report should be in JSON format with key/value pairs</p>
                    </li>
                </ul>
            </td>
        </tr>
        <tr class="even">
            <td>A1.2.2 Ensure complete and accurate production of data</td>
            <td>
                <p>B1.2.2a Create checksums / manifest file during data production [DE]</p>
                <p>B1.2.2b Perform planned science quality checks for the data produced before release (see Requirement
                    A1.1.11) [DE]</p>
            </td>
        </tr>
        <tr class="odd">
            <td>A1.2.3 Validate that Planning and Design requirements (from Section A1.1) are met for data ingest and /
                or production</td>
            <td>B1.2.3 Perform review demonstrating implementation has met the defined requirements from the planning
                phase (i.e. everything specified for Requirements A1.1.3 through A1.1.16; data format, file naming
                conventions, etc.) [DE]</td>
        </tr>
        <tr class="even">
            <td>A1.2.4 Ensure data products are assigned persistent identifiers and cross-referenced if appropriate</td>
            <td>
                <p>B1.2.4 Include the persistent identifier (e.g. DOI) in the data product metadata [DS]</p>
                <ul>
                    <li>
                        <p><a
                                href="https://www.earthdata.nasa.gov/engage/doi-process#:~:text=To%20initiate%20the%20process%20of,NASA%20data%20repository%20for%20assistance"><span
                                    class="underline">ESDIS DOI Process</span></a>: Follow the ESDS process when
                            delivering data to a DAAC. DOIs should be reserved prior to the delivery of actual data
                            to a DAAC. Detailed steps for registering/reserving DOIs with ESDS as well as updating a
                            DOI are described in the <a
                                href="https://wiki.earthdata.nasa.gov/display/DOIsforEOSDIS/ESDIS+DOI+Process"><span
                                    class="underline">ESDS DOI Process</span></a>.</p>
                    </li>
                    <li>
                        <p><a href="https://help.zenodo.org/"><span class="underline">Zenodo Process</span></a>:
                            Follow this process for data not going to a DAAC; More details on how to upload data to
                            Zenodo are described in <a
                                href="https://drive.google.com/file/d/1zMc3YUFtjadxhv2RtveVMKJOXluCiSDu/view?usp=sharing"><span
                                    class="underline">this Zenodo best practice document</span></a>.</p>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
