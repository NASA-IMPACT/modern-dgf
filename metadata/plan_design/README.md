**2.1 Planning and Design**
-----------------------

<table>
<thead>
<tr class="header">
<th><strong>Requirement</strong></th>
<th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A2.1.1 Adhere to a standard metadata schema for data product (collection) and file (granule) level metadata</td>
<td><p>B2.1.1 Utilize the UMM or STAC schema [DS + DE]</p>
<ul>
<li><blockquote>
<p>UMM schema: <a href="https://git.earthdata.nasa.gov/projects/EMFD/repos/unified-metadata-model/browse"><span class="underline">UMM Schemas</span></a></p>
</blockquote></li>
<li><blockquote>
<p>STAC Spec: <a href="https://github.com/radiantearth/stac-api-spec/tree/main/stac-spec"><span class="underline">STAC Spec</span></a></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>A2.1.2 Support mandatory metadata elements in the selected schema</td>
<td><p>B2.1.2a UMM: Ensure that the metadata schema includes the following: [DS]</p>
<ul>
<li><blockquote>
<p>UMM <a href="https://wiki.earthdata.nasa.gov/display/CMR/UMM-C+Schema+Representation"><span class="underline">Collection-Level mandatory fields</span></a>: Metadata Specification, Entry Title, DOI, Abstract, Data Center, Processing Level, Collection Progress, Science Keywords, Temporal Extents, Spatial Extent, Platform, Related URL, Short Name, Version</p>
</blockquote></li>
<li><blockquote>
<p>UMM <a href="https://wiki.earthdata.nasa.gov/display/CMR/UMM-G+Schema+Representation"><span class="underline">Granule-Level</span></a> mandatory fields: Granule UR, Provider Dates, Collection Reference, Metadata Specification</p>
</blockquote></li>
</ul>
<p>B2.1.2b STAC: Ensure that the metadata schema includes the following: [DS]</p>
<ul>
<li><blockquote>
<p>STAC <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/collection-spec/collection-spec.md"><span class="underline">Collection-Level</span></a> mandatory fields: type, stac_version, id, description, license, extent, links</p>
</blockquote></li>
<li><blockquote>
<p>STAC <a href="https://github.com/radiantearth/stac-api-spec/blob/main/stac-spec/item-spec/item-spec.md"><span class="underline">Granule(Item)-Level</span></a> mandatory fields: type, stac_version, id, geometry, bbox, properties, links, assets</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>A2.1.3 Utilize a standard data product naming convention</td>
<td>B2.1.3 Use the ARC guidelines when developing a data product naming convention - “The Entry Title should be a descriptive, formal title of the dataset. The Entry Title should not be the same as the <a href="https://wiki.earthdata.nasa.gov/display/CMR/Short+Name"><span class="underline">Short Name</span></a> element. It is recommended that the Entry Title follow a mixed case capitalization scheme and that the use of special characters (such as underscores) and acronyms be kept to a minimum, if possible. In order to make titles descriptive, important elements about the data may be included, such as: parameters measured, geographic location, instrument, project, temporal coverage, etc.” Link for more info <a href="https://wiki.earthdata.nasa.gov/display/CMR/Entry+Title"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Entry+Title</span></a> [DS]</td>
</tr>
<tr class="even">
<td>A2.1.4 Identify any needed additional metadata fields for specific projects</td>
<td><p>B2.1.4a UMM: Review entire schema and determine what optional elements are needed. Where available, use existing optional elements. If needed, leverage custom UMM <a href="https://wiki.earthdata.nasa.gov/display/CMR/Additional+Attributes"><span class="underline">Additional Attribute</span></a> fields. For example, the <a href="https://docs.google.com/document/d/1Cwn97mRC5F2kj1Ul7hu54D4PVgEPiLrOKR--vHKXoIM/edit?usp=sharing"><span class="underline"> MAAP project developed SAR specific element</span></a>s that were implemented as Additional Attributes. [DS]</p>
<p>B2.1.4b STAC: Review the <a href="https://stac-extensions.github.io/#grouped-by-maturity"><span class="underline">available STAC extensions</span></a>. [DE?] Extensions should be selected using the following criteria:</p>
<ul>
<li><blockquote>
<p>Relevance to the data being described. Projection, item assets, electro-optical (EO), raster and SAR are commonly used extensions.</p>
</blockquote></li>
<li><blockquote>
<p>Maturity of the STAC extension. Only mature extensions (pilot, candidate or stable) should be utilized.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>A2.1.5 Incorporate any access control fields into the metadata, as required</td>
<td><p>B2.1.5a UMM: Utilize the ‘Access Constraints’ element to define constraints as needed. <a href="https://wiki.earthdata.nasa.gov/display/CMR/Access+Constraints"><span class="underline">https://wiki.earthdata.nasa.gov/display/CMR/Access+Constraints</span></a> [DS]</p>
<p>B2.1.5b TBD: STAC: The best practice for providing Access Constraints using the STAC Collection spec is still TBD. [DS + DE]</p></td>
</tr>
<tr class="even">
<td>A2.1.6 Define the data product citation</td>
<td><p>B2.1.6 Work with the data provider, the principal investigator (PI), or others to come to a consensus on how the data product should be cited. This should include identifying the main contributors to the data product, the order of the contributors in the citation and the data product name. [DS]</p>
<p>Citation should include:</p>
<ul>
<li><blockquote>
<p>Author(s) or project name(s): The people or organizations responsible for the intellectual work to develop the data product</p>
</blockquote></li>
<li><blockquote>
<p>Date published: When the particular version of the data set was first made available for use</p>
</blockquote></li>
<li><blockquote>
<p>Title: The formal title of the data set</p>
</blockquote></li>
<li><blockquote>
<p>Release version: Current data version</p>
</blockquote></li>
<li><blockquote>
<p>Repository: The name of the entity that holds, archives, publishes, distributes, or releases the data</p>
</blockquote></li>
<li><blockquote>
<p>DOI: Resolvable persistent identifier that provides the ability to access data</p>
</blockquote></li>
<li><blockquote>
<p>Access date: Date of online data were accessed</p>
</blockquote></li>
<li><blockquote>
<p>Resource type: [dataset]</p>
</blockquote></li>
</ul>
<p>Sources: <a href="https://www.agu.org/Publish-with-AGU/Publish/Author-Resources/Data-and-Software-for-Authors"><span class="underline">AGU Data and Software Citation</span></a>; <a href="https://esip.figshare.com/articles/online_resource/Data_Citation_Guidelines_for_Earth_Science_Data_Version_2/8441816"><span class="underline">ESIP Data Citation Guidelines for Earth Science Data</span></a></p></td>
</tr>
</tbody>
</table>
