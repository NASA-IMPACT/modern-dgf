**1.1 Planning and Design**
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
<td>A1.1.1 Define a data flow diagram with the purpose of identifying data sources and touchpoints for the project and for communicating to data users how data was handled.</td>
<td><p>B1.1.1 Create a data flow diagram extending from acquisition/creation to user delivery and add diagram to DMP. [DE]</p>
<p>Example diagram: <img src="_images/image1.png" style="width:3.10417in;height:1.55556in" /></p></td>
</tr>
<tr class="even">
<td>A1.1.2 Develop touchpoint agreements identified in the data flow diagram</td>
<td>B1.1.2 Create needed touchpoint agreements such as Interface Control Documents, (ICDs) / Submission Agreement (SA), Memorandum of Understanding (MOU),or Service Level Agreement (SLA). [DS + DE]</td>
</tr>
<tr class="odd">
<td>A1.1.3 Adhere to community accepted standard machine readable data file formats</td>
<td><p>B1.1.3 Select standard machine-readable data file format(s) from <a href="https://www.earthdata.nasa.gov/esdis/esco/standards-and-practices#data-formats"><span class="underline">NASA Approved Data Formats</span></a> [DS]</p>
<ul>
<li><blockquote>
<p>The <a href="https://doi.org/10.5067/DOC/ESO/DPDG_QSG_VERSION1"><span class="underline">EOSDIS Data Product Development Guide for Data Producers - Quick Start Guide</span></a> prefers the following data formats: netCDF-4 and GeoTIFF.</p>
</blockquote></li>
<li><blockquote>
<p>Cloud Optimized GeoTIFF (COG) and Zarr are the preferred Cloud-based formats</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>A1.1.4 Identify and document all data product characteristics</td>
<td>B1.1.4 Create a data sheet using the following template: <a href="https://docs.google.com/document/d/1FqAPO0jwMk7rzxJTkHFuOpwOvHviQDW2/edit#heading=h.gjdgxs"><span class="underline">Data Sheet Template</span></a><em>.</em> Add additional data characteristics as needed for each project. [DS]</td>
</tr>
<tr class="odd">
<td>A1.1.5 Adhere to community best practice(s) on data file naming conventions</td>
<td>B1.1.5 Define and document file naming conventions using following guidelines: <a href="https://ghrc.nsstc.nasa.gov/home/sites/default/files/GHRC_naming_convention.pdf"><span class="underline">GHRC File Naming convention</span></a> [DS]</td>
</tr>
<tr class="even">
<td>A1.1.6 Adhere to community standard variable names, types, and unit(s), keywords</td>
<td>B1.1.6 Utilize standard variable(s), types, and unit(s) such as <a href="http://cfconventions.org/"><span class="underline">CF convention</span> <span class="underline"> </span></a>[DS]</td>
</tr>
<tr class="odd">
<td>A1.1.7 Adhere to community standards for coordinate systems</td>
<td><p>B1.1.7 Utilize coordinate reference systems (CRS) from this list (<a href="https://epsg.io/"><span class="underline">https://epsg.io/</span></a>) [DE]</p>
<ul>
<li><blockquote>
<p>Recommended global CRS:</p>
</blockquote>
<ul>
<li><blockquote>
<p>2-dimensional World Geodetic System 1984 (WGS 84) (Lat/Long): <a href="https://epsg.io/4326"><span class="underline">EPSG:4326</span></a></p>
</blockquote>
<ul>
<li><blockquote>
<p>WGS 84 World Mercator: <a href="https://epsg.io/3395"><span class="underline">EPSG:3395</span></a></p>
</blockquote></li>
<li><blockquote>
<p>WGS 84 Pseudo-Mercator: <a href="https://epsg.io/3857"><span class="underline">EPSG:3857</span></a></p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>3-dimensional WGS 84 (Lat/Long/Elevation)<span class="underline">:</span> <a href="https://epsg.io/4979"><span class="underline">EPSG:4979</span></a></p>
</blockquote></li>
</ul></li>
<li><blockquote>
<p>Recommended CRS for data over polar regions:</p>
</blockquote>
<ul>
<li><blockquote>
<p>WGS 84 Arctic Polar Stereographic: <a href="https://epsg.io/3995"><span class="underline">EPSG:3995</span></a></p>
</blockquote>
<ul>
<li><blockquote>
<p>NSIDC Sea Ice Polar Stereographic North: <a href="https://epsg.io/3413"><span class="underline">EPSG:3413</span></a></p>
</blockquote></li>
<li><blockquote>
<p>NSIDC Sea Ice Polar Stereographic South: <a href="https://epsg.io/3976"><span class="underline">EPSG:3976</span></a></p>
</blockquote></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td>A1.1.8 Adhere to community standards for map projections</td>
<td>B1.1.8 Utilize map projections from this list (<a href="https://epsg.io/"><span class="underline">https://epsg.io/</span></a>) [DE]</td>
</tr>
<tr class="odd">
<td>A1.1.9 Adhere to community standards for date and time formats</td>
<td>B1.1.9 Utilize data and time formatting from <a href="https://www.w3.org/TR/NOTE-datetime"><span class="underline">ISO 8601</span></a> [DE]</td>
</tr>
<tr class="even">
<td>A1.1.10 Define a data product versioning scheme</td>
<td>B1.1.10 Represent the data product version with an ordinal identifier (e.g., 1, 2, 3, etc.) that expresses its position in a series of data product publications. The data product version can be represented with both a major and minor version identifier (e.g., 2.1, 2.2, etc.). (Reference: see Section 4.3 of the <a href="https://www.earthdata.nasa.gov/s3fs-public/2022-06/ESDS-RFC-041-DPDG_V1.1-20220516_0.pdf?VersionId=0gPInlDI2oyQMh.RNC3e87qEnwcBdJzm"><span class="underline">Data Product Development Guide for Data Producers</span></a>) [DE]</td>
</tr>
<tr class="odd">
<td>A1.1.11 Define a science quality evaluation plan for data products</td>
<td><p>B1.1.11 Develop the characteristics of the science quality evaluation needed for each data product [DS]</p>
<p>Suggested:</p>
<ul>
<li><blockquote>
<p>Univariate visualization of each field in the raw dataset, with summary statistics and Fill Values, Mask Values</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>A1.1.12 Develop a data retention plan including a process for when and how data will be sunset</td>
<td>B1.1.12 Create a data retention plan that includes information about the end of project preservation plan and rolling archive plans. Use the <a href="https://docs.google.com/document/d/1nWOkkKoICDhb9VWcZF7cvp31pjtZyRP1VM3wqNj4HHo/edit"><span class="underline">CSDA data retirement policy template</span></a> as needed. [DS]</td>
</tr>
<tr class="odd">
<td><p>A.1.1.13 Define metrics to be collected along the following dimensions:</p>
<ul>
<li><blockquote>
<p>Data use (search and access)</p>
</blockquote></li>
<li><blockquote>
<p>Data quality</p>
</blockquote></li>
<li><blockquote>
<p>Data/information (quality) profile</p>
</blockquote></li>
<li><blockquote>
<p>Data Processing</p>
</blockquote></li>
<li><blockquote>
<p>Ingest</p>
</blockquote></li>
<li><blockquote>
<p>Data Access APIs/Services</p>
</blockquote></li>
</ul></td>
<td><p>B1.1.13 Develop a metrics implementation plan. [DE]</p>
<p>Recommended minimum metrics:</p>
<blockquote>
<p><strong>Data Use Metrics</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p>Data Product Search frequency</p>
</blockquote></li>
<li><blockquote>
<p>S3 Bucket Access frequency</p>
</blockquote></li>
<li><blockquote>
<p>Data download counts</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Information/Data Profile</strong>:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Data completeness</p>
</blockquote></li>
<li><blockquote>
<p>Metadata completeness</p>
</blockquote></li>
<li><blockquote>
<p>Data lineage completeness</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Data Quality</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p>Checksum validation</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Data Processing</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p>Processing time</p>
</blockquote></li>
<li><blockquote>
<p>Processing throughput</p>
</blockquote></li>
<li><blockquote>
<p>Error rate</p>
</blockquote></li>
<li><blockquote>
<p>Resource utilization</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Ingest</strong>:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Ingest rate</p>
</blockquote></li>
<li><blockquote>
<p>Ingest completeness / volume</p>
</blockquote></li>
<li><blockquote>
<p>Ingest error rate</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>Data Access APIs/Services</strong>:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Service availability</p>
</blockquote></li>
<li><blockquote>
<p>Service usage</p>
</blockquote></li>
<li><blockquote>
<p>Service response time</p>
</blockquote></li>
<li><blockquote>
<p>Service error rate</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>A1.1.14 Identify the most appropriate data license for the data product</td>
<td>B1.1.14 If there are no other restrictions, SMD scientific data should be released with a Creative Commons Zero license. [DS]</td>
</tr>
<tr class="odd">
<td>A1.1.15 Determine content and format for the dataset landing page</td>
<td><p>B1.1.15 Design dataset landing page format and content. Recommend using the <a href="https://docs.google.com/document/d/1qEoqYMh6K0QjY4HFqJ55yinwn4u0s22j88IAED583_U/edit?usp=sharing"><span class="underline">IMPACT data product landing page design</span></a>. [DS]</p>
<p>Note that dataset landing pages can be automatically generated using UMM metadata (published to CMR) and STAC metadata (using STAC Browser). All information needed in the dataset landing page should be included in the metadata.</p></td>
</tr>
<tr class="even">
<td>A1.1.16 Determine whether API-based data access is needed &amp; if so, identify an API standard</td>
<td><p>B1.1.16a Refer to your system design as to whether an API-based data access is needed. [DE] For example, databases that store vector data should have an API.</p>
<p>B1.1.16b If an API doesn’t already exist for the data being distributed, select an appropriate <a href="https://ogcapi.ogc.org/"><span class="underline">OGC API standard</span></a> to use (also see Requirement A1.4.2). For raster and map content, use <a href="https://ogcapi.ogc.org/maps/"><span class="underline">OGC API - Maps</span></a>. For vector and tile data, use <a href="https://ogcapi.ogc.org/tiles/"><span class="underline">OGC API - Tiles</span></a>. Also consider using <a href="https://ogcapi.ogc.org/features/overview.html"><span class="underline">OGC API - Features</span></a> as needed.[DE]</p></td>
</tr>
</tbody>
</table>
