**2.2 Generation / Curation**
-----------------------------

<table>
<thead>
<tr class="header">
<th><strong>Requirement</strong></th>
<th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A2.2.1 Provide the metadata specification information in the collection level metadata</td>
<td><p>B2.2.1a: UMM: Populate the ‘MetadataSpecification’ element. The Metadata Specification element requires the user to add in schema information into every collection record. It includes the schema's name, version, and URL location. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Metadata+Specification+for+UMM-C"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Metadata+Specification+for+UMM-C</span></a></p>
<p>B2.2.16b: STAC: Provide a value of “Collection” in the STAC ‘type’ element and the version of STAC the Collection implements in the ‘stac_version’ element. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.2 Provide the data product title in the collection level metadata</td>
<td><p>B2.2.2a UMM: Populate the ‘EntryTitle’ element. The Entry Title should be a descriptive, formal title of the dataset (see B2.1.3). [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Entry+Title"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Entry+Title</span></a></p>
<p>B2.2.2b STAC: Provide the data product title in the ‘title’ element. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.3 Provide the DOI information in the collection level metadata</td>
<td><p>B2.2.3a UMM: Include the DOI itself and the authority information in the DOI element. The authority for most metadata is <a href="https://doi.org/"><span class="underline">https://doi.org/</span></a>. In most cases, a DOI should be provided (i.e. ‘MissingReason is not an option). More information on DOI best practices for UMM can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/DOI"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/DOI</span></a> [DS]</p>
<p>B2.2.3b STAC: Leverage the <a href="https://github.com/stac-extensions/scientific"><span class="underline">Scientific Citation Extension Specification</span></a> and the ‘sci:doi’ element within that specification. This element is meant to contain the DOI value of the data, e.g. 10.1000/xyz123. This MUST NOT be a DOI link. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.4 Provide the abstract information in the collection level metadata</td>
<td><p>B2.2.4a UMM: Include the abstract, or dataset description, in the ‘Abstract’ element. The Abstract should provide a brief description of the resource the metadata represents.The abstract should summarize the dataset and mimic a journal abstract that is useful to the science community, but is also approachable for a first time user of the data. [DS] More information on abstract best practices for UMM can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Abstract"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Abstract</span></a></p>
<p>B2.2.4b STAC: Include the abstract, or dataset description, in the ‘description’ element for the collection specification. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.5 Provide information on the organization responsible for originating, processing, archiving, and/or distributing the dataset in the collection level metadata</td>
<td><p>B2.2.5a UMM: Include information on the organization responsible for originating, processing, archiving, and/or distributing the dataset in the ‘DataCenter’ element. The organization name must be selected from the <a href="https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all/3d012cef-866c-4df1-8fef-19ef25c1c2a3?gtm_keyword=NASA/IMPACT&amp;gtm_scheme=providers"><span class="underline">GCMD provider list</span></a>. The role of the organization must be selected from the following values: DISTRIBUTOR, ORIGINATOR, ARCHIVER, PROCESSOR. ‘NASA/IMPACT’ is a project in the <a href="https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all/3d012cef-866c-4df1-8fef-19ef25c1c2a3?gtm_keyword=NASA/IMPACT&amp;gtm_scheme=providers"><span class="underline">GCMD provider list</span></a>. This enumeration should be used for UMM Data Center information when IMPACT is the originator of the data. Selection of the role will depend on the individual project’s needs. [DS] For example, for the HLS data products, the role of NASA/IMPACT is ‘PROCESSOR.’ More details on the Data Center options and best practices for UMM can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Data+Center"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Data+Center</span></a></p>
<p>B2.2.5b STAC: Include the data center information in the ‘providers’ element [<a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/collection-spec/collection-spec.md#provider-object"><span class="underline">Provider Object</span></a>] using the Collection specification. When possible, use the <a href="https://gcmd.earthdata.nasa.gov/KeywordViewer/scheme/all/3d012cef-866c-4df1-8fef-19ef25c1c2a3?gtm_keyword=NASA/IMPACT&amp;gtm_scheme=providers"><span class="underline">GCMD provider list</span></a> enumeration in the ‘name’ element of the Provider Object. The ‘roles’ element should also be provided. Roles in STAC are: licensor, producer, processor or host. [DS]</p></td>
</tr>
<tr class="even">
<td>A2.2.6 Provide the data processing level in the collection level metadata</td>
<td><p>B2.2.6a UMM: Provide the data processing level in the ‘ProcessingLevel’ element. The data processing level should align with the EOSDIS data processing level whenever possible. [DS] More details on the EOSDIS data processing level can be found here: <a href="https://earthdata.nasa.gov/earth-science-data-systems-program/policies/data-information-policy/data-levels"><span class="underline">https://earthdata.nasa.gov/earth-science-data-systems-program/policies/data-information-policy/data-levels</span></a>. More details on data processing level best practices can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Processing+Level"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Processing+Level</span></a></p>
<p>B2.2.6b STAC: Provide the processing level using the ‘processing:level’ element using the processing extension (<a href="https://github.com/stac-extensions/processing"><span class="underline">https://github.com/stac-extensions/processing</span></a>) for Collections. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.7 Provide the data product production status in the collection level metadata</td>
<td><p>B2.2.7a UMM: Provide the collection production status in the ‘CollectionProgress’ element. Leverage the Collection Progress controlled vocabulary to describe the production status of the dataset. [DS] More info and the controlled vocabulary list can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Collection+Progress"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Collection+Progress</span></a></p>
<p>B2.2.7b TBD: STAC: The best practice for providing the collection progress using the STAC Collection spec is still TBD. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.8 Provide science keywords applicable to the data product in the collection level metadata</td>
<td><p>B2.2.8a UMM: Populate science keywords using the ‘ScienceKeywords’ element. Science keywords should represent the scientific parameters being provided in the data as well as any broader conceptual terms that may aid in describing the data. [DS] The Science Keywords are chosen from a <a href="https://www.earthdata.nasa.gov/learn/find-data/idn/gcmd-keywords"><span class="underline">controlled keyword hierarchy</span></a>. More information on science keyword best practices can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Science+Keywords"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Science+Keywords</span></a></p>
<p>B2.2.8b STAC: The ‘keywords’ element in the Collection specification should be used to provide science keywords. Science keywords should be selected from the <a href="https://www.earthdata.nasa.gov/learn/find-data/idn/gcmd-keywords"><span class="underline">GCMD science keywords list.</span></a> [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.9 Provide the temporal extent of the data in the collection level metadata</td>
<td><p>B2.2.9a UMM: Dates provided in CMR metadata should comply with the ISO 8601 Standard, which is an International Standard for the representation of dates and times. Select from one of three options in the UMM for describing the temporal extent of data: Single Date Time, Range Date Time and Periodic Date Time. More specific details on each of these options can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Temporal+Extents"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Temporal+Extents</span></a> [DS + DE]</p>
<p>B2.2.9b STAC: The temporal information should be provided in the Extent Object -&gt; <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/collection-spec/collection-spec.md#temporal-extent-object"><span class="underline">Temporal Extent Object</span></a>. If the data has an open range (e.g. active/ongoing collection), this can be specified by setting the start and/or end time to “null”. For example, [[&quot;2019-01-01T00:00:00Z&quot;, null]]. Timestamps should consist of a date and time in UTC and MUST be formatted according to <a href="https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"><span class="underline">RFC 3339, section 5.6</span></a>. The temporal reference system is the Gregorian calendar. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.10 Provide the spatial extent of the data in the collection level metadata</td>
<td><p>B2.2.10a UMM: Determine what type of spatial extent is being described in the metadata. In the CMR, there is the option to describe the horizontal, vertical, and orbital spatial coverage of a dataset along with its coordinate system and resolution. [DS] More details on each type can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent</span></a></p>
<p>For horizontal spatial extents, select an option that best describes the coverage of the data product. The four options in the CMR include: point, bounding rectangle, gpolygon and line. More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent</span></a></p>
<p>Determine whether any other spatial extent metadata (horizontal spatial resolution, geodetic model, etc) should be included in the metadata.</p>
<p>B2.2.10b STAC: The spatial information should be provided in the Extent Object -&gt; <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/collection-spec/collection-spec.md#spatial-extent-object"><span class="underline">Spatial Extent Object</span></a>. The first bounding box always describes the overall spatial extent of the data. All subsequent bounding boxes can be used to provide a more precise description of the extent and identify clusters of data. The coordinate reference system of the values is WGS 84 longitude/latitude. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.11 Provide the platform information (and optionally, instrument information) in the collection level metadata</td>
<td><p>B2.2.11a UMM: Provide the platform information using the ‘Platform’ element. Ensure all relevant platforms are listed in the metadata. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Platform"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Platform</span></a>. If applicable, it is also recommended that instruments/sensors be provided as well using the ‘Instrument’ element. More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Instrument"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Instrument</span></a>. The Platform name(s) must be selected from the <a href="https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/platforms?format=csv"><span class="underline">GCMD Platform keyword list</span></a> and Instrument/Sensor names must be selected from the <a href="https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/instruments/?format=csv"><span class="underline">GCMD Instruments keyword list</span></a>. If a platform is not listed, a new keyword may be requested through the <a href="https://forum.earthdata.nasa.gov/viewforum.php?f=7&amp;&amp;ServicesUsage=101"><span class="underline">GCMD Keywords Community Forum</span></a>.</p>
<p>B2.2.11b TBD: STAC: Provide platform and optionally instrument information using the ‘summaries’ element in the Collection spec. Instructions on how to appropriately do this is TBD (example: <a href="https://github.com/radiantearth/stac-spec/blob/master/examples/collection.json#L45"><span class="underline">https://github.com/radiantearth/stac-spec/blob/master/examples/collection.json#L45</span></a>) [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.12 Provide resource related URLs in the collection level metadata</td>
<td><p>B2.2.12a UMM: Provide links to all relevant documentation in the collection level metadata. A complete list of relevant documentation can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Related+URLs"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Related+URLs</span></a>. Any documentation created in either the ‘data’ ‘code,’ or ‘information content’ activities should also be included here. Describe each URL using the guidance provided here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Related+URLs"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Related+URLs</span></a> [DS]</p>
<p>B2.2.12b STAC: Provide links to all relevant information in the <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/collection-spec/collection-spec.md#link-object"><span class="underline">Link Object</span></a> -&gt; ‘href’ and ‘rel’ elements. Provide the actual link in the ‘href’ element. The ‘ref’ element describes the relationship between the collection and the URL. More information on relationships can be <a href="https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md#relation-types"><span class="underline">found here.</span></a> [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.13 Provide a unique identifier for the data product in the collection level metadata</td>
<td><p>B2.2.13a UMM: A unique identifier for the data product should be provided in the ‘ShortName’ element. This should take the form of a shortened or abbreviated name of the data product. [DS] More details on short name best practices can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Short+Name"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Short+Name</span></a></p>
<p>B2.2.13b STAC: A unique identifier for the data product should be provided in the ‘id’ element. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.14 Provide the data product version in the collection level metadata</td>
<td><p>B2.2.14a UMM: Provide the data product version number in the collection level metadata using the ‘Version’ element. [DS] More detailed information can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Version"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Version</span></a></p>
<p>B2.2.14b TBD: STAC: The best practice for providing the data product version using the STAC Collection spec. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.15 Provide the data product license information in the collection level metadata</td>
<td><p>B2.2.15a UMM: Provide the license information in the ‘UseConstraints’ element. At a minimum, it is recommended that a link to the relevant license be provided in the ‘UseConstraints/LicenseURL/Linkage’ field. [DS] Additional info and other options for providing the license information can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Use+Constraints"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Use+Constraints</span></a></p>
<p>Note: If a EULA identifier is available, linked it to the UMM-C under the ‘UseConstraints/EULAIdentifiers’ field.</p>
<p>B2.2.15b STAC: Provide the license using the ‘license’ element. The license should be selected from the SPDX License identifier list: <a href="https://spdx.org/licenses/"><span class="underline">https://spdx.org/licenses/</span></a>. Provide “varies” if multiple licenses apply and “proprietary” for all other cases. The default value for an open license should be “CC0-1.0” unless otherwise specified. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.16 Provide a unique identifier in the granule level metadata</td>
<td><p>B2.2.16a UMM: Provide the universal reference identifier of the granule in each metadata record using the ‘GranuleUR’ element. Typically, the Granule UR will match the granule's file name. However, other identifying information may be included. The UR must be completely unique when compared to all other data from the same provider (i.e. datasets with the same provider Id in CMR). [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Granule+UR"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Granule+UR</span></a></p>
<p>B2.2.16b STAC: Provide a unique identifier for the file/layer/granule in the <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/item-spec/item-spec.md#item-fields"><span class="underline">STAC Item spec</span></a> ‘id’ field. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.17 Provide a date indicating when the granule metadata was created in the granule level metadata</td>
<td><p>B2.2.17a UMM: At least one provider date is required for granule metadata in the CMR. The ‘ProviderDates’ element presents dates associated with changes made to the granule in the database where it is stored. The Provider Dates include the date the granule was created, inserted, or updated in its database, and the date the granule metadata will be deleted from the CMR. It is highly recommended that the ‘Create’ date be included. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Provider+Dates"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Provider+Dates</span></a></p>
<p>B2.2.17b STAC: Provide the date the Item record was created using ‘properties &gt; created’ <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/item-spec/common-metadata.md#date-and-time"><span class="underline">https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/item-spec/common-metadata.md#date-and-time</span></a> [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.18 Provide a reference to the associated collection in the granule level metadata</td>
<td><p>B2.2.18a UMM: The Collection Reference identifies the collection to which the granule belongs. This is done by providing the collection's Short Name and Version Id, or the collection's Entry Title in the ‘CollectionReference’ element. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Collection+Reference"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Collection+Reference</span></a></p>
<p>B2.2.18b STAC: Provide the id of the associated STAC Collection in the ‘collection’ element. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.19 Provide the metadata specification information in the granule level metadata</td>
<td><p>B2.2.19a UMM: Populate the ‘MetadataSpecification’ element. The Metadata Specification element requires the user to add in schema information into every granule record. It includes the schema's name, version, and URL location. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Metadata+Specification"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Metadata+Specification</span></a></p>
<p>B2.2.19b: STAC: Provide a value of “Feature” in the STAC ‘type’ element and the version of STAC the Item implements in the ‘stac_version’ element. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.20 Provide the temporal extent information in the granule level metadata</td>
<td><p>B2.2.20a UMM: File level temporal extent information is not required per UMM but is highly recommended to enable more targeted discovery. Ensure file level temporal information does not contradict collection level information. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Temporal+Extents"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Temporal+Extents</span></a></p>
<p>B2.2.20b STAC: The temporal information should be provided in the <a href="https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#properties-object"><span class="underline">Properties Object</span></a> -&gt; ‘datetime’ element. If the file can be represented as a single datetime, the time stamp can be provided directly in the ‘datetime’ element. If the temporal extent is a temporal range, then a value of “null” should be provided in ‘datetime’ followed by the ‘start_datetime’ and ‘end_datetime’ elements. Timestamps should consist of a date and time in UTC and MUST be formatted according to <a href="https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"><span class="underline">RFC 3339, section 5.6</span></a>. [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.21 Provide the spatial extent information in the granule level metadata</td>
<td><p>B2.2.21a UMM: File level spatial extent information is not required per UMM but is highly recommended to enable more targeted discovery. For specific files or granules, the spatial extent describes the area covered by that individual file. Ensure file level spatial information does not contradict collection level information. [DS] More details can be found here: <a href="https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Spatial+Extent</span></a></p>
<p>B2.2.21b STAC: The spatial information should be provided using either the ‘geometry’ element or the ‘bbox’ element. Use ‘geometry’ to provide a GeoJSON footprint, formatted according to <a href="https://tools.ietf.org/html/rfc7946#section-3.1">RFC 7946, section 3.1</a>. The footprint should be the default GeoJSON geometry, though additional geometries can be included. Coordinates are specified in Longitude/Latitude or Longitude/Latitude/Elevation based on <a href="http://www.opengis.net/def/crs/OGC/1.3/CRS84">WGS 84</a>. If ‘geometry’ is set to “null”, then providing a ‘bbox’ is required. The bbox should be formatted according to <a href="https://tools.ietf.org/html/rfc7946#section-5">RFC 7946, section 5</a>. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.2.22 Provide a link to access the data in the granule level metadata</td>
<td><p>B2.2.22a UMM: A link to access the data described by the granule metadata is not required per UMM but is highly recommended to enable data access. This link is provided in the ‘RelatedURLs’ element. The link goes in the ‘RelatedURLs -&gt; URL’ field, and this must be accompanied by a ‘RelatedURLs -&gt; Type’ value of “GET DATA”. An optional ‘Subtype’ can be provided to further describe the nature of the URL. It is recommended that the link also be accompanied by a description. [DS] Additional details can be found here: <a href="https://wiki.earthdata.nasa.gov/pages/viewpage.action?pageId=138875957"><span class="underline">RelatedURLs (Granules)</span></a></p>
<p>B2.2.22b STAC: There are two required STAC elements to consider here. First is the ‘links’ element which is a list of <a href="https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#link-object"><span class="underline">Link Objects</span></a> to resources and related URLs. At minimum, a link with the ‘rel’ set to “self” is strongly recommended. It is encouraged that links pointing to other related STAC resources are also provided, such as a link to the associated collection and root or parent entity. Additional information can be found here: <a href="https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#link-object"><span class="underline">Link Object</span></a>. The second is the ‘assets’ element which is a dictionary of <a href="https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#asset-object"><span class="underline">Asset Objects</span></a> that can be downloaded, each with a unique key. This element is key to facilitating data access, as it contains a URI to data associated with the Item that can be downloaded or streamed. Details can be found here: <a href="https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md#asset-object"><span class="underline">Asset Object</span></a> [DS + DE]</p></td>
</tr>
<tr class="odd">
<td>A2.2.23 Preserve data provenance (preserve metadata from original source, and data editing history)</td>
<td><p>B2.2.23a TBD: UMM: Implementation procedure for data provenance.</p>
<p>B2.2.23b TBD: STAC Implementation procedure for data provenance</p></td>
</tr>
</tbody>
</table>
