**2.6 Monitoring**
------------------

<table>
<thead>
<tr class="header">
<th><strong>Requirement</strong></th>
<th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>A2.6.1 Monitor and report metadata quality metrics</td>
<td>B2.6.1 Use <a href="https://github.com/NASA-IMPACT/pyQuARC"><span class="underline">pyQuARC</span></a> to generate metadata quality metrics. <a href="https://quarc.nasa-impact.net/docs/#/default/post_validate"><span class="underline">QuARC is also available via an API.</span></a> [DE]</td>
</tr>
<tr class="even">
<td>A2.6.2 Monitor changes to the metadata schema used</td>
<td><p>B2.6.2a Update the schema to the latest version. More information on <a href="https://wiki.earthdata.nasa.gov/pages/viewpage.action?pageId=210801058"><span class="underline">UMM schemas can be found here</span></a>. More information on the <a href="https://github.com/radiantearth/stac-spec"><span class="underline">STAC specification can be found here.</span></a> [DE]</p>
<p>B2.6.2b Update the content for each metadata record to be compliant with the new schema changes [DS+DE]</p></td>
</tr>
<tr class="odd">
<td>A2.6.3 Monitor changes to controlled vocabularies</td>
<td><p>B2.6.3a Update controlled vocabulary keywords in metadata (e.g., GCMD; CF); [DS]</p>
<p>B2.6.3b Remove deprecated keywords, as needed [DS + DE]</p></td>
</tr>
</tbody>
</table>
